"""
Cycle WHILE
"""
print('0 --------------------------------------------------------')
i = 1
while i < 10:
    print('i =', i)
    i += 1
print('1 --------------------------------------------------------')
i = 1
while i < 10:
    print('i =', i)
    if i == 3:
        break
    i += 1
print('2 --------------------------------------------------------')
i = 0
while i < 10:
    i += 1
    if i%2 == 0:
        continue
    print('i =', i)