n= 600851475143
d = 2
factors = []
while d*d <= n:
    while n%d == 0:
        n //= d
        factors.append(d)
    d += 1
if n != 1:
    factors.append(n)
print(max(factors))
