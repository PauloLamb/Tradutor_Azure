import requests, uuid, json
from config import AZURE_KEY, AZURE_ENDPOINT, AZURE_LOCATION
from texto_json import texto_para_json, json_para_texto_transliteracao

key = AZURE_KEY
endpoint = AZURE_ENDPOINT
location = AZURE_LOCATION

def transliterate(texto, idioma_origem, pais_origem):
    path = '/transliterate'
    constructed_url = endpoint + path

    params = {
    'api-version': '3.0',    
    'language': idioma_origem,
    'fromScript': pais_origem,
    'toScript': 'latn'
}

    headers = {
    'Ocp-Apim-Subscription-Key': key,
    # location required if you're using a multi-service or regional (not global) resource.
    'Ocp-Apim-Subscription-Region': location,
    'Content-type': 'application/json',
    'X-ClientTraceId': str(uuid.uuid4())
    }

    body = texto_para_json(texto)
     
    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()

    return json_para_texto_transliteracao(response)