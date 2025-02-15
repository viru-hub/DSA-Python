import random
import math

def rand7():
    return random.randint(1,7)

vals = []
for i in range(1,8):
    for j in range(1,8):
        vals.append(i*j)

vals = sorted(vals)
vals

def rand10():
    vals = ''
    while vals  not in [2,3,5,7,8,10,14,15,18,20]:
        vals = rand7()*rand7()

    if vals == 2:
        val = 1
    elif vals == 3:
        val = 2
    elif vals == 5:
        val = 3
    elif vals == 7:
        val = 4
    elif vals == 8:
        val = 5
    elif vals == 10:
        val = 6
    elif vals == 14:
        val = 7
    elif vals == 15:
        val = 8
    elif vals == 18:
        val = 9
    elif vals == 20:
        val = 10
    return val


rand10()