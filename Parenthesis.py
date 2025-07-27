def gen_parenthesis_util(n, open, close, s, ans):

    if open == n and close == n:
        ans.append(s)

    if open < n:
        gen_parenthesis_util(n, open + 1, close, s + "{", ans)

    if close < open:
        gen_parenthesis_util(n, open, close + 1, s + "}", ans)

def AllParenthesis(n):
  
    # List for storing the answer
    ans = []
    if n > 0:
        gen_parenthesis_util(n, 0, 0, "", ans)
    return ans

if __name__ == "__main__":
    n = 3
    ans = AllParenthesis(n)

    for s in ans:
        print(s)
ans
