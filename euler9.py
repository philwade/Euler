"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

base = 1000
c = base / 3

for c in range(base, 0, -1):
    for b in range(c - 1, 0, -1):
        for a in range(b - 1, 0, -1):
            if a**2 + b**2 == c**2:
                if a + b + c == base:
                    print a, b, c, a*b*c
                    break
