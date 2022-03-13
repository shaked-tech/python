import re

def main(logfile_path):
  RE = '()'
  data = {}
  with open(logfile_path) as f:
    lines = f.readlines()
    for line in lines:
      bank = line.split(' ')
      if bank[8] in data:
        data[bank[8]] += 1
      else:
        data[bank[8]] = 1
  
  ret = list(data.items())
  ret.sort
  return ret
  

print(main("/home/develeap/Desktop/example-projects/py_workshop/12/example.log"))