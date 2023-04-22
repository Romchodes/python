"""
Dict (словарь) — неупорядоченная изменяемая последовательность, состоящая из пар ключ, значение. Ключи не дублируются.
"""
print('0 --------------------------------------------------------')
thisDict = {'color': 'red', 'size': 'small', 'fruit': 'true', 'count': 3, 'vegetable': 'false'}
print('Information about cherry is:', thisDict)
print('1 --------------------------------------------------------')
print(thisDict['color'])
print(thisDict.get('fruit'))
print('2 --------------------------------------------------------')
thisDict['color'] = 'bloodly red'
print('Information about cherry after color clarify is :', thisDict) #clarification - уточнить, clarify - уточнение
print('3 --------------------------------------------------------')
print('Keys of the dict by using the cycle:')
for i in thisDict:
    print(i)
print('Values of the keys in the dict by using the cycle:')
for i in thisDict:
    print(thisDict[i])
print('Values of the keys in the dict by using the cycle and .values function:')
for i in thisDict.values():
    print(i)
print('4 --------------------------------------------------------')
print('Keys-values of the dict by using the cycle:')
for i, k in thisDict.items():
    print(i, k)
print('5 --------------------------------------------------------')
print(len(thisDict))
print('6 --------------------------------------------------------')
thisDict['loved'] = 'by_me'
print(thisDict)
print('7 --------------------------------------------------------')
print('Deleted value for key "size" is:', thisDict.pop('size'))
print(thisDict)
print('Deleted key-value is:', thisDict.popitem())
print(thisDict)
del thisDict['vegetable']
print(thisDict)
thisDict.clear()
print(thisDict)
del thisDict #print(thisDict) вызовет ошибку, так как словарь удален
print('8 --------------------------------------------------------')
newDict = dict(color='light_red', size='small', fruit='true')
print('The new dict is:', newDict)