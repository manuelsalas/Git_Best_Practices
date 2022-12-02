a = 0
b = 1
print(str(a))
print(str(b))
s = b
while s<1000:
    s = a + b
    print(str(s))
    a = b
    b = s
