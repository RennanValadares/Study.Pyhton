#coding: Utf-8

den = 2
num = int(input("Escolha um número decimal para transformar em binário."))

p = "PAR"
i = "IMPAR"
result = '=)'
var = p if num % 2 == 0 else i

while(num>=1):
    var = p if num % 2 == 0 else i
    if (var == p):
        num = int((num/den))
        result = (0, result)
    if (var == i):
        num = int((num/den))
        result = 1, result

print(result)

