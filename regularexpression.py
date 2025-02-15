import re

txt = 'ab'
pattern = '.*c'

re.search(pattern, txt)

def isMatch(s: str, p: str) -> bool:
    if len(s)>=1 and len(s)<= 20 and len(p)>= 1 and len(p)<= 20:
        res = re.search(p, s)
        if res:
            return True if res[0] == s else False
        else:
            return False
    else:
        False

isMatch(s= txt, p= pattern)

