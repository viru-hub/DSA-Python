s = "words and 987"

def str2int(s):
    s = s.strip()
    Ml_factor = int
    val = ''

    if s.startswith('-'):
        Ml_factor = -1
        s = s[1:]
    elif s.startswith('+'):
        Ml_factor = +1
        s = s[1:]
    else:
        Ml_factor = +1

    for i in s:
        try:
            i = str(int(i))
            val += i
        except:
            break
    if val:
        val = int(val)*Ml_factor
        val = -2**31 if val < -2**31 else val
        val = 2**31 - 1 if val > 2**31 - 1 else val
    else :
        val = 0
    return val

