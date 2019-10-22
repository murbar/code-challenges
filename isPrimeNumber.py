import math


def isPrime(number):
    boundary = math.floor(math.sqrt(number))
    for i in range(2, boundary+1):
        if number % i == 0:
            return False

    return number >= 2


print(isPrime(3))
print(isPrime(7))
print(isPrime(9))
print(isPrime(435375373415465733))
