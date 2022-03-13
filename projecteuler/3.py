# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from cmath import sqrt


def find_prime(num):
    check_list = [2,3]
    for n in range(3,num+1):
        print(n)
        for check in check_list:
            print("check: {}".format(check))
            if (n % check == 0):
                break
            if (check == check_list[-1]):
                # if (check not in check_list):
                check_list = check_list + [n]
    return check_list

# print(find_prime(13195))

def find_prime_factors(num):
    prime_factors_list = []
        # print(num)
    while (num % 2 == 0):
        num /= 2
        print(num)
        prime_factors_list += [2]

    
    for i in range(3,round(sqrt(num).real),2):
        if (num % i == 0):
            num /= i
            print(num)
            prime_factors_list += [i]
            continue
    return prime_factors_list

# print(find_prime_factors(13195))
print(find_prime_factors(600851475143))
