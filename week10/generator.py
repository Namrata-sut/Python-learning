# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def fun():
    yield 1
    yield 2
    yield 3


for val in fun():
    print(val)
