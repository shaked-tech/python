

state = 0b1001
print("{0:4b} < state".format(state), end='\n\n')
for i in range(15):
                                                                                                     # 1001
    newbit = ((state >> 1) ^ state) & 1  # 'xor' the last two bits and get the resault (single bit)  #  100 xor
    state = (newbit << 3) | (state >> 1) # 'or' the newbit shifted three times left, making it 1000  # 1101 & 1 -> 1 (the last bit)
                                         # with the state shifted right 1 time
    # print("{0:4b}".format(newbit << 3))
    print("{0:04b} <".format(state))
    print("")

