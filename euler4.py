#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(n):
    n = str(n)
    if len(n) == 1 or n == '': 
        return True

    if n[0] == n[-1]:
        return isPalindrome(n[1:-1])
    else:
        return False

top = 0

for n in range(999, 99, -1):
    for m in range(999, 99, -1):
        if isPalindrome(n * m):
            tmp = n * m
            if tmp > top:
                print n, m
                print n * m
                top = tmp

print top
