"""
List (список) — упорядоченная последовательность, которую можно изменять. Допускаются одинаковые элементы.
Tuple (кортеж) — последовательность, которая упорядочена, но не изменяемая. Допускаются одинаковые элементы.
Set (множество) — неупорядоченная изменяемая последовательность. Одинаковые элементы удаляются.
Dict (словарь) — неупорядоченная изменяемая последовательность, состоящая из пар ключ, значение. Ключи не дублируются.
"""

ThisList = ['яблоко', 'апельсин', 'киви']
print('Список:',ThisList, 'класса -', type(ThisList))
print('-----------------------------------------------')
print('First element of the list is "'+ThisList[0]+'"')
print('Second element of the list is "'+ThisList[1]+'"')
print('Third element of the list is "'+ThisList[2]+'"')
ThisList[1] = 'вишня'
print('Second element of the list was changed and now list is:',ThisList)
print('-----------------------------------------------')
print('List in cicle:')
for x in ThisList:
    print(x)
print('------Немного заморочился (Как мне сейчас кажется. Хотя, наверное, это легкотня полная, но сейчас я горд собой)--------')
x = range(len(ThisList))
for i in x:
    print('Now print the',i,'element in list:')
    print(ThisList[i])
print('-----------------------------------------------')
print ('Lenght of the list =', len(ThisList))
print('-----------------------------------------------')
ThisList.append('изюм')
print('One element was added to the list and now it is:',ThisList)
print('-----------------------------------------------')
ThisList.insert(3,'груша')
print('Fourth element was added and now list is:',ThisList)
print('-----------------------------------------------')
List = list(('клубника','арбуз','манго'))
l = len(List)
for i in range(l):
    ThisList.append(List[i]) #ThisList.insert(i,List[i]) если написать так, то подставятся в начало списка
print('Three elements was added to the end of the list and now it is:',ThisList)
print('-----------------------------------------------')
ThisList.reverse()
print('Reversed list:', ThisList)
print('-----------------------------------------------')
l = len(ThisList) # Ну тут вообще замудрил, разбирался около часа вроде, как построить цикл, чтобы удалялись элементы по порядку начиная с первого
for i in range(l):
    DelElement = ThisList.pop(0)
    if ThisList == []:
        print('The', i-1, 'element =', '"' + DelElement + '"', 'was deleted')
        print('List is empty')
    elif i == 0:
        print('List is:', ThisList)
        print('>>>')
    else:
        print('The', i-1, 'element =', '"' + DelElement + '"', 'was deleted')
        print('Now list is:',ThisList)
        print('>>>')