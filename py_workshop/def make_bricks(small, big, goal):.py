def make_bricks(small, big, goal):
  if (goal % 5 == 0):
    if (5 * big >= goal) or (5 * big + small >= goal):
      return True
  else:
    if (big * 5 > goal):
      # smallest_big = ((big * 5 - goal) // 5) + 1
      smallest_big = goal // 5
      print(f"{smallest_big * 5}")
      if (smallest_big * 5 + small >= goal):
        return True
    else:
      if (big * 5 + small >= goal):
        return True
  
  return False


# (4, 5, 6)
# 25 ; 6 = 1

# (4, 5, 18)
# 20 ; 28 = 





print(make_bricks(2, 1000000, 100003))