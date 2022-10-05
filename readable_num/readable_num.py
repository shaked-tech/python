
def readable_num(num):
    num = str(num)
    N = 3
    L = len(num)
    # List = [ [num[i:i+N]] for i in range(0,len(num),N) ]
    List = [ [num[-i-N:L-i]] for i in range(0,len(num),N) ]

    Res = ""
    print("List:", List)
    for x in range(len(List)):
        Res += List[len(List)-x-1][0] + ","
    return Res[:-1]

print(readable_num(12345676576532658388))