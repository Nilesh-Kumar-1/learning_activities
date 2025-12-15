a = 1
print(not a)
def dummy(a):
    b = 0
    b = b + 1 if a > 2 else 0
    return b
print(dummy(a))
a = 10
print(dummy(a))