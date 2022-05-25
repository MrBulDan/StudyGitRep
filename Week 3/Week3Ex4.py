seasons = {"Зима": "За окном падал белый снег", "Весна": "Птицы пели прекрасные песни", "Лето": "Солнце светило ярче чем когда-либо", "Осень": "Урожай был невероятным"}
print("Введите месяц своего рождения:")
winter = {12: "Декабрь", 1: "Январь", 2: "Февраль"}
spring = {3: "Март", 4: "Апрель", 5: "Май"}
summer = {6: "Июнь", 7: "Июль", 8: "Август"}
autumn = {9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь"}
year = [winter, spring, summer, autumn]


def season_events(number_of_month):
    for season in year:
        for snum, sname in year[season].items():
            if number_of_month == snum:
                print("Вы родились в ", sname)



    """
    if number_of_month >= 1 & number_of_month <= 3:
        print("Вы родились в ", months[number_of_month], seasons["Зима"])
    elif number_of_month >= 4 & number_of_month <= 6:
        print("Вы родились в ", months[number_of_month], seasons["Весна"])
    elif number_of_month >= 7 & number_of_month <= 9:
        print("Вы родились в ", months[number_of_month], seasons["Лето"])
    else:
        print("Вы родились в ", months[number_of_month], seasons["Осень"])
    """


season_events(int(input()))
