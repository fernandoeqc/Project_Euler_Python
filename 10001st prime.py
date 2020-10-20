""" By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number? """

import time

t = time.time()


def primo(numero):
    dividendo = numero
    
    for div in range(2, numero, 1):
        if (dividendo % div) == 0:
            return False

    return True


lista = []
numeracao = 2
contagem = 0


while contagem != 10001:
    if (primo(numeracao)) is True:
        lista.append(numeracao)
        print(numeracao, contagem)
        contagem += 1
    numeracao += 1

print("fim")

print(time.time() - t)
""" 82.43018507957458 s """