from random import randint
import os
from time import sleep
os.system('cls')
print("="*25)
print("Seja bem vindo ao pedra papel tesoura")
print("="*25)
itens = ("Pedra","Papel","Tesoura")
computador = randint(0, 2)
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA """)
jogador = int(input("Qual é sua jogada? "))
print("JO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO")
sleep(0.5)
print("="*25)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print("=" * 25)

if computador == 0: #PEDRA
    if jogador == 0:
        print("EMPATE")
    elif jogador == 1:
        print("JOGADOR VENCE")
    elif jogador ==2:
        print("COMPUTADOR VENCE")
    else:
        print("JOGADA INVALIDA")
elif computador == 1: #PAPEL
    if jogador == 0:
        print("COMPUTADOR VENCE")
    elif jogador == 1:
        print("EMPATE")
    elif jogador == 2:
        print("JOGADOR VENCE")
    else:
        print("Jogada invalida")

elif computador == 2: #TESOURA
    if jogador == 0:
        print("JOGADOR VENCE")
    elif jogador == 1:
        print("COMPUTADOR VENCE")
    elif jogador == 2:
        print("EMPATE")
    else:
        print("Jogada invalida")