import csv

students_list = list()

with open('test_data.csv', encoding="utf-8") as csvfile:
    flats_csv = csv.reader(csvfile, delimiter=',')
    students_list = list(flats_csv)

#print(students_list)

# TODO 1: используя множества, выведите все иностранные языки, которыми владеют студенты (без повторов). например, в таком виде:
# Английский,Украинский

langs = set()
a = []

for i in students_list:
	a.append(str(i[1]).lower().strip())

a.pop(0)

langs = set(a)

print(langs)


# TODO 2: у некоторых студентов язык не указан. Сделайте проверку на пустое значение через assert
# не забудьте добавить код перехвата и обработки исключения

for i in students_list:
	try:
		assert i[1] != ""
	except:
		print("Язык не указан")


# TODO 3: подсчитайте и выведите УНИКАЛЬНЫЕ имена студентов (т.е. те, которые встретились в списке students_list только один раз)
# например, в таком виде: Кирилл, Максим, Гильтяй,...
# для неуникальных имен выведите имя и количество повторов. Например:  Андрей, 2
# подсказка: решите эту задачу не "в лоб" перебором списка, а другим способом:
# 1) сделайте множество из имен,
# 2) используйте его для прохода по списку и подсчета частоты встречаемости имен
# не забудьте отделить фамилию от имени через string.split()
name = set()
for i in students_list:
	a.append(str(i[0]).strip)
	print(a)
