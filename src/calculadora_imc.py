def calculadora_imc(massa, altura, idade, preciso=False):
    # Verifica a idade para definir se o índice é válido
    if(idade < 18):
        return 'IMC inválido para crianças e adolescentes', 0
    if(idade > 60):
        return 'IMC inválido para idosos', 0

    # Define se o cálculo do IMC será tradicional ou preciso
    if(preciso):
        imc = (1.3 * massa)/(altura**2.5)
    else:
        imc = massa/(altura**2)

    # Encontra a situação correspondente ao IMC
    if(imc < 17):
        return 'Muito abaixo do peso', imc
    elif(17 <= imc < 18.5):
        return 'Abaixo do peso', imc
    elif(18.5 <= imc < 25):
        return 'Peso normal', imc
    elif(25 <= imc < 30):
        return 'Acima do peso', imc
    elif(30 <= imc < 35):
        return 'Obesidade', imc
    elif(35 <= imc < 40):
        return 'Obesidade severa', imc
    elif(imc >= 40):
        return 'Obesidade mórbida', imc
    else:
        return 'Inválido', 0 