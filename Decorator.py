# Задание:
# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом
# и "Составное" в противном случае.


def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)                    # вызывается функция

        count = 0                                         # Вводится счетчик
        for i in range(2, result):                         # Цикл, где проверяется деление результата
            if result % i == 0:             # Если делится без остатка на каое-либо число из диапазона, то счетчик увеличивается
                count += 1
        if count == 0:
            print(f'Результат: Простое число: {result} ')
        else:
            print(f'Результат: Составное число: {result}')

        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    result = a + b + c
    return result

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

summator = sum_three(a, b, c)

