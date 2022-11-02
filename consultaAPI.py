import requests


def main(cep):

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    data = request.json()

    if 'erro' not in data:
        return data
    else:
        print('\nCEP inválido.')

