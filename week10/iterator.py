# An iterator in Python is an object that allows you to loop through (iterate) a collection
# (like lists, tuples, or dictionaries) takes one element at a time.
class EvanNumber:
    def __iter__(self):
        self.n = 2
        return self

    def __next__(self):
        x = self.n
        self.n += 2
        return x


even = EvanNumber()
iterator_even = iter(even)
print(next(iterator_even))
print(next(iterator_even))
print(next(iterator_even))
print(next(iterator_even))
print(next(iterator_even))

list_vals = [10, 20, 30, 40, 50]
iter_vals = iter(list_vals)

while True:
    try:
        print(next(iter_vals))
    except StopIteration:
        print("End of Iteration.")
        break
        
