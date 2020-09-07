""" A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers. """

mult = 9009
maiorPalimdromo = 0

string = '98788789'


def palindromo(string):
    for i in range(len(string)):
        if(string[i] == string[(i * -1)-1]):
            pass
        else:
            return False
    return True

for digit1 in range(100,999):
    for digit2 in range(100,999):
        mult = digit1 * digit2
        if(palindromo(str(mult))):
            if mult > maiorPalimdromo:
                print(digit1, digit2, maiorPalimdromo)
                maiorPalimdromo = mult

print(maiorPalimdromo)

palindromo(string)

    