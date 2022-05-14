def main(str):
  back=""
  for l in str[-1::-1]:
    back="".join([back,l])
  return back

print(main("test HI my MAN"))
print(main(""))
print(main("1234 56789"))
if main("Hello World and Coders") == "sredoC dna dlroW olleH":
  print("works")