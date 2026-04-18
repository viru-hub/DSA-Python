#https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/1805970053/

def manipulator(str1, str2):
    out = []
    for i in str1:
        c = 0
        while c < len(str2):
            out.append(i+str2[c])
            c+=1
    return out

def letterCombinations(num, manipulator = manipulator):
    mapping = {'2': ['a','b', 'c'],
    '3': ['d','e','f'],
    '4':['g','h','i'],
    '5':['j','k','l'],
    '6':['m','n','o'],
    '7':['p','q','r','s'],
    '8':['t','u','v'],
    '9':['w','x','y','z']}

    num = 24
    num = str(num)
    strings = []
    out = []
    for i in range(0,len(num)):
        i = num[i]
        if i in mapping: 
            #print('True')
            strings.append(mapping[i])
        else:
            None

    for i in range(0,len(strings)-1):
        #print(i)
        out = manipulator(str1= strings[0], str2= strings[1])
        str1 = strings[0].copy()
        str2 = strings[1].copy()
        strings.remove(str1)
        strings.remove(str2)
        strings.insert(0,out)

    return strings[0]


