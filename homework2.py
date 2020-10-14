#задание1

list_1 = [12, None, -77, 'True', True, 9.5]
def my_type(el):
    for el in range(len(list_1)):
        print(type(list_1[el]))
    return
my_type(list_1)

#задание2
el_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
el = 0
while i < el_count:
    my_list.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
        el += 2
print(my_list)

#задание3
month = int(input("Введите число, соответствующее месяцу"))
season_list = ('winter', 'spring', 'summer', 'autumn')
season_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
if month ==1 or month ==2 or month == 12:
    print(season_list[0])
    print(season_dict.get(1))
elif month ==3 or month ==4 or month == 5:
    print(season_list[1])
    print(season_dict.get(2))
elif month ==6 or month ==7 or month == 8:
    print(season_list[2])
    print(season_dict.get(3))
elif month ==9 or month ==10 or month == 11:
    print(season_list[3])
    print(season_dict.get(4))
else:
    print("Такого месяца не существует. Необходимо ввесте число, соответствующее месяцу, от 1 до 12")

#задание4
string = input("Введите строку из нескольких слов")
for el in string:
    print(el)

