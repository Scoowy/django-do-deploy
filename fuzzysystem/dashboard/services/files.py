from django.core.files.uploadedfile import UploadedFile
from .types import FunctionResponseType


def handle_uploaded_file(f: UploadedFile) -> FunctionResponseType:
    try:
        with open(f'./media/{f.name}', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

        return True, f.name, None

    except Exception as err:
        print(f'[ERROR]: {err}')
        return False, f.name, err


def add_prefix(filename: str, prefix: str) -> str:
    name = ''.join(filename.split('.')[:-1])
    extension = filename.split('.')[-1]

    return f'{name}_{prefix}.{extension}'
