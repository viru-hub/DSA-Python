

def reverse(x):
    if x >= 0:
        x = int(str(x)[::-1])
    else:
        x = x*-1
        x = str(x)[::-1]
        x = int(x)*-1

    return x if x >= -2147483648 and x <= 2147483647 else 0

reverse(x= 1534236469)

2**31 - 1

def reverse(self, x: int) -> int:
    x = int(str(x)[::-1]) if x >= 0 else int(str(x*-1)[::-1])*-1
    return x if x >= -2147483648 and x <= 2147483647 else 0
