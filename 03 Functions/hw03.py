# ==================
# ДЗ №3: функции
# Дедлайн: 04 ноября 18:14
# Результат присылать на адрес nike64@gmail.com

# также прочитайте раздел "Функции" из книги "A byte of Python" (с.59)

# Задание: сделайте анализ возрастного состава группы студентов, используя функции.
# Помните, что а) у некоторых студентов отсутствуют данные по возрасту, б) возраст может быть задан диапазоном, например, 25-35. Поэтому не забывайте обрабатывать ошибки и исключения!

import csv

# помним, что в этот раз мы читаем не список списков, а список словарей!
# ключи в словаре для каждого студента называются по первой строчке из файла student_ages.csv: "Номер в списке", "Возраст"
ages_list = list()
with open('ages.csv', encoding="utf-8") as csvfile:
    ages_dictreader = csv.DictReader(csvfile, delimiter=',')
    ages_list = list(ages_dictreader)

# подсказка: вот так мы можем получить данные из списка словарей
# именно так мы уже делали в коде лекции с квартирами
for al in ages_list:
    print(f'"Номер в списке": {al["Номер в списке"]}, "Возраст": {al["Возраст"]}')
    print()


# Задание 1: напишите функцию, которая разделяет выборку студентов на две части: меньше или равно указанного возраста и больше указанного возраста
# вернуться должна пара "Номер в списке, Возраст"
def filter_students_1(age):
    under_list = list()
    upper_list = list()
    unknownage_count = 0

    # TODO 1: напишите ваш код проверки.
    # не забудьте исключить студентов, у которых возраст не указан, и подсчитать их количество
    for al in ages_list:
        try:
            if al["Возраст"] != "":
                if int(al["Возраст"]) <= age:
                    under_list.append(al)
                else:
                    upper_list.append(al)
            else:
                unknownage_count += 1
        except:
            exc = al["Возраст"].split("-")
            if int(exc[0]) > age:
                upper_list.append(al)
            if int(exc[1]) < age:
                under_list.append(al)

    # возвращаем результат из функции:
    return under_list, upper_list, unknownage_count


# вызываем функцию:
und_list, upp_list, unknwncount = filter_students_1(30)
# TODO 2: выведите результат:
print("Ниже указанного")
for i in und_list:
    print( i["Номер в списке"], i["Возраст"])
print()

print("Выше указанного")
for i in upp_list:
    print( i["Номер в списке"], i["Возраст"])
print() 

print(f"Без возраста: {unknwncount}")
print()

# Задание 2: улучшите функцию filter_students_1
# напишите функцию, которая принимает переменное количество параметров, каждый из которых может быть необязательным:
# Список и пример передачи параметров: age=30, warn=True, show_average=True
# 1) warn=True (False) - параметр, указывающий, что делать со студентами, которые не указали возраст:
# если возраст не указали значительно большее количество студентов, чем указали, выводите дополнительно предупреждение, что выборка неточная
# 2) show_average=True (False) нужно ли подсчитать и отобразить средний возраст студента.

# все параметры передавайте как **kwargs, т.е. пару "название параметра - значение параметра"
def filter_students_2(**kwargs):
    under_list = list()
    upper_list = list()
    unknownage_count = 0

    # TODO 3: скопируйте сюда текст функции filter_students_1, которую вы написали ранее, и измените ее так, чтобы она работала с параметрами **kwargs
    newage = kwargs.get("age")

    for al in ages_list:
        try:
            if al["Возраст"] != "":
                if int(al["Возраст"]) <= newage:
                    under_list.append(al)
                else:
                    upper_list.append(al)
            else:
                unknownage_count += 1
        except:
            exc = al["Возраст"].split("-")
            if int(exc[0]) > newage:
                upper_list.append(al)
            if int(exc[1]) < newage:
                under_list.append(al)

    # возвращаем результат из функции:
    return under_list, upper_list, unknownage_count

    # TODO 4: получите остальные два параметра по аналогии:
    warn_if_toomany = kwargs.get("warn")
    show_average = kwargs.get("show_average")

    # TODO 5: сделайте проверку. Если значение параметра warn, show_average = True, выполните соответствующую обработку. Например:
    if warn_if_toomany == True:
    # напишите здесь код проверки и вывод предупреждающего сообщения пользователю
        if unknownage_count > len(ages_list)/2:
            print("Выборка неточная", end="")
    if show_average == True:
        sum = 0
        for i in ages_list:
            if i["Возраст"] != "":
                try:
                    sum += int(i["Возраст"])
                except:
                    exc = i["Возраст"].split("-")
                    sum += (int(i[0]) + int(i[1])) / 2
    # напишите здесь код подсчета и вывода среднего значения возраста студентов
    print("Средний возраст: ", sum / (len(ages_list) - unknownage_count))
    print()

    # возвращаем результат из функции:
    return under_list, upper_list, unknownage_count


# вызываем функцию filter_students_2
und_list, upp_list, unknwncount = filter_students_2(age=30, warn=True, show_average=True)
print("Ниже указанного")
for i in und_list:
    print( i["Номер в списке"], i["Возраст"])
print()

print("Выше указанного")
for i in upp_list:
    print( i["Номер в списке"], i["Возраст"])
print() 

print(f"Без возраста: {unknwncount}")



