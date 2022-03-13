# The sum of the squares of the first ten natural numbers is
# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

def sol():
    s1 = 0
    s2 = 0
    for i in range(1,101):
        s1 += i**2
        s2 += i

    return(s2**2 - s1)

print(sol())