sum1 = []
for i in range(2,1000):
    if i % 5 == 0 or i % 3 == 0:
        sum1.append(i)
print(sum(sum1))
