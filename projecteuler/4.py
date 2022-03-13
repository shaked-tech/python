# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindromic(pal):
    mid = len(pal)//2
    for i in range(mid):
        # print("{}, {}".format(pal[i], pal[-(i+1)]))
        if (pal[i] != pal[-(i+1)]):
            return False
    return True

def find_palindromic(length):
    num = 1
    j = 0 
    ret = 0
    while len(str(num)) <= length:
        num *= 10
    num -= 1
    while num-j >= 10**(length-1):
        i = 0
        while num-i-j >= 10**(length-1):
            sum = (num-j) * (num-i-j)
            # print("{} * {} = {}".format(num-j,num-i-j,sum))
            if (is_palindromic(str(sum))):
                if (sum > ret):
                    ret = sum
            i += 1
        j += 1
    return ret


# def sol():
# 	ans = max(i * j
# 		for i in range(100, 1000)
# 		for j in range(100, 1000)
# 		if str(i * j) == str(i * j)[ : : -1])
# 	return str(ans)   


print(find_palindromic(3))
