n = 10
a,b = 0,1
i = 0
out = []
while i < n-1:
    if len(out) == 0:
        out.append(a)
        out.append(b)
    else:
        out.append(out[-1]+out[-2])
    i += 1