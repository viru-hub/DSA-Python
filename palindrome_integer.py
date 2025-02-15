x = 121

def palindrome_integer(x):
    if x >= -2**31 and x <= 2**31 - 1:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
