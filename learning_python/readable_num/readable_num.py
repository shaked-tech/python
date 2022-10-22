global N; N = 3

def readable_num(num):
    num = str(num)
    length = len(num)
    Res = ""
    # List = [ [num[i:i+N]] for i in range(0,len(num),N) ]

    sub_list = [ [num[-i-N:length-i]] for i in range(0,len(num),N) ]

    print(','.join(sub_list))
    # for sub in List:
        # Res += List[len(List)-x-1][0] + ","
    return Res[:-1]

print(readable_num(12345676576532658388))