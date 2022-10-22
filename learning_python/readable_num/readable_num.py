global N; N = 3

# 123   --> 123
# 1234  --> 1,234
# 12345 --> 12,345

def readable_num_1(num):
    num = str(num)
    length = len(num)
    res = ''

    sub_tuple = (num[-i-N:length-i] for i in range(0,len(num),N))
    for sub in sub_tuple:
        res = f"{sub},{res}"
    return res[:-1]


def readable_num_2(num):
    num = str(num)
    res = ''

    for i in range(0,len(num),N):
        res = num[-i-N:len(num)-i] + ',' + res
    return res[:-1]


print(readable_num_2(123))
print(readable_num_2(12345))
print(readable_num_2(123456))
print(readable_num_2(1234567))