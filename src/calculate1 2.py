def trig(s,c):
    C = (0.5 + c/2)**0.5
    S = 0.5*s/C
    return (S,C)

n = 4
S = 1/2**0.5
C = S

print ' ' * 8 + "trig"
for i in range(6):
    fmt = '%3d %3.6f  %3.6f'
    print fmt % (n, n*S, n*S/C)
    S,C = trig(S,C)
    n *= 2

    