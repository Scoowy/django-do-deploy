import json
from typing import Any


def read_cache_file(file_path) -> dict[str, Any]:
    try:
        with open(file_path, encoding='utf-8', mode='r') as file:
            cache_json = json.loads(file.read())
            print('[ALERT]: Cache readed')
            return cache_json
    except Exception as e:
        print(f'[ERROR]: {e}')
        print(f'[ALERT]: Error al leer el archivo de cache')
        return {}


def write_cache_file(data, file_path) -> None:
    try:
        with open(file_path, encoding='utf-8', mode='w') as file:
            cache_text = json.dumps(data, indent=1)
            file.write(cache_text)
            print('[ALERT]: Cache writed')
    except Exception as e:
        print(f'[ERROR]: {e}')
        print(f'[ERROR]: Error al escribir el archivo de cache')
