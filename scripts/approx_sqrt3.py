N = 50000
L = [n**2 for n in range(5*N)]

# find first value with j**2 > 3 * i**2
def f(i):
    for j in range(i,N):
        if L[j] > L[i] * 3:
            return j

for i in range(N):
    n = 3
    j = f(i)
    if not j:
        continue
        
    triple = L[i] * 3
    low = triple - L[j-1]
    high = L[j] - triple
    if low < n or high < n:
        t = (i, j-1, low, j, high)
        print "%6d %6d %6d %6d %6d" % t

