# Coding: utf-8

#Esta calculadora tem por objetivo calcular o salário liquido.

bruto = float(input('Qual o seu salário bruto?'))
inss = float(0)
dependentes = int(input('Quantos dependentes você possui ?'))
descdep = dependentes * 189.59
irrpf = 0
imposto = 0

print('Salário Bruto: R$ ',bruto)

msal = bruto

if(msal <= 1659.39):
    inss = (msal * 0.08)
    print('Desconto INSS: R$ ', inss)
elif(msal > 1659.39 and msal <= 2765.66):
    inss = (msal * 0.09)
    print('Desconto INSS: R$ ', inss)
elif(msal >2765.66 and msal <= 5531.31):
    inss = (msal * 0.11)
    print('Desconto INSS: R$ ', inss)
elif(msal> 5531.31):
    inss = 608.44
    print('Desconto INSS: R$ ', inss)

fsal = msal - inss - descdep

if(fsal > 1903.98 and fsal <= 2826.65):
    irrpf = fsal * 0.075
    imposto = irrpf - 142.8
elif(fsal > 2826.65 and fsal <= 3751.05):
    irrpf = fsal * 0.15
    imposto = irrpf - 354.8
elif(fsal > 3751.05 and fsal <= 4664.68):
    irrpf = fsal * 0.225
    imposto = irrpf - 636.13
elif(fsal > 4664.68):
    irrpf = fsal * 0.275
    imposto = irrpf - 869.36

print('Desconto IRRPF: R$ ', imposto)


liquid = bruto - inss - imposto
print('O salário liquido é: R$ ', liquid)






