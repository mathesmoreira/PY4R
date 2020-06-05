# Programa cria uma classe 'GenderDetector' que
# faz um request pro api.genderize.io retornando
# o genero do nome informado

import requests


class GenderDetector():
    def run(self, name):
        result = requests.get('https://api.genderize.io/'
                              '?name={}'.format(name)).json()
        return print(result['gender'])


# Testando classe
gender = GenderDetector()
gender.run('Mateus')
