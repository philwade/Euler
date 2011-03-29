#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10001st prime number?
start = 3
count = 2
import math

def is_prime(num):
    start = 2
    end = int(math.ceil(math.sqrt(num)))

    for n in range(start, end + 1):
        if num % n == 0:
            return False

    return True

while count < 10001:
    start += 2
    if is_prime(start):
        count += 1

print start
