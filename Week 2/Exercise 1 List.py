from collections import Counter
# Создаем список
FirstList = ["Элемент 0", "Элемент 1", "Элемент 2"]
print(FirstList)
# Добавляем новый элемент в конец списка
FirstList.append("Элемент 3")
print(FirstList)
# Добавляем новый элемент списка на место с индексом 3
IntNum = 5
FirstList.insert(3, IntNum)
print(FirstList)
# Добавим новый список в конец первого списка
SecList = [0b010, 0b100]
FirstList.append(SecList)
print(FirstList)
# Добавим новый кортеж в список
FirstTuple = "Tuple 1", "Tuple 2", "Tuple 3"
FirstList.insert(3, FirstTuple)
print(FirstList)
# получим 4ый элемент списка
print("4ый элемент списка - ", FirstList[4])
# Удалим элемент с индексом 3
del FirstList[3]
print(FirstList)
# Найдем количество повторяющихся элементов списка нельзя
print(Counter(FirstList))
