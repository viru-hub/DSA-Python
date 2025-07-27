#https://leetcode.com/problems/integer-to-roman/

I = 1
II = 2
III = 3
IV = 4
V = 5
VI = 6
VII = 7
VIII = 8
IX = 9
X = 10
L = 50
C = 100
D = 500
M = 1000


def Roman(num):
    out = []
    symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    values =  [1,    5,   10,  50,  100, 500, 1000]

    counts = num//values[6]
    out.append(symbols[6]*counts)

    for i in [6,4,2]:
        num = num%values[i]
        prop = num/values[i-1]

        if prop >= 1:
            counts = num%values[i-1]
            counts = int(counts/values[i-2])
            if counts <=3:
                out.append(symbols[i-1]+symbols[i-2]*counts)
            else:
                out.append(symbols[i-2]+symbols[i])
        else:
            counts = num//values[i-2]
            if counts <=3:
                out.append(symbols[i-2]*counts)
            else:
                out.append(symbols[i-2]+symbols[i-1])
    return ''.join(out)


num = 49
Roman(num = num)







out = []
symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
values =  [1,    5,   10,  50,  100, 500, 1000]

counts = num//values[6]
out.append(symbols[6]*counts)

num = num%values[6]
prop = num/values[5]
prop
if prop > 1:
    counts = num%values[5]
    counts = int(counts/values[4])
    if counts <=3:
        out.append(symbols[5]+symbols[4]*counts)
    else:
        out.append(symbols[4]+symbols[6])
else:
    counts = num//values[4]
    if counts <=3:
        out.append(symbols[4]*counts)
    else:
        out.append(symbols[4]+symbols[5])


num = num%values[4]
prop = num/values[3]
prop
if prop > 1:
    counts = num%values[3]
    counts = int(counts/values[2])
    if counts <=3:
        out.append(symbols[3]+symbols[2]*counts)
    else:
        out.append(symbols[2]+symbols[4])
else:
    counts = num//values[2]
    if counts <=3:
        out.append(symbols[2]*counts)
    else:
        out.append(symbols[2]+symbols[3])

num = num%values[2]
prop = num/values[1]
prop
if prop > 1:
    counts = num%values[1]
    counts = int(counts/values[0])
    if counts <=3:
        out.append(symbols[1]+symbols[0]*counts)
    else:
        out.append(symbols[0]+symbols[2])
else:
    counts = num//values[0]
    if counts <=3:
        out.append(symbols[0]*counts)
    else:
        out.append(symbols[0]+symbols[1])


''.join(out)