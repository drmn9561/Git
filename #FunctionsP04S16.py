#Functions
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fa':
        print('salam')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')
greet('fa')
greet('es')
greet('fr')