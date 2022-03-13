import time
import datetime

j=0
date = datetime.datetime.now()
date_formated = date.strftime("%H:%M:%S_%d-%m-%Y")

f = open(f"./percentage_list_{date_formated}.txt", 'a')

START = time.time()

while (j<10000):
    START1 = time.time()
    L1 = []
    for i in range (1, 1000):
        if i%3 == 0:
            L1.append (i)
    TIME1 = time.time() - START1 

    START2 = time.time()
    L2 = [i for i in range (1, 1000) if i%3 == 0]
    TIME2 = time.time() - START2

    # print( f"TIME1 = {TIME1:.9f} (sec) \nTIME2 = {TIME2:.9f} (sec) ")

    percent = (TIME1/TIME2)*100-100

    if (percent > 0):
        f.write(f"L2 was {round(percent)}% faster than L1\n")
    else:
        f.write(f"L2 was {round(percent)}% slower than L1\n")
    j+=1

f.close()


STOP = (time.time() - START)
print(f"wrote {j} lines to file, took {round(STOP, 5)} seconds")

# ex. if t1 took is smaller then t2 (t1 took less time then t2) then following the calculation below we will get the percentige of t1 compared to t2 (t1/t2). 
# T1/T2
# 35/70 * 100 - 100
