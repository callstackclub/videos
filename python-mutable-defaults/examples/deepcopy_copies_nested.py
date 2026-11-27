import copy

a = [[1]]
b = copy.deepcopy(a)
b[0].append(2)
print(a)
print(b)
print(a[0] is b[0])