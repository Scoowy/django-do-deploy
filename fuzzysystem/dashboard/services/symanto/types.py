from typing import Literal, TypedDict


SymantoHostType = Literal['ekman-emotion-analysis.p.rapidapi.com'] | Literal['personality-traits.p.rapidapi.com']
JsonContentType = Literal['application/json']

SymantoPayloadType = TypedDict('SymantoPayloadType', {
    "id": int,
    "languaje": str,
    "text": list[str]
})

SymantoHeadersType = TypedDict('SymantoHeadersType', {
    "content-type": JsonContentType,
    "Accept": JsonContentType,
    "X-RapidAPI-Key": str,
    "X-RapidAPI-Host": SymantoHostType
})

SymantoPredictionType = TypedDict('SymantoPredictionType', {
    "prediction": str,
    "probability": float
})

SymantoResponseObjType = TypedDict('SymantoResponseJsonObjType', {
    "id": str,
    "predictions": list[SymantoPredictionType]
})

SymantoResponseType = list[SymantoResponseObjType]

ResponseType = Literal['rasgo'] | Literal['emocion']

DataRequestType = TypedDict('DataRequestType', {
    'Professor': str,
    'Course': str,
    'Q1': str,
    'Q2': str,
    'Q3': str,
    'Q4': str,
    'Q5': str,
    'Q6': str,
    'Q7': str,
    'Q8': str
})

StudentRowsData = TypedDict('StudentRowsData', {
    "id": int,
    "texts": list[str]
})

CacheStoragePredictionType = TypedDict('CacheStoragePredictionType', {
    "rasgo": list[SymantoPredictionType],
    "emocion": list[SymantoPredictionType]
})
