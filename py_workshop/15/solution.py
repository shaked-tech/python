def main(str):
    rtn = ""
    count = 0
    for letter in range(len(str)):
        rtn = rtn + str[letter].upper()
        for i in range(count):
          rtn = rtn + str[letter].lower()
        rtn = rtn + '-'
        count += 1
    return rtn[:-1]

# def solution(str):
#   ret=""
#   l=0
#   for c in str:
#     if l>0: ret+="-"
#     l+=1
#     for i in range(0,l):
#       ret+=(c.upper() if i==0 else c.lower())
#   return ret

main("RqaEzty") 