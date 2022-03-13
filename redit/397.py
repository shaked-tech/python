
# list(dict.values())[list(dict.values()).index(num)]
    
dict = { 'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }

def greek_sum(string):
    sum = 0
    for letter in string:
        sum += dict[letter]
    return sum

def numcompare(a, b):
    return(greek_sum(a) < greek_sum(b))


print(numcompare("I", "I")) #=> false
print(numcompare("I", "II")) #=> true
print(numcompare("II", "I")) #=> false
print(numcompare("V", "IIII")) #=> false
print(numcompare("MDCLXV", "MDCLXVI")) #=> true
print(numcompare("MM", "MDCCCCLXXXXVIIII")) #=> false