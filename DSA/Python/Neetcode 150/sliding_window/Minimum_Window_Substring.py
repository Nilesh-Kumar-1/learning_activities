a = {i: i-1 for i in range(10)}
b = {i:i-1 for i in range(2,10)}

print(a.items()-b.items())
print(b in a)
