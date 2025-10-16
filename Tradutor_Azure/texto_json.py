def texto_para_json(texto):
    paragrafos = [p.strip() for p in texto.split('\n') if p.strip()]
    json_array = [{"text": p} for p in paragrafos]
    return json_array

def json_para_texto(json_saida):
    paragrafos = [item["translations"][0]["text"] for item in json_saida]
    texto_puro = "\n".join(paragrafos)
    return texto_puro

