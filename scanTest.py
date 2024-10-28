from scan import *

lista = {}
scanLan('192.168.1', [1, 151], lista, {'tents': 1})
print(lista)
input(":")