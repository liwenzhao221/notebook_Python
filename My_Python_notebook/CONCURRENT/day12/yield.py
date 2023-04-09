def fun():
    print("start")
    yield 1
    print("end")

g = fun()
print(g.__next__()) # next(g)
print(g.__next__())