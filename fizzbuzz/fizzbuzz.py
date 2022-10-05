
import itertools as its
import time

def itertool_fizzbuzz(n):
    fizzes = its.cycle([""] * 2 + ["Fizz"])
    buzzes = its.cycle([""] * 4 + ["Buzz"])
    fizzes_buzzes = (fizz + buzz for fizz, buzz in zip(fizzes, buzzes))
    result = (word or n for word, n in zip(fizzes_buzzes, its.count(1)))
    for i in its.islice(result, 100):
        print(i)

def one_print_fizzbuzz(n):
    result = ""
    for i in range(1, n+1):
        if (i % 3) == 0:
            if (i % 5) == 0:
                result += "fizzbuzz\n"
            else: result += "fizz\n"
        elif (i % 5) == 0:
            result += "buzz\n"
        else: result += str(i) + "\n"
    print(result)

def main5(start,stop):
    fizzbuzz = ''
    for i in range(start,stop):
        if (i%3) == 0:
            if (i%5) == 0:
                fizzbuzz += 'FizzBuzz\n'
        else:
            fizzbuzz += 'Fizz\n'
    else:
        if (i%5) == 0:
            fizzbuzz += 'Buzz\n'
        else:
            fizzbuzz += str(i) + "\n"
    print(fizzbuzz)

  
def if_else_fizzbuzz(n):
    for i in range(1, n+1):
        if not (i % 15):
            print("fizzbuzz")
        elif not (i % 3):
            print("fizz")
        elif not (i % 5):
            print("buzz")
        else:
            print(i)


if __name__ == "__main__":
    N = 3000000
    # is_else_fizzbuzz(N)
    # itertool_fizzbuzz(N)
    start = time.time()
    one_print_fizzbuzz(N)
    end = time.time()
    print("Function took: " + str((end-start)) + " Sec. to go through " + str(N))