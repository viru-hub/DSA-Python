n= 10
gen = (x*2 for x in range(n))
res = list(gen)
res

def generator(n):
    for x in n:
        yield x

out = generator(res)
print(next(out))