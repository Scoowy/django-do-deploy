import pandas as pd
import json
from typing import TypedDict

from ..files import add_prefix

from . import methods as met

PredictionType = TypedDict('PredictionType', {
    'prediction': str,
    'probability': float
})

PredictionPairType = TypedDict('PredictionPairType', {
    'rasgo': PredictionType,
    'emocion': PredictionType
})

OPCIONES = {
    ('rational', 'sadness'): met.racionalTristeza,
    ('rational', 'surprise'): met.racionalSorpresa,
    ('rational', 'anger'): met.racionalEnfado,
    ('rational', 'fear'): met.racionalTemor,
    ('rational', 'disgust'): met.racionalAsco,
    ('rational', 'joy'): met.racionalDisfrute,
    ('rational', 'no-emotion'): met.racionalNoEmocion,
    ('emotional', 'sadness'): met.emocionalTristeza,
    ('emotional', 'surprise'): met.emocionalSorpresa,
    ('emotional', 'anger'): met.emocionalEnfado,
    ('emotional', 'fear'): met.emocionalTemor,
    ('emotional', 'disgust'): met.emocionalAsco,
    ('emotional', 'joy'): met.emocionalDisfrute,
    ('emotional', 'no-emotion'): met.emocionalNoEmocion,
}


def identify(rasgo: PredictionType, emocion: PredictionType):
    key = (rasgo['prediction'], emocion['prediction'])

    if key in OPCIONES:
        f = OPCIONES[key]
        return f(rasgo['probability'] * 100, emocion['probability'] * 100)
    else:
        print(f'No hay un método asociado para la opción {key}')
    return None


def fuzzed_data(filename: str):

    df: pd.DataFrame = None

    try:
        df = pd.read_excel(f'./media/{filename}')
    except Exception as err:
        print(f'[ERROR]: {err}')
        return False, filename, err

    try:
        # Fuzzing data
        # return True, diffused_filename, None
        fuzzed_colums = df.iloc[:, 3:].applymap(
            lambda pair: json.dumps(dict(identify(**(json.loads(pair))))))

        df = pd.concat([df.iloc[:, :3], fuzzed_colums], axis='columns')

        # print(df.head())

        # Exportar xlsx
        diffused_filename = add_prefix(filename, prefix='diffused')
        df.to_excel(f'./media/{diffused_filename}', index=False)

        return True, diffused_filename, None
    except Exception as err:
        print(f'[ERROR]: {err}')
        print(err.with_traceback())
        return False, filename, err
