# задание 1
a = 10
b = "Hello!"
print(a, b)
a = input("Введите Ваше имя: ")
b = int(input("Сколько Вам лет?"))
print("Привет", a, "Тебе", b, "лет")

# задание2
time = int(input("Введите время в секундах: "))
hours = (time // 3600) % 24
min = (time // 60) % 60
sec = time % 60
print('%02d:%02d:%02d' % (hours, min, sec))

# задание3

n = int(input("Введите число: "))
res = (n + int(str(n) + str(n)) + int(str(n) + str(n) + str(n)))
print("Сумма чисел равна %d" % res)

# задание4

n = abs(int(input("Введите целое положительное число: ")))
max = n % 10
while n > 0:
    if n % 10 > max:
        max = n % 10
    n = n // 10
print(max)

# задание5

rev = float(input("Введите сумму выручки компании: "))
cost = float(input("Введите сумму издержек компании: "))
if rev > cost:
    rent = (rev - cost) / rev * 100
    print(f"Поздравляю! Ваша компания работает с прибылью! Ваша рентабельность: {rent:.2f} %")
    staff = int(input("Введите численность сотрудников: "))
    print(f"Прибыль в расчете на одного сотрудника составляет: {(rev - cost) / staff:.2f}")

else:
    print("Компания работает с убытком")

# задание6
a = float(input("Результат первого дня составил: "))
b = float(input("Желаемый результат: "))
days = 1
while a < b:
    a = a * 1.1
    days += 1
print("Через {} дней Вы достигнете желаемого результата в {} км".format(days, b))
