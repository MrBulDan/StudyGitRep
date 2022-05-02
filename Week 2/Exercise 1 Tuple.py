from collections import Counter
# Создаем кортеж
FirstTuple = ("Элемент 1", "Элемент 2", "Элемент 3", "Элемент 3")
print(FirstTuple)
# Добавить новый элемент нельзя так как это неизменяемый тип данных
# Получим 4й элемент кортежа
print(FirstTuple[3])
# Удалить элемент кортежа нельзя
print(Counter(FirstTuple))
