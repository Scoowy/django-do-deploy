import json
import requests
import time
import pandas as pd
from pandas import DataFrame

from .constants import REPLACE_WORDS, API_URL, API_HEADERS
from ..cache import read_cache_file, write_cache_file
from ..files import add_prefix
from ..types import FunctionResponseType

SENTENCE_CACHE = {}

writed_sentences = 0
readed_sentences = 0
fetched_sentences = 0
processed_sentences = 0


def replace_words(sentence: str):
    for key, value in REPLACE_WORDS.items():
        sentence = sentence.replace(key, value)

    return sentence


def replace_word(sentence: str, word: str, replaced: str):
    if sentence.lower() == word:
        sentence = replaced

    return sentence


def clean_spaces(sentence): return sentence.strip()


def fetch_grammar(sentence: str):
    global readed_sentences, fetched_sentences, writed_sentences, processed_sentences, SENTENCE_CACHE

    processed_sentences += 1

    if sentence not in SENTENCE_CACHE:
        # Hacer fetch
        payload = {
            "text": sentence,
            "lang": 'es'
        }

        print(f'[FETCH]: \"{sentence}\"')
        res = requests.post(API_URL, json=payload, headers=API_HEADERS)
        res = json.loads(res.text)

        fetched_sentences += 1

        try:
            newSentence = res['correction']
            # Cacheamos respuesta
            print('[CACHE]: Writed cache')
            SENTENCE_CACHE[sentence] = newSentence

            writed_sentences += 1

            return newSentence

        except Exception as e:
            print(f'[ERROR]: {e}')
            print(f'[ERROR]: Sentence: \"{sentence}\"')
            return sentence
    else:
        print('[CACHE]: Readed cache')
        readed_sentences += 1
        return SENTENCE_CACHE[sentence]


def clean_data(filename: str, cache_file_path: str = None) -> FunctionResponseType:
    global SENTENCE_CACHE

    df: DataFrame = None

    try:
        df = pd.read_excel(f'./media/{filename}', index_col=0)
    except Exception as err:
        print(f'[ERROR]: {err}')
        return False, filename, err

    try:
        # Leer el archivo de cache
        if cache_file_path != None:
            SENTENCE_CACHE = read_cache_file(f'./media/{cache_file_path}')

        # Extraer las columnas necesarias
        df = df.iloc[:, [6, 9, 12, 15, 18, 21, 24, 27, 30]]

        # Limpieza del dataframe
        df = df.applymap(clean_spaces)
        df = df.applymap(replace_words)
        df = df.applymap(lambda x: replace_word(x, 'si', 'Si'))
        df = df.applymap(lambda x: replace_word(x, 'no', 'No'))
        df = df.applymap(lambda x: replace_word(x, 'sí', 'Si'))

        # Uso de la API para gramatica
        dfNew = df.iloc[:, 1:].applymap(fetch_grammar)
        df = pd.concat([df.iloc[:, 0], dfNew], axis=1)

        # Exportar xlsx
        cleaned_filename = add_prefix(filename, prefix='cleaned')
        df.to_excel(f'./media/{cleaned_filename}')

        if cache_file_path != None:
            # Escribir la cache
            write_cache_file(SENTENCE_CACHE, f'./media/{cache_file_path}')

        print(
            f'[INFO]: {processed_sentences} sentences - {fetched_sentences} fetched | {writed_sentences} writed | {readed_sentences} readed')

        return True, cleaned_filename, None
    except Exception as err:
        print(f'[ERROR]: {err}')
        return False, filename, err


if __name__ == "__main__":
    initial_time = time.time()
    clean_data('test-file.xlsx', cache_file_path='words-cache.temp')
    running_time = time.time() - initial_time
    print(f'[INFO]: Total execution time: {running_time:.2f}s')
