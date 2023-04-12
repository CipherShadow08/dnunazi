import requests

url = "https://www.gov.br/mj/pt-br/escolasegura"

pagina = input("Informe o link da página a ser denunciada: ")

motivo = input("Informe o motivo da denúncia: ")

data = {
    'report[url]': pagina,
    'report[comment]': motivo
}

response = requests.post(url, data=data)

if response.status_code == 200:
    print("Denúncia enviada com sucesso!")
else:
    print("Erro ao enviar denúncia. Código de resposta:", response.status_code)

