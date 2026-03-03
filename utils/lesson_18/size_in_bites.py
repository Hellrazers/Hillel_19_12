import sys

N = 1_000_000

lst = list(range(N))          # список з мільйоном int
rng = range(N)                # range — лінивий (майже не займає)
gen = (x for x in range(N))   # generator
it = iter(range(N))           # Iterator

print("list(range):", sys.getsizeof(lst), "bytes")
print("range:", sys.getsizeof(rng), "bytes")
print("generator:", sys.getsizeof(gen), "bytes")
print("Iterator:", sys.getsizeof(it), "bytes")

# [1..10000]