#coding: utf-8
lata = 108
galao = float(21.6)
plata = 80
pgalao = 25
metro = float(input('Quantos metros quadrados deseja pintar ?'))
resto = (metro / galao) - int(metro / galao)

if((metro % lata)) == 0:
    onlyl = metro / lata
    preço1 = onlyl * plata
    print('Comprando Latas você precisara de: ', onlyl, 'latas e pagará ', preço1, 'Reais.')

if(resto == 0):
    onlyg = metro / galao
    preço2 = onlyg * pgalao
    print('Comprando Galões voce precisará de: ', onlyg, 'galões e pagará ', preço2, 'Reais.')
if((metro % lata ) != 0):
    onlyl = (int(metro / lata) +1)
    precol = onlyl * plata
    print('Se comprar Somente Latas terá que comprar: ', onlyl, 'Unidades e gastará', precol, 'Reais.')

if(resto != 0):
    onlyg = (int(metro / galao) +1)
    preco2 = onlyg * pgalao
    print('Se comprar Somente Galões terá que comprar: ', onlyg, 'Unidades e gastará', preco2, 'Reais.')
if((metro > 108) and (metro % lata) % galao) != 0 :
    qtlata = int(metro / lata)
    qtgalao = int((metro % lata) / galao) + 1
    preço3 = qtlata * plata
    preço4 = qtgalao * pgalao
    preço5 = preço4 + preço3
    print('Você precisará comprar: ', qtlata, 'latas e', qtgalao, 'galões e o preço ficará: ', preço5, 'Reais.')
