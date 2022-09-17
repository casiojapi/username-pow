import hashlib
import sys

string_to_work = str(input("input the string you want to pow: "))
# diff = int(input("input the difficulty you want: "))
max_iter = int(input("input the amount of iterations you want to do: "))
# min_diff = float('inf')
# min_hash = ""
nonce = 0

#TODO: terminar de maquetear los siguientes TODOs y despues empezar a optimizarlo. (usar rust? go?)

#TODO: la idea es hacerlo con un algoritmo de hashing mas hippie, que no escale ni con GPUs ni asics. RandomX? - para que sea mas o menos igual de costoso para cualquiera. No que puedan mandar el request a una nave de google y este en 1ms.

for i in range(max_iter):
    string_with_nonce = string_to_work + " " + str(nonce)
    hashed = hashlib.sha256(string_with_nonce.encode('utf-8')).hexdigest()
    if i % 1000:
        print("\t" + str((i * 100) / max_iter) + "%", end='\r')
    
    #TODO: no tener hardcodeada la diff, si no que dadas las max iteraciones, encontrar el hash con menor valor numerico.

    #TODO: Implementar una dificultad opcional dada por input, que si sale con esa, breakea el loop y ya te devuelve tu string con nonce y su hash.
    if hashed[:6] == "000000":
        print("\t" + str((i * 100) / max_iter) + "%")
        min_hash = hashed
        break


    nonce += 1

print(string_with_nonce)
print(min_hash)
 