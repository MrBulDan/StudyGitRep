# Леха, прошу прощения что долго проебывался))
# Создадим словарь
FirstVoc = {"Teacher" : "Леха", "Student" : "Даня"}
print(FirstVoc)
# Добавим новый элемент типа int с ключем str
FirstVoc["ExerciseNumber"] = 3
print(FirstVoc)
# Создадим элемент с ключем типа кортеж и значением типа список
TupKey = (1, 2, 3)
ListMean = [1, 2]
FirstVoc[TupKey] = ListMean
print(FirstVoc)
# Получим элемент словаря по ключу
print("Самый лучший учитель для ", FirstVoc["Student"], ", это ", FirstVoc["Teacher"])
# Удалим элемент словаря по ключу
del FirstVoc[TupKey]
print(FirstVoc)
# Получим список всех ключей словаря
print(dict.keys(FirstVoc))