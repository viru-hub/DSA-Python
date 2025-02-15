s = "PAYPALISHIRING"
n = 4
Output = "HolelHlole"

def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    rows = [''] * min(numRows, len(s))
    curRow, goingDown = 0, False

    for c in s:
        rows[curRow] += c
        if curRow == 0 or curRow == numRows - 1:
            goingDown = not goingDown
        curRow += 1 if goingDown else -1

    return ''.join(rows)



def conversion(s, n):
    current_row = 0
    going_down = True
    out_lst = [""]*n

    if n==1:
        return s
    elif len(s) == 1:
        return s
    else:
        for i in s:
            if current_row == 0:
                out_lst[current_row] += i
                current_row += 1
                going_down = True
            elif current_row == n-1:
                out_lst[current_row] +=i
                current_row -=1
                going_down = False
            elif going_down == True:
                out_lst[current_row] += i
                current_row += 1
            elif going_down == False:
                out_lst[current_row] +=i
                current_row -=1


        return "".join(out_lst)


conversion(s=s, n=n)