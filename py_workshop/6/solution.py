def main(bigstr,smallstr):
  for char in smallstr:
    # print(char)
    if (bigstr.find(char) != -1):
      bigstr = bigstr.replace(char, "", 1)
    else:
      return False
  return True

print(main("nomad","and"))
print(main("to do is to be","dodo"))
