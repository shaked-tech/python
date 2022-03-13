
def solution(S, C):
    S = (S.split(", "))
    # List = ""
    # count = 0
    first_last_name = []
    for name in S:
        name = name.split(" ")
        first_last_name.append(".".join(name[::len(name)-1]).lower().replace("-", ""))
    # print(first_last_name)
    
    my_dict = {i:first_last_name.count(i) for i in first_last_name}
    print(first_last_name)

    print(my_dict)

    c = len(first_last_name) - 1 
    for name in reversed(first_last_name):
        if my_dict[name] > 1:
            first_last_name[c] = S[c] + " <" + name + str(my_dict[name]) + "@{}.com>".format(C) 
            my_dict[name] = my_dict[name] - 1
        else:
            first_last_name[c] = S[c] + " <" + name + "@{}.com>".format(C) 

        print(name)
        c -= 1
    first_last_name = ", ".join(first_last_name)
    return first_last_name + "."


S = "John Doe, Peter Benjamin Parker, Mary Jane Watson-Parker, John Elvis Doe, John Evan Doe, Jane Doe, Peter Brian Parker"
C = "example"


Email_list = solution(S, C)
print(Email_list)