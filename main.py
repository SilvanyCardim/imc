#100 - Calculadora de IMC

def imc(peso, altura):
    imc = peso/(altura*altura)
    return imc

def condicao(sexo, peso, altura):
    condicao = imc(peso, altura)

    if sexo == 'M':
        if condicao < 20:
            return 'Abaixo do Normal.'
        elif 20 <= condicao < 25:
            return 'Peso Normal.'
        elif 25 <= condicao < 30:
            return 'Acima do Peso Ideal.'
        elif 30 <= condicao < 43:
            return 'Obesidade Moderada.'
        else:
            return 'Obesidade Mórbida'

    if sexo == 'F':
        if condicao < 19:
            return 'Abaixo do Normal.'
        elif 19 <= condicao < 24:
            return 'Peso Normal.'
        elif 24 <= condicao < 29:
            return 'Acima do Peso Ideal.'
        elif 29 <= condicao < 39:
            return 'Obesidade Moderada.'
        else:
            return 'Obesidade Mórbida.'

vAlt = False
while vAlt == False:
    alt = input('Altura: ')
    try:
        alt = float(alt)
        if alt < 1:
            print('Digite uma altura maior que 1.00. Tente novamente.')
        else:
            vAlt = True
    except:
        print('Digite apenas valores numéricos, utilizando "." como separador em caso de necessidade.')

vPeso = False
while vPeso == False:
    peso = input('Peso: ')
    try:
        peso = float(peso)
        if peso <= 0:
            print('Digite um peso acima de zero. Tente novamente.')
        else:
            vPeso = True
    except:
        print('Digite apenas valores numéricos, utilizando "." como separador em caso de necessidade.')

sexo = input('Sexo M/F: ').upper()
vImc = imc(peso, alt)
condicao = condicao(sexo, peso, alt)
print('IMC: {}'.format(vImc))
print('Condição: {}'.format(condicao))
print('Peso:{:.2f}kg\nAltura:{:.2f}'.format(peso, alt))
