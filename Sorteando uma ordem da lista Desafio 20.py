import random
n1 = str(input('Digite o Primeiro Nome: '))
n2 = str(input('Digite o Segundo Nome: '))
n3 = str(input('Digite o Terceiro nome:'))
n4 = str(input('Digite o Quarto Nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(lista)
#Random.shuffle sorteia em ordem aleatoria, random.choice escolhe 1 da lista
#Declarei a variavel string pra deixar claro o tipo (fixação)
#Se usar from random import shuffle, posso tirar o random. e usar apenas shuffle