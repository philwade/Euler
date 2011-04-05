"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
start = 3
sum = 2
import math

def is_prime(num):
    start = 2
    end = int(math.ceil(math.sqrt(num)))

    for n in range(start, end + 1):
        if num % n == 0:
            return False

    return True

while start < 2000000:
    if is_prime(start):
        sum += start
    start += 2

print sum
