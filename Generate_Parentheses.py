###https://leetcode.com/problems/generate-parentheses/description/?envType=problem-list-v2&envId=dynamic-programming

n =3

res = []

def dfs(openP, closeP, s):
    if openP == closeP and openP + closeP == n * 2:
        res.append(s)
        return
    
    if openP < n:
        dfs(openP + 1, closeP, s + "(")
    
    if closeP < openP:
        dfs(openP, closeP + 1, s + ")")

dfs(0,0,"")
res