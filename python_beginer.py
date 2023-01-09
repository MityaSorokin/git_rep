import math

def arithmetic(arg1, arg2, op):
    if op == '+':
        return arg1 + arg2
    elif op == '-':
        return arg1 - arg2
    elif op == '*':
        return arg1 * arg2
    elif op == '/':
        return arg1 / arg2
    else:
        return "Неизвестная операция"

print(arithmetic(11, 22, '*'))
#year = int(input('input year -'))

def is_the_year_leap (year):
    if year % 400 == 0:
        return print(366)
    elif year % 100 == 0:
        return print(365)
    elif year % 4 == 0:
        return print(366)
    else:
        return print(365)

is_the_year_leap(2024)

def square (width):
    a = width * 4
    b = width ** 2
    c = math.sqrt(width ** 2 + width ** 2)
    return print(a, b, c)
square(1)

def season(month_num):
    if month_num < 3 or month_num == 12:
        return print("winter")
    elif month_num > 2 and month_num < 6:
        return print("spring")
    elif month_num > 5 and month_num < 9:
        return print("summer")
    else:
        return print("autumn")

season(6)

def bank (a, years):
    for x in range(years):
        a = a * 0.1 + a
    return print("money you've earned ", a)

bank(100, 10)

def is_prime(number):
    if number == 0 or number == 1:
        return print(number, " not a prime")
    for i in range(2, number):
        #print(number % i)
        if number % i == 0:
            return print(number, " not a prime")
    return print(number, " - is a prime")
is_prime(102)

def date(day, month, year):
    day_in_month = {1: 31,
                    2: 29 if is_the_year_leap(year) else 28,
                    3: 31,
                    4: 30,
                    5: 31,
                    6: 30,
                    7: 31,
                    8: 31,
                    9: 30,
                    10: 31,
                    11: 30,
                    12: 31}

    if 1 <= month <= 12 and 1 <= day <= day_in_month[month]:
        return True
    return False


def date_cheat(day, month, year):
    """Проще, но это непедагогично :)"""
    import datetime
    try:
        datetime.date(day, month, year)
    except ValueError:
        return False
    else:
        return True

print(date_cheat(29,2,2000))


import itertools


def XOR_cipher(string, key):

    answer = []

    key = itertools.cycle(key)  # Повторяем ключ, чтобы зашифровать всю строку

    for s, k in zip(string, key):
        answer.append(chr(ord(s) ^ ord(k)))

    return ''.join(answer)

# Функция для расшифровки точно такая же
XOR_uncipher = XOR_cipher
