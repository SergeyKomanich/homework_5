"""
Программа запрашивает ввод, с клавиатуры, целых чисел, пока не будет введён 0.
Как только пользователь введёт 0 (ноль), программа должна посчитать и вывести на экран следующие результаты
(без учёта последнего 0):

количество введённых чисел
их сумму
среднее арифметическое всех введённых чисел
максимальное и минимальное значение
количество чётных и не чётных значений

"""
even_number = 0
odd_number = 0
num_sum = 0
num_of_numbers = 0
enter_num = int(input("Введите число: "))
min = max = enter_num

# останавливает цикл при вводе: 0
while enter_num != 0:
# вычисление максимального и минимального значения
    if enter_num > max:
        max = enter_num

    if enter_num < min:
        min = enter_num

    # введенное число плюсуется к уже имеющемуся (сумма всех чисел)
    num_sum += enter_num
    enter_num = int(input())

    # плюсует все вводы
    num_of_numbers += 1

    # выводит среднее арифметическое всех введённых чисел
    arithmetic_mean = num_sum / num_of_numbers

    # количество чётных и не чётных значений
    if enter_num % 2 == 0:
        even_number += 1
    else:
        odd_number += 1

print("Ввели: ", num_of_numbers)
print("Сумма введенных чисел: ", num_sum)
print("Среднеарифметическое: ", arithmetic_mean)
print("Максимальное значение: ", max)
print("Минимальное значение: ", min)
print("Четных: ", even_number)
print("Нечетных: ", odd_number)