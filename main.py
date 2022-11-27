k=0
def f(n,p10,p29):
    if n==33 and p10==1 and p29==0: global k; k = k + 1
    if n<33:
        if n == 10: p10=1
        if n == 29: p29=1
        f(n+1,p10,p29);f(n*3,p10,p29)
f(2,0,0)
print(k)