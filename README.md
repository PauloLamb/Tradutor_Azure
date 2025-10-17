# Tradutor_Azure
Um simples tradutor que utiliza a API de tradução do Azure

Aplicação inicial para teste das funcionalidades do Azure

config.py tem as chaves de acesso ao Azure
translate.py é a função de tradução propriamente
transliterate.py é a função que "traduz" a fonética de caracteres como japoneses, russos, etc
texto_json.py contém funções para converter texto em json e vice-versa, pois o tradutor do Azure só trabalha com json
main.py arquivo principal com um texto que serve de experimento onde é traduzido para japonês de depois transliterado para o alfabeto latino.

