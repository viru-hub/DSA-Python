#https://leetcode.com/problems/longest-common-prefix/submissions/1602013028/
strs = ["filower","flow","flight"]


def prefix(strs):
    if len(strs)>0:
        short = min(strs, key= len)
        short
        out = ['no']
        while 'no' in out:
            out = []
            for i in range(len(strs)):
                if short in strs[i] and strs[i].startswith(short) :
                    out.append('yes')
                else:
                    out.append('no')
            short = short[:-1] if 'no' in out else short
    else:
        short = ''
    return short


prefix(strs=strs)