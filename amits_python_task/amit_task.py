


def multi_name_fix(name):
    # print(name[-1])
    if name[-1].isdigit():
        print(name + "has number" )
    else: 
        name = name + '2'
        # print(name)
    return name


def solution(S, C):
    S = (S.split(", "))
    List = ""
    count = 0
    name_list = []
    for name in S:
        # print(S)
        # print(name)
        subname = name.split(" ")
        first_last_name = ".".join(subname[::len(subname)-1]).lower()

        if first_last_name not in name_list:
            name_list.append(first_last_name)
            # print(same_name_list)
        #     print(same_name_list)
        # else:
        #     same_name_list = [n.replace(first_last_name, multi_name_fix(first_last_name)) for n in same_name_list]
        #     print("first_last_name " + first_last_name)
        #     print("multi_name_fix " + multi_name_fix(first_last_name))
        #     print(same_name_list)
        #     first_last_name = multi_name_fix(first_last_name)

        count += 1 
        List += name + " <" + first_last_name + "@{}.com>".format(C)
        if (len(S) != count):
            List += ", "
        else:
            List += "."    
    # print(name_list)  
    # for name in name_list:
    #     count = 1
    #     check_list = List.split(" ")
    #     for part in check_list:
    #         # print(part)
    #         if name in part:
    #             # print(name)
    #             # print(part)
    #             count = count + 1
    #             part = part.replace(name, name+str(count))
    #             print(part)

                # print(count)

    check_list = List.split(" ")
    for name in name_list:
        count = 0
        print(name)
        print(check_list)
        if check_list:
            count += 1
            List = List.replace(name, name+str(count))
            print(List)

    return List





S = "John Doe, Peter Benjamin Parker, Mary Jane Watson-Parker, John Elvis Doe, John Evan Doe, Jane Doe, Peter Brian Parker"
C = "example"


Email_list = solution(S, C)
print(Email_list)