#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import math
import sys
primes = [2, 3]
try:
    target = int(sys.argv[1])
except IndexError:
    target = 600851475143 

def is_prime(num):
    if num in primes:
        return True
    start = 2
    end = int(math.ceil(math.sqrt(num)))

    for n in range(start, end):
        if num % n == 0:
            return False

    primes.append(num)
    return True

def get_next_prime():
    start = max(primes)
    start += 1
    while not is_prime(start):
        start += 1

    primes.append(start)
    return start

def factor(num):
    if(is_prime(num)):
        return num
    for n in primes:
        if num % n == 0:
            return n, factor(num / n)

    while True:
        n = get_next_prime()
        if num % n == 0:
            return n, factor(num / n)

print factor(target)
