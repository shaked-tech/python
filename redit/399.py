def lettersum(string):
    sum = 0
    for letter in string:
        sum += ord(letter) - (ord('a') - 1) 
    return sum        



print(lettersum("")) # => 0
print(lettersum("a")) # => 1
print(lettersum("z")) # => 26
print(lettersum("cab")) # => 6
print(lettersum("excellent")) # => 100
print(lettersum("microspectrophotometries")) # => 317