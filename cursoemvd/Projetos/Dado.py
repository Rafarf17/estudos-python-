import random
tentativa = 0
dado = 0

while dado != 6:
    input('Gire o dado: ')
    dado = random.randint(1, 6)
    tentativa += 1
    if dado <= 5:
        print(f'O número que você tirou foi {dado}')

    else:
        print(f'finalmente você tirou 6, total de tentativas foi {tentativa}')

