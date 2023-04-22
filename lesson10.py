"""
Tuple (кортеж) — последовательность, которая упорядочена, но не изменяемая. Допускаются одинаковые элементы.
"""
thisTuple = ('яблоко', 'вишня', 'апельсин')
print('The tuple =', thisTuple)
print('----------------------------------------------------')
print('The first element of the tuple is:', thisTuple[0])
print('----------------------------------------------------')
for i in thisTuple:
    print(i)
print('----------------------------------------------------')
print('The length of tuple is', len(thisTuple))
print('----------------------------------------------------')
del thisTuple
#print(thisTuple) Команда не пройдет, так как весь кортеж удалился
newTurple = tuple(('арбуз', 'дыня', 'лимон'))
print(newTurple)