#L = int(input("Coloque o valor da base do retangulo: "))
#l = int(input("Coloque o valor da altura do retangulo: "))
#resultret = (L * l)
#0print("A área do retangulo é: {} ".format(resultret))
from turtledemo.round_dance import stop

#################################################################

#num = int(input('coloque o número: '))
#print('O numero {}, tem de antecessor o {} e sucessor {}.'.format(num, num-1,num+1))

#################################################################

#num = int(input('coloque o número: '))
#print('O dobro de {} é {}'.format(num, num*2))
#print('O triplo de {} é {}'.format(num, num*3))
#print('A Raiz de {} é {}'.format(num, num**0.5))

#################################################################

#nt1 = float(input('digite a primeira nota: '))
#nt2 = float(input('digite a segunda nota: '))
#ntm = (nt1 + nt2)/2
#print('sua nota média foi: {}'.format(ntm))

#################################################################

# m = float(input('Digite a distancia em metros: '))
# km = (m /1000)
# hm = (m / 100)
# dam = m / 10
# dm = m * 10
# cm = m * 100
# mm = m * 1000
# print("""a medida de {}m corresponde a:
# {}km
# {}hm
# {}dam
# {}dm
# {}cm
# {}mm""".format(m, km, hm, dam, dm, cm, mm))

#################################################################

#preco = float(input('Qual o valor do produto? R$'))
#desc = preco -(preco/ 1 * 5/ 100)
#print('O valor de {}, recebeu desconto de 5%, com isso ficou R$ {}'.format(preco, desc))

#################################################################

#sal = float(input('Qual é o eu salário? R$'))
#aumen = sal +(sal/ 1 * 15/ 100)
#print('O funcionario ganhava R${:.2f}, mas com o aumento de 15%, ganha R${:.2f}'.format(sal, aumen))

#################################################################

#km = float(input('Quantos km você rodou com o carro?'))
#dias = float(input('Quantos dias você ficou com o carro?'))
#tot = 60 * dias + 0.15 * km
#print('O preço do veiculo alugado, ficou R${:.2f}'.format(tot))

################################################################# aula8

#import math as mt
#nm =  float(input('coloque o número: '))
#ntrunc = mt.trunc(nm)
#print(f'o Valor é {nm} e sua porção inteira é {ntrunc} ')

#################################################################

#import math
#co = float(input('Coloque o valor do Cateto Oposto: '))
#ca = float(input('Coloque o valor do Cateto Adjacente: '))
#hi = math.hypot(co, ca)
#print(f'O valor de hipotenusa é: {hi}')

#################################################################

#from  math import sin, cos, tan, radians
#gr =  float(input('Coloque o angulo: '))
#s = sin(radians(gr))
#print(f'O valor de {gr}, tem o seno de {s}')
#c = cos(radians(gr))
#print(f'O valor de {gr}, tem o cosseno de {c}')
#t = tan(radians(gr))
#print(f'O valor de {gr}, tem a tangente de {t}')

#################################################################

#import random as rd
#n1 =  str(input('Coloque o nome: '))
#n2 =  str(input('Coloque o nome: '))
#n3 =  str(input('Coloque o nome: '))
#n4 =  str(input('Coloque o nome: '))
#lista = [n1, n2, n3, n4]
#res = rd.choice (lista)
#print(f'O escolhido foi: {res}')

################################################################# aula9

# nome = str(input('Digite o nome inteiro: '))
# nmg = nome.upper()
# nmp = nome.lower()
# quantlt = len(nome)
# prinm = nome.split()
# print("{}".format(nmg))
# print("{}".format(nmp))
# print("{}".format(quantlt))
# print(prinm[0])

#################################################################

# num = int(input('Digite um número: '))
# uni = num % 10
# dez = (num // 10) % 10
# cnt = (num // 100) % 10
# mil = (num // 1000) % 10
# print(f"""unidade: {uni}
# dezena: {dez}
# centena: {cnt}
# centena: {mil} """)

#################################################################

# nome = str(input('Qual a sua cidade? '))
# print(nome[:5].upper() == 'SANTO')

################################################################# primeiro e ultimo nome

# n = str(input('Digite seu nome: ')).strip()
# nome = n.split()
# print(nome[0])
# print(nome[len(nome)-1])

################################################################# aula 10

# from random import randint
# from time import sleep
# computador = randint(0, 5)
#
# print("Vou pensar em um número, tente adivinhar...")
# n = int(input('Qual o número? '))
#
# print('processando...')
# sleep(2)
# if n == computador :
#     print(f'Você venceu, o numero é o {computador}')
# else:
#     print(f'Você perdeu! O num é {computador}')

#################################################################

# v = float(input('Qual a velocidade atual do seu carro? '))
# if v <= 80:
#     print('Sua velocidade está ok!')
# else:
#     limite = (v-80) * 7
#     print(f"""Você excedeu o limite de 80km, multa de R${limite:.2f}.
#Tenha um bom dia!""")

#################################################################

# n = int(input('Digite qualquer número: '))
# cnt = n %2
# if cnt == 0:
#     print('O número é par!')
# else:
#     print('O número é impar!')

#################################################################

# km = int(input('Digite a distância da sua viagem: '))
# if km <= 199:
#     preco = km * 0.50
#     print(f'O preço da viagem ficou R${preco:,.2f}')
# else:
#     preco = km * 0.45
#     print(f'O preço da viagem ficou R${preco:.2f}')

#################################################################

# ano = int(input('Digite o ano: '))
# bi = ano % 4
# if bi == 0:
#     print('O ano é bissexto')
# else:
#     print('O ano não é bissexto')

#################################################################

# s = int(input("Qual é o salário do funcionário? R$"))
# sn1 = s * 15/100 + s
# sn2 = s * 10/100 + s
# if s <= 1500:
#     print(f'Seu salário de R${s:.2f} ganhou um almento de 15%, ficando R${sn1:.2f}.')
# else:
#     print(f'Seu salário de R${s:.2f} ganhou um almento de 10%, ficando R${sn2:.2f}.')

#################################################################

# r1 = float(input('primeira reta: '))
# r2 = float(input('Segunda reta: '))
# r3 = float(input('Terceira reta: '))
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
#     print('faz triangulo')
# else:
#     print('Não faz triangulo')

#################################################################