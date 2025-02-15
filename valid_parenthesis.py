  

import re
s = "(()())((((((((((((((((()))))))))))))))))"

#s1 = s.replace('()', 'A')
#s1 = s1.replace('(A)', 'AA')

if len(s)> 1:
    start = '('
    between = ''
    end = ')'
    R_char = 'A'
    for i in range(len(s)):    
        if i>=1:
            between += 'A'
            R_char += 'A'

        r_char = start+between+end

        s = s.replace(r_char, R_char)

    res = re.split(r'[)(]+', s)
    res = max(res, key= len)
    res = len(res)*2
    print(res)
else:
    res = 0
    print(res)

s

count = len(s)//2 if len(s)<20 else len(s)//4
count

len(s)//4