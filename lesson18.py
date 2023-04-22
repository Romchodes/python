"""
Массив — это специальная переменная, которая может содержать более чем одно значение.
"""
print('0 ----------------------------------------------')
cars = ['Ford', 'Opel', 'BMW']
x = cars[0]
print(x)
print('1 ----------------------------------------------')
cars[0] = 'Dodge'
print(cars)
print('2 ----------------------------------------------')
print(len(cars))
print('3 ----------------------------------------------')
for x in cars:
    print(x)
print('4 ----------------------------------------------')
carsAdd = ['Honda', 'Mazda', 'Volvo']

for i in range(len(carsAdd)): #len(carsAdd) = 3 / range(len(carsAdd)) = (0, 3)
    cars.append(carsAdd[i])
print(cars)
print('5 ----------------------------------------------')
cars.pop(5)
print(cars)
cars.pop(4)
print(cars)
print('6 ----------------------------------------------')
cars.remove('Honda')
print(cars)