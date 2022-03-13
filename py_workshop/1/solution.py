def main(a,b,c):
  try:
    return (a+b)/c
  except:
    return "err"

print(main(2,3,4))
print(main(2,3,0))