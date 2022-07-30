def gen(n):
    for i in range(n):
        yield i

for i in range (1000000000):
   for i in gen(10000):
    print(i)