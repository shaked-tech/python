# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10,001st prime number?

def find_10001_prime():
    prime_list = [2,3]
    count = 3
    while len(prime_list) < 10001:
        count += 2
        # print("prime_list: {}".format(prime_list))
        for prime in prime_list:
            if (count % prime == 0):
                break
            if (prime == prime_list[-1]):
                prime_list = prime_list + [count]
    return prime_list[10000]

print(find_10001_prime())
