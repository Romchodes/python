'''
Условные выражения и конструкция if
'''
print('0 --------------------------------------------------------')
a = 3
b = 9
print('a =', a, ',', 'b =', b)
if a < b:
    print('"a" smaller than "b"') #обязательна табуляция
print('1 --------------------------------------------------------')
a = 333
b = 333
print('a =', a, ',', 'b =', b)
if a > b:
    print('"a" bigger than "b"')
elif a == b:
    print('"a" equals "b"')
print('2 --------------------------------------------------------')
a = 3
b = 9
print('a =', a, ',', 'b =', b)
if a > b:
    print('"a" bigger than "b"')
elif a == b:
    print('"a" equals "b"')
else: print('"a" smaller than "b"')
print('3 --------------------------------------------------------')
a = 3
b = 7
print('a =', a, ',', 'b =', b)
if a < b: print('"a" smaller than "b"') #однострочная запись
print('4 --------------------------------------------------------')
a = 3
b = 9
print("It's true") if a > b else print("It's not true (false)")
print("First IF scenario worked") if a > b else print("First ELSE scenario worked") if a == b else print("Second ELSE scenarion worked")
#сначала отрабатывает IF конструкция, потом через ELSE задается другая IF конструкция, а потом уже отрабатывает вторая ELSE конструкция
print('5 --------------------------------------------------------')
a = 3
b = 5
c = 7
d = 9
if a < b and c > d:
    print('Both conditions are true')
else: print('One of the conditions is false')
print('6 --------------------------------------------------------')
if a > b or c < d:
    print('One of the conditions is true')