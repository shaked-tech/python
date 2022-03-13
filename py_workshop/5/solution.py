def main(seconds):
  sgn = ''
  if seconds < 0:
    seconds *= -1
    sgn = '-'

  fin_hours = seconds // (60*60)
  m = (seconds - fin_hours*3600) // 60
  s = seconds % 60
  
  return f"{sgn}{fin_hours}:{m:02}:{s:02}"


  # return f"{fin_hours}:{fin_minutes:02d}:{fin_seconds:02d}"


print(main(50)) # 0:00:50
print(main(60)) # 0:01:00
print(main(-3600)) # 1:00:00
print(main(-3723)) # 1:02:03

print(main(-50)) # 0:00:-50


# 1 min = 60 Sec
# 1 h = 60 min = 3600 sec 