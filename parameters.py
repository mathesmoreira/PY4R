# Programa, através da funcao greet, recebe um
# idioma escolhido e imprimi uma saudacao com
# o nome

def greet(lang):
    if lang == 'es':
        return 'Holla'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'


lingua = str(input('Choose one language : espanhol/frances/ingles: '))

if lingua == 'ingles':
    print(greet('en') + ' Josefina')
elif lingua == 'frances':
    print(greet('fr') + ' Josefino')
elif lingua == 'espanhol':
    print(greet('es') + ' Josefao')
else:
    print('Nao sei essa lingua')
