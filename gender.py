import requests

class GenderDetector():
    def run(self, name):
        result = requests.get('https://api.genderize.io/?name={}'.format(name)).json()
        return print(result['gender'])

# gender = GenderDetector()
# gender.run('Mateus')