import requests 

cep = input("digite o seu CEP: ")
url = f"https://viacep.com.br/ws/{cep}/json/"

dados = requests.get(url)
resposta = dados.json()

print(resposta["logradouro"])

print(f"voce mora na {resposta["logradouro"]}, no bairro {resposta["complemento"]}, na cidade {resposta["localidade"]}")