# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a2 + b2 = c2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc (a*b*c).

from math import sqrt

def compute():
    a = 0
    while True:
        a += 1
        b = a
        while b < 499:
            b += 1
            # print("{},{}".format(a,b))
            # print("{} {} = {}".format(a**2,b**2,a**2+b**2))
            c = sqrt((a**2+b**2))
            if c % 1 == 0:
                if (a+b+c == 1000):
                    return (a*b*c)
                    # print("{} {} {} = {}".format(a,b,c,a+b+c))

print(compute())