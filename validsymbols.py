#https://leetcode.com/problems/valid-parentheses/submissions/1807406734/

s = "{()}"

def validator (s):
    T = len(s)
    V= 0
    if T == 2 and s in ['[]','()','{}']:
        s = ''
    elif T > 2:
        while V < T and T > 2:
            T = V if V>0 else T
            if len(s)==2 and s in ['[]','()','{}']:
                s = ''
            elif len(s)>2:
                for i in range(1, (len(s))):
                    if s[i-1]+s[i] in  ['[]','()','{}'] and i>1:
                        s = s[:i-1]+s[1+i:]
                        print(s)
                        break
            V = len(s)
    elif T <2:
        s = s
    return True if s == '' else False


validator(s=s)
