#coding: utf-8
saque = int(input('Qual o valor do Saque ?'))
vlr100 = 0
vlr50 = 0
vlr20 = 0
vlr10 = 0
vlr5 = 0
vlr2 = 0
vlr1 = 0
nr100 = 0
nr50 = 0
nr20 = 0
nr10 = 0
nr5 = 0
nr2 = 0
nr1 = 0

while(saque > 500):
    print('O valor do Saque excede o valor máximo diário!')
    saque = int(input('Digite um valor abaixo de 500 R$'))

if(saque > 100):
    nr100 = int(saque/100)
    saque = saque % 100

if(saque > 50):
    nr50 = int(nr100/50)
    saque = saque % 50

if(saque > 20):
    nr20 = int(nr50/20)
    saque = saque % 20

if(saque > 10):
    nr10 = int(nr20/10)
    saque = saque % 10

if(saque > 5):
    nr5 = int(nr10/5)
    saque = saque % 5

if(saque > 2):
    nr2 = int(nr5/2)
    saque = saque % 2

if(saque > 1):
    nr1 = int(nr2/1)
    saque = saque % 1

print('Você receberá: ' )
if(nr100 != 0):
    print(nr100, 'Notas de 100 Reais')
if (nr50 != 0):
    print(nr50, 'Notas de 50 Reais')
if (nr20 != 0):
    print(nr20, 'Notas de 20 Reais')
if (nr10 != 0):
    print(nr10, 'Notas de 10 Reais')
if (nr5 != 0):
    print(nr5, 'Notas de 5 Reais')
if (nr2 != 0):
    print(nr2, 'Notas de 2 Reais')
if (nr1 != 0):
    print(nr1, 'Notas de 1 Reais')



