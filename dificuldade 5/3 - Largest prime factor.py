""" The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ? """

numero = 600851475143

maxFator = 0


def divide(num):
    divisor = 2
    global maxFator

    while (num % divisor != 0):
        divisor+=1

        if (divisor > maxFator):
            maxFator = divisor

    resultado = num / divisor
    return resultado

while (numero > 2):
    numero = divide(numero)
    print(numero)

print("max: ",maxFator)