def main(word,parts):
    bank = parts.split(',')
    for part in bank:
        if word.startswith(part[0]):
            if (word.find(part) == 0):
                bank.remove(part)
                List = [part, word.replace(part, '', 1)]
                if List[1] in bank:
                    return List
    return []


# def solution2(word,parts):
#     bank = parts.split(',')
#     for i in range(0,len(bank)):
#         if (word.startswith(bank[i])):
#             for j in range(0,len(bank)):
#                 if i!=j and (bank[i]+bank[j]==word):
#                     return [bank[i],bank[j]]
#     return []





# print(main("hellocat", "apple,bat,cat,goodbye,hello,yellow,why"))

# print(main("onetwothrees", "three,two,ones"))
# print(main("onetwothree", "three,two,ones"))
# print(main("onetwothrees", "threes,two,one"))
# print(main("oneone", "one,two,oneq"))

print(main("manga", "nga,man,anga,ma,mang"))