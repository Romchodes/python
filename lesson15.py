"""
Cycle FOR
"""
print('0 --------------------------------------------------------')
list = ['apple', 'orange', 'cherry']
for i in list:
    print (i)
print('1 --------------------------------------------------------')
string = 'lemon'
for i in string:
    print(i)
print('2 --------------------------------------------------------')
list = ['apple', 'cherry', 'orange', 'lemon', 'strawberry']
print(list)
for i in list:
    print(i)
    if i == 'orange':
        break
print('3 --------------------------------------------------------')
print(list)
for i in list:
    if i == 'strawberry':
        break
    print(i)
print('4 --------------------------------------------------------')
print(list)
for i in list:
    if i == 'lemon':
        continue
    print(i)
print('5 --------------------------------------------------------')
for i in range(10):
    print(i)
print('6 --------------------------------------------------------')
for i in range(3, 10):
    print(i)
print('7 --------------------------------------------------------')
for i in range(0, 10, 3):
    print(i)
print('8 --------------------------------------------------------')
for i in range(10):
    print(i)
else: print('Cycle is over')
print('9 --------------------------------------------------------')
list0 = ['apple', 'cherry', 'orange', 'lemon', 'strawberry']
list1 = ['green', 'red', 'yellow']
for i in list0:
    for j in list1:
        print(j, i)
print('10 --------------------------------------------------------')
#пока не понятно, надо разобраться
def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\nРезультат примера рекурсии")
tri_recursion(5)