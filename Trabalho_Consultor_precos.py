    #fiz para aprender um pouco um sistema de moedas, onde se pode ver o preço em diferentes moedas, embora eu tenha aprendido mais sobre economia do que programação, eu me diverti
    #nota: passei meia hora para descobrir como juntar float e string para descobrir q era colocar uma "," ao inves de "+"
Maca_fruta_BRL = 1.00
banana_fruta_BRL = 0.50
Laranja_fruta_BRL = 0.75
Uva_fruta_BRL = 2.00
Pera_fruta_BRL = 1.50
#valores covertidos aproximados do dia 28/4 as 14:40
maca_fruta_ARG = 172
banana_fruta_ARG = 86
Laranja_fruta_ARG = 129
Uva_fruta_ARG = 343
Pera_fruta_ARG = 257
#valores covertidos aproximados do dia 28/4 as 14:40
maca_fruta_PU = 0.74
banana_fruta_PU = 0.37
Laranja_fruta_PU = 0,55
Uva_fruta_PU = 1.74
Pera_fruta_PU = 1.10

moeda_BR = "R$"
moeda_AR = "A$"
moeda_PU = "S/"

print ("Selecione uma moeda")
print ("Real Brasileiro - R$ [1]")
print ("Peso Argentino - A$ [2]")
print ("Novo Sol - S/ [3]")

moeda_escolhida = input('Escolha uma moeda:')
if moeda_escolhida == '1':
    print ("Consultor de Preços")
    print ("Maçã: [1]")
    print ("Banana [2]")
    print ("Laranja [3]")
    print ("Uva [4]")
    print ("Pêra [5]")
    opcao_escolhida = input('Escolha uma opção:')
    if opcao_escolhida == '1':
        print (moeda_BR, Maca_fruta_BRL)
    if opcao_escolhida == '2':
        print (moeda_BR, banana_fruta_BRL)
    if opcao_escolhida == '3':
        print (moeda_BR, Laranja_fruta_BRL)
    if opcao_escolhida == '4':
        print (moeda_BR, Uva_fruta_BRL)
    if opcao_escolhida == '5':
        print (moeda_BR, Pera_fruta_BRL)
else: print ('Opção Inválida')


if moeda_escolhida == '2':
    print ("Consultor de Preços")
    print ("Maçã: [6]")
    print ("Banana [7]")
    print ("Laranja [8]")
    print ("Uva [9]")
    print ("Pêra [10]")
    opcao_escolhida = input('Escolha uma opção:')
    if opcao_escolhida == '6':
        print (moeda_AR, maca_fruta_ARG)
    if opcao_escolhida == '7':
        print (moeda_AR, banana_fruta_ARG)
    if opcao_escolhida == '8':
        print (moeda_AR, Laranja_fruta_ARG)
    if opcao_escolhida == '9':
        print (moeda_AR, Uva_fruta_ARG)
    if opcao_escolhida == '10':
        print (moeda_AR, Pera_fruta_ARG)
else: print ('Opção Inválida')
if moeda_escolhida == '3':
    print ("Consultor de Preços")
    print ("Maçã: [11]")
    print ("Banana [12]")
    print ("Laranja [13]")
    print ("Uva [14]")
    print ("Pêra [15]")
    opcao_escolhida = input('Escolha uma opção:')
    if opcao_escolhida == '11':
        print (moeda_PU, maca_fruta_PU)
    if opcao_escolhida == '12':
        print (moeda_PU, banana_fruta_ARG)
    if opcao_escolhida == '13':
        print (moeda_PU, Laranja_fruta_PU)
    if opcao_escolhida == '14':
        print (moeda_PU, Uva_fruta_PU)
    if opcao_escolhida == '15':
        print (moeda_PU, Pera_fruta_PU)
else: print ('Opção Inválida')