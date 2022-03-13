import re

def clean_string(str):
  # regex='![A-Z|a-z]'

  regex='[,|.|;|:|\'|"|(|)|}]'
  non_word_regex=r"[,.;:\'\"(){}\\/]" # \\ as part of the regex does not remove the \ in string
  # str=str.replace("\\"," ")
  str=re.sub(regex, r" ", str)  
  return str

def main(sentence):
  new_sentence=clean_string(sentence)
  longest=""
  for word in new_sentence.split():
    if len(word) > len(longest):
      longest = word
  return longest

print(main("              single "))
print(main("Hello world"))
print(main("short loooong"))
print(main("hello\world"))
