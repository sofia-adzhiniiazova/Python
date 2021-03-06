#: 1Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(*nums):
    try:
        a = int(input("Введите первое число\n"))
        b = int(input("Введите второе число\n"))
        result = a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'
    except ValueError:
        return 'Введите число'
    return result


print(division())


# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: ФИО, год рождения, город проживания, email, тел.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def user(**kwargs):
    return kwargs


print(user(name='Sofia', surname='Adzhiniyazova', year='1992', city='Moscow', email='123@example.com', phone='123456'))


# 3.Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(*args):
    a = int(input("введите первое число\n"))
    b = int(input("введите второе число\n"))
    c = int(input("введите третье число\n"))
    if c < a and c < b:
        return a + b
    elif b < a and b < c:
        return a + c
    else:
        return b + c


print(my_func())


#4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.


def my_func(*args):
    x = int(input("Введите действительное положительное число\n"))
    y = int(input("Введите целое отрицательное число\n"))
    if x <= 0 or y >= 0:
        print("Введены некорректные данные")
    else:
        return x ** y


print(my_func())


#5.Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
#Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def my_sum():
    sum_result = 0
    ex = False
    while ex == False:
        nums = input('Введите числа через пробел или нажмите q для выхода: ').split()
        sum = 0
        for el in range(len(nums)):
            if nums[el] == 'q' or nums[el] == 'Q':
                ex = True
                break
            else:
                sum = sum + int(nums[el])
        sum_result = sum_result + sum
        print(f'Current sum is {sum_result}')
    print(f'Your final sum is {sum_result}')

my_sum()


#6 Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
#Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().


def int_func(*args):
    words = input("Введите слова на латиннице с маленькой буквы: ")
    print(words.title())
    return


int_func()

