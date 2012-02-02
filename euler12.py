import math
"""
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""
def divisors(n):
    factor_list = [1, n]
    square = math.ceil(math.sqrt(n)) + 1
    for i in range(2, square):
        if n % i == 0:
            factor_list.append(i)
            factor_list.append(n/i)
    return len(set(factor_list))

n = 1
t = 1
j = 0

while(True):
    n += 1
    t = t + n
    j = divisors(t)
    print j
    if(j > 500):
        break

print t

    