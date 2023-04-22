"""
Функция — блок кода, который запускается только при его вызове.
Вы можете передавать данные, известные как параметры, в функцию.
В результате у функции появляется возможность возвращать данные.
"""
print('0 ----------------------------------------------')
def myFirstFunction():
    print('Hello from function')
myFirstFunction()
print('1 ----------------------------------------------')
def mySecondFunction(name):
    print(name, 'Иванов')
mySecondFunction('Иван')
mySecondFunction('Петр')
mySecondFunction('Василий')
print('2 ----------------------------------------------')
def myThirdFunction(country='Russia'):
    if country == 'Russia':
        print('I will return in', country, 'sometimes')
    else:
        print('I will be in', country, 'sometimes')
myThirdFunction()
myThirdFunction('Norway')
myThirdFunction('Switzerland')
myThirdFunction('Canada')
print('3 ----------------------------------------------')
def myFourthFunction(x):
    return 3 * x
print(myFourthFunction(3))
print(myFourthFunction(5))
print(myFourthFunction(9))