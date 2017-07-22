# Coding: utf-8

venda = float(input('Qual o valor da venda neste mês?'))
markup = float(input('Quanto em % é o markup de sua empresa?'))
cfixo = float(input('Qual foi o custo fixo de sua empresa este mês?'))
cvar = float(input('Qual foi o custo variável da sua empresa este mês'))
custos = cfixo + cvar
margem = venda * (markup/100)
lucro = margem - custos
if (markup<= 0):
    print('Infelizmente com esse Markup sua empresa não consegue ter Lucro !')
elif(margem<custos):
    print('Você teve Prejuizo este mês !')
    print('Seu prejuizo foi de: R$ ', lucro)
elif(margem>custos):
    print('Você lucrou neste mês !')
    print('Seu lucro foi de: R$ ', lucro)






