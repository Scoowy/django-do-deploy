from enum import Enum
import json
from pathlib import Path
import re
from django.conf import settings
import pandas as pd

from .table_utils import ColumnTable


__EMOTION_VALUE_PATTERN = r'\[\(\'(\w+)\', (\d*.\d*)\), \(\'(\w*)\', (\d*.\d*)\)\]'
__PATTERN = re.compile(__EMOTION_VALUE_PATTERN)
__QUESTION_COLUMNS = [
    ColumnTable.Q1.value,
    ColumnTable.Q2.value,
    ColumnTable.Q3.value,
    ColumnTable.Q4.value,
    ColumnTable.Q5.value,
    ColumnTable.Q6.value,
    ColumnTable.Q7.value,
    ColumnTable.Q8.value
]
__FILTER_COLUMNS = [
    ColumnTable.PROFESSOR.value,
    ColumnTable.COURSE.value
]


def __extractProfessorAndCourseFilters(df: pd.DataFrame, groupby: list[str] = []):
    filters = {}
    professorsAndCourses = df.groupby(groupby).all().index.to_list()

    for professor, course in professorsAndCourses:
        if professor in filters:
            filters[professor].append(course)
        else:
            filters[professor] = [course]

    return filters

# TODO : Change funccion with json parser


def __extractSentimentsAndValues(x) -> tuple[str, float, str, float]:
    prediction: dict[str, float] = json.loads(x)
    emotionText, emotionValue = list(prediction.items())[0]

    emotionText2, emotionValue2 = None, None

    return emotionText, emotionValue, emotionText2, emotionValue2

# TODO : Now using json with data transport


def __extractSentiment(row, columns: list[str]):
    columnsIndex = 0
    for column in columns:
        et, ev, _, _ = __extractSentimentsAndValues(row[columnsIndex])
        row[f'{column}T'] = et
        row[f'{column}V'] = ev

        columnsIndex += 1
    return row


def __getAverageOfEmotions(row: pd.Series, columns: list[str] = []):
    emotions = {}

    for colum in columns:
        emotionT = row[f'{colum}T']
        emotionV = row[f'{colum}V']

        if row[f'{colum}T'] in emotions:
            emotions[emotionT]['count'] += 1
            emotions[emotionT]['sum'] += emotionV
        else:
            emotions[emotionT] = {'count': 1, 'sum': emotionV}

    for emotion, values in emotions.items():
        emotions[emotion] = values['sum'] / values['count']

    return emotions


def __getAvergeOfEmotionsDict(listOfDicts: list[dict[str, float]]):
    emotions = {}

    for row in listOfDicts:
        for emotion, value in row.items():
            if emotion in emotions:
                emotions[emotion]['count'] += 1
                emotions[emotion]['value'] += value
            else:
                emotions[emotion] = {'count': 1, 'value': value}

    for emotion, values in emotions.items():
        emotions[emotion] = values['value'] / values['count']

    return emotions


def extractDataFromExcelEmotion(filename: str, professor: str | None = None, course: str | None = None) -> tuple[list[str], list[str]]:
    df = pd.read_excel(filename)

    professorWithCourses = __extractProfessorAndCourseFilters(
        df[__FILTER_COLUMNS], groupby=__FILTER_COLUMNS)

    professors = list(professorWithCourses.keys())

    df_emotions = df.iloc[:, 3:].apply(lambda x: __extractSentiment(
        x, __QUESTION_COLUMNS), axis=1).iloc[:, -16:]

    df = pd.concat([df.iloc[:, :3], df_emotions], axis=1)

    # Extraction value of emotion
    professorFilter = df[ColumnTable.PROFESSOR.value] == professor
    courseFilter = df[ColumnTable.COURSE.value] == course

    df = df.loc[(professorFilter) & (courseFilter)].iloc[:, -16:
                                                         ] if professor and course else df.iloc[:, -16:]

    listOfSentimentsAndValues = df.apply(lambda row: __getAverageOfEmotions(
        row, __QUESTION_COLUMNS), axis=1).to_list()

    sentimentsWithValues = __getAvergeOfEmotionsDict(listOfSentimentsAndValues)

    numResponsesTotal = int(df.size / 2)

    numStudentTotal = df.loc[(professorFilter) & (courseFilter)
                             ].iloc[:, 0].size if professor and course else df.iloc[:, 0].size

    return professors, professorWithCourses, sentimentsWithValues, numStudentTotal, numResponsesTotal


def analyzeExcelFile(filename: str, professor: str, course: str):

    filenameDir = Path(settings.MEDIA_ROOT, filename)

    # filenameDir = Path('./media', filename)

    professors, professorsWithCourses, sentimentsWithValues, totalStudents, totalResponses = extractDataFromExcelEmotion(
        filenameDir, professor, course)

    print(sentimentsWithValues)

    emotions = list(sentimentsWithValues.keys())
    values = list(sentimentsWithValues.values())

    # Valores inversos
    valuesI = [100.0 - round(value, 2) for value in values]

    EMOTIONS_LABELS = {
        'responsabilidad': {
            'original': 'Responsabilidad',
            'inverse': 'Poco Conciente'
        },
        'amabilidad': {
            'original': 'Amabilidad',
            'inverse': 'Antagonismo'
        },
        'estEmocional': {
            'original': 'Estabilidad Emocional',
            'inverse': 'Neurotismo'
        },
        'apExperiencias': {
            'original': 'Apertura a experiencias',
            'inverse': 'Cierre a experiencias'
        },
        'extrovertido': {
            'original': 'Extrovertido',
            'inverse': 'Introversion'
        },
    }

    emotionsComplete = []

    for emotion in emotions:
        emotionsComplete.append(EMOTIONS_LABELS[emotion]['original'])
        emotionsComplete.append(EMOTIONS_LABELS[emotion]['inverse'])

    valuesComplete = []

    for index in range(len(values)):
        valuesComplete.append(round(values[index], 2))
        valuesComplete.append(round(valuesI[index], 2))

    # Adicionar al render la data
    context = {
        'professorSelected': professor if professor else 'Todos',
        'courseSelected': course if professor else 'Todos',
        'professors': professors,
        'professorsWithCourses': json.dumps(professorsWithCourses),
        'totalStudents': totalStudents,
        'totalResponses': totalResponses,
        'dataEmotions': {
            'emotions': json.dumps(emotionsComplete),
            'values': json.dumps(valuesComplete),
        },
        'filename': filename
    }

    return context
