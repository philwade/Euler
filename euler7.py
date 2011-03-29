#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?
primes = [2, 3]
import math

def is_prime(num):
    start = 2
    end = int(math.ceil(math.sqrt(num)))

    for n in range(start, end + 1):
        if num % n == 0:
            return False

    primes.append(num)
    return True

def get_next_prime():
    start = max(primes)
    start += 2
    while not is_prime(start):
        start += 2

    return start

while len(primes) < 10001:
    next = get_next_prime()

print next, len(primes)
    

