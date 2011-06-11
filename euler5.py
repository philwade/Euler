#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def allDivisible(n):
   for i in range(1, 21): 
        if n % i != 0:
            return False

   return True

loop = True
start = 2520

while start % 20 != 0:
    start += 1
    
while loop:
    if allDivisible(start): 
        print start
        loop = False
    else:
        start += 20
    
