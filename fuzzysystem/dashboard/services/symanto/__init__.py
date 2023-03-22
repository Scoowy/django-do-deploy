from concurrent.futures import ThreadPoolExecutor
import requests
import typing as tp
import pandas as pd
import json

from dashboard.services.files import add_prefix

from ..cache import read_cache_file, write_cache_file

from django.conf import settings


__EMOTION_ENDPOINT = 'https://ekman-emotion-analysis.p.rapidapi.com/ekman-emotion'
__PERSONALITY_ENDPOINT = 'https://personality-traits.p.rapidapi.com/personality'


__SYMANTO_API_KEY = settings.SYMANTO_API_KEY
# __SYMANTO_API_KEY = '6dd8dcb6acmsh0ae0691ab41c058p119ad5jsnd876ea394d69'
__SYMANTO_PAYLOAD_BASE = {
    "language": 'es'
}
__SYMANTO_HEADERS_BASE = {
    "content-type": 'application/json',
    "Accept": 'application/json',
    "X-RapidAPI-Key": __SYMANTO_API_KEY,
}

SYMANTO_HEADERS_EMOTION = {
    "X-RapidAPI-Host": 'ekman-emotion-analysis.p.rapidapi.com',
    ** __SYMANTO_HEADERS_BASE
}
SYMANTO_HEADERS_PERSONALITY = {
    "X-RapidAPI-Host": 'personality-traits.p.rapidapi.com',
    ** __SYMANTO_HEADERS_BASE
}

# === TYPOS ===
PredictionItemType = tp.TypedDict('PredictionItemType', {
    'id': str | int,
    'predictions': list[tp.TypedDict('PredictionType', {
        'prediction': str,
        'probability': float
    })]
})

CacheItemType = tp.TypedDict('CacheItemType', {
    "rasgo": list,
    "emocion": list
})

CacheSymantoType = dict[str, CacheItemType]
# === TYPOS ===

SYMANTO_CACHE: CacheSymantoType = {}

writed_sentences = 0
readed_sentences = 0
fetched_sentences = 0
processed_sentences = 0


def post_url(args) -> tuple[str, list[PredictionItemType]]:
    fetch_type = args[0]  # 'emocion' | 'rasgo'
    res = requests.post(url=args[1], json=args[2], headers=args[3]).json()
    return fetch_type, res


def fetch_symanto(student_id: int, sentences: list[str]) -> list[list[CacheItemType]]:
    global readed_sentences, fetched_sentences, writed_sentences, processed_sentences, SYMANTO_CACHE

    processed_sentences += 8

    emotions: list[PredictionItemType] = []
    personalities: list[PredictionItemType] = []
    sentences_for_fetch: list[str] = []

    # Prepare Payload
    payload = []

    for i, student_text in enumerate(sentences):
        if student_text not in SYMANTO_CACHE:
            payload.append({
                'id': i,
                'text': student_text,
                'language': 'es'
            })
            emotions.append({})
            personalities.append({})
            sentences_for_fetch.append(student_text)
        else:
            emotions.append({
                'id': student_id,
                'predictions': SYMANTO_CACHE[student_text]['emocion']
            })
            personalities.append({
                'id': student_id,
                'predictions': SYMANTO_CACHE[student_text]['rasgo']
            })

            readed_sentences += 1

    emotions_fetched: list[PredictionItemType] = []
    personalities_fetched: list[PredictionItemType] = []

    if len(payload) != 0:
        list_of_urls = [
            ('emocion', __EMOTION_ENDPOINT, payload, SYMANTO_HEADERS_EMOTION),
            ('rasgo', __PERSONALITY_ENDPOINT, payload, SYMANTO_HEADERS_PERSONALITY)
        ]

        # Aqui
        with ThreadPoolExecutor(max_workers=2) as pool:
            responses = list(
                pool.map(post_url, list_of_urls))

        fetched_sentences += 2

        # print(responses)

        emotions_fetched = [res for i, res in responses if i == 'emocion'][0]
        personalities_fetched = [res for i,
                                 res in responses if i == 'rasgo'][0]

    for emotion, personality, sentence in zip(emotions_fetched, personalities_fetched, sentences_for_fetch):
        print(
            f'[INFO]: SENTENCE: {sentence}\n        EMOTION: {emotion}\n        PERSONALITY: {personality}')

        emotions[int(emotion['id'])] = {
            'id': student_id,
            'predictions': emotion['predictions']
        }

        personalities[int(personality['id'])] = {
            'id': student_id,
            'predictions': personality['predictions']
        }

        SYMANTO_CACHE[sentence] = {
            'emocion': emotion['predictions'],
            'rasgo': personality['predictions']
        }

        writed_sentences += 1

    combined_results: list[list[CacheItemType]] = []

    for emotion, personality in zip(emotions, personalities):
        combined_results.append({
            'emocion': [emotion][0]['predictions'][0],
            'rasgo': [personality][0]['predictions'][0]
        })

    return combined_results


def symanted_data(filename: str, cache_filename: str = None):
    global SYMANTO_CACHE

    df: pd.DataFrame = None

    try:
        df = pd.read_excel(f'./media/{filename}')
        df = prepare_data(df)
    except Exception as err:
        print(f'[ERROR]: {err}')
        return False, filename, err

    # Create a new DataFrame with same columns
    new_df = pd.DataFrame(columns=df.columns)

    try:
        # Leer el archivo de cache
        if cache_filename != None:
            SYMANTO_CACHE = read_cache_file(f'./media/{cache_filename}')

        # Extract a list of sentences
        for _, row in df.iterrows():
            if cache_filename != None:
                # Escribir la cache
                write_cache_file(SYMANTO_CACHE, f'./media/{cache_filename}')

            student_id = row['studentID']
            student_texts = row.loc['Q1':'Q8'].tolist()

            combined_results = fetch_symanto(student_id, student_texts)

            # print(combined_results)

            new_df = pd.concat([new_df, pd.DataFrame([{'studentID': row['studentID'], 'Professor': row['Professor'], 'Course': row['Course'],
                                                       'Q1': json.dumps(combined_results[0]),
                                                       'Q2': json.dumps(combined_results[1]),
                                                       'Q3': json.dumps(combined_results[2]),
                                                       'Q4': json.dumps(combined_results[3]),
                                                       'Q5': json.dumps(combined_results[4]),
                                                       'Q6': json.dumps(combined_results[5]),
                                                       'Q7': json.dumps(combined_results[6]),
                                                       'Q8': json.dumps(combined_results[7])}])], ignore_index=True)

        # Exportar xlsx
        symanted_filename = add_prefix(filename, prefix='symanted')
        new_df.to_excel(f'./media/{symanted_filename}', index=False)

        if cache_filename != None:
            # Escribir la cache
            write_cache_file(SYMANTO_CACHE, f'./media/{cache_filename}')

        print(
            f'[INFO]: {processed_sentences} sentences - {fetched_sentences} fetched | {writed_sentences} writed | {readed_sentences} readed')

        return True, symanted_filename, None

    except Exception as err:
        print(f'[ERROR]: {err}')
        print(err.with_traceback())
        return False, filename, err


def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    new_df = df.rename(columns={df.columns[0]: 'studentID',
                       df.columns[1]: 'course',
                       df.columns[2]: 'Q1',
                       df.columns[3]: 'Q2',
                       df.columns[4]: 'Q3',
                       df.columns[5]: 'Q4',
                       df.columns[6]: 'Q5',
                       df.columns[7]: 'Q6',
                       df.columns[8]: 'Q7',
                       df.columns[9]: 'Q8',
                                })

    new_df['Professor'] = new_df['course'].str.split("(").str[1].str.strip(")")
    new_df['Course'] = new_df['course'].str.split("(").str[0].str.strip()

    new_df = new_df.drop(columns=['course'])
    new_df = new_df[['studentID', 'Professor', 'Course', 'Q1',
                     'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8']]

    return new_df
