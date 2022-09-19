import hashlib
import sys

string_to_work = str(sys.argv[1])
# max_iter = int(sys.argv[2])
print("string: " + string_to_work)
# print("iterations: " + str(max_iter))
print("start")

min_diff = float('inf')
min_hash = ""
final_nonce = 0
nonce = 0

#TODO: terminar de maquetear los siguientes TODOs y despues empezar a optimizarlo. (usar rust? go?)

#TODO: la idea es hacerlo con un algoritmo de hashing mas hippie, que no escale ni con GPUs ni asics. RandomX? - para que sea mas o menos igual de costoso para cualquiera. No que puedan mandar el request a una nave de google y este en 1ms.

while True:
    string_with_nonce = string_to_work + " " + str(nonce)
    hashed = hashlib.sha256(string_with_nonce.encode('utf-8')).hexdigest()
    # if i % 1000:
        # print("\t" + str((i * 100) / max_iter) + "%", end='\r')

    #TODO: Implementar una dificultad opcional dada por input, que si sale con esa, breakea el loop y ya te devuelve tu string con nonce y su hash.
    if int(hashed, 16) < int("00000000ffffffffffffffffffffffffffffffffffffffffffffffffffffffff", 16):
        min_diff = int(hashed, 16)
        print(string_with_nonce)
        print(hashed)
        min_hash = hashed
        final_nonce = nonce
        best_hash = string_with_nonce
        break

    nonce += 1

print(best_hash)
print(min_hash)


