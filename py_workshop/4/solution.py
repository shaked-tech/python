def main(str):
  new_str = ""
  # i=0
  upper = True
  # while (i < len(str)):
  for c in str:
    if upper: new_str = new_str + c.upper()
    else: new_str = new_str + c.lower()

    # if (str[i] == "," or str[i] == "." or str[i] == ";" or str[i] == " "):
    #   upper = True
    # else:
    #   upper = False
    # i += 1
    upper = (c in ",.; ")
  return new_str

print(main("I don't like this excercise"))
print(main("i don't li(ke this exc)ercise,this     i"))

