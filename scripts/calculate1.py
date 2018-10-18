def perimeter(p,P):
    y = 2*p*P/(p+P)
    x = (p*y)**0.5
    return x,y
    
def area(a,A):
    x = (a*A)**0.5
    y = 2*x*A/(x + A)
    return x,y
    
def test(x,y,f):
    print ' ' * 8 + f.func_name
    fmt = '%3.6f  %3.6f'
    print '%3d' % 0, fmt % (x,y)
    for i in range(1,6):
        x,y = f(x,y)
        print '%3d' % i, fmt % (x,y)
    print

# circle diameter 1, polygon = square
p = 4/2**0.5
P = 4*1

test(p,P,f=perimeter)

# circle radius 1, polygon = square
a = 2
A = 2*2
test(a,A,f=area)

