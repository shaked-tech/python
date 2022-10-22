# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

def compute():
    prime_list = [2,3]
    a = 3
    sum = 0
    while True:
        a += 2
        for prime in prime_list:
            if (a % prime == 0):
                break
            if prime == prime_list[-1]:
                if a > 2000000:
                    return sum + 5
                prime_list += [a]     
                sum += a

print((compute()))
