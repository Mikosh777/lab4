#Task 1
try:
    str1 = input("Введите строку без пробелов: ")
    str1 = str1.strip()

    if " " in str1: 
        raise ValueError("Ввод не должен содержать пробелы.")

    input_tuple = tuple(char for char in str1)  # Используем генератор кортежей

    print("Созданный кортеж:")
    print(input_tuple)

except ValueError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Произошла ошибка: {e}")

#Task1.2
# Создадим кортеж из задачи 1.1
input_tuple = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')

# Преобразуем кортеж в строку, объединяя его элементы
result_string = ''.join(input_tuple)
print(f"The string is: '{result_string}'")

#Task 1.3
tuple_A = (1, 2, 3, 4, 5, 6, 7)
tuple_B = (5, 6, 7, 9, 7, 1, 10, 10)

# Разделим кортежи на две половины
half_A = len(tuple_A) // 2
half_B = len(tuple_B) // 2

# добавляем первую половину кортежа A и вторую половину кортежа B
result_tuple = tuple_A[:half_A] + tuple_B[half_B:]

print(result_tuple)

#Task 1.4
def count_element_occurrences(input_tuple):
    element_counts = {}  # Создаем словарь для отслеживания количества вхождений элементов

    # Подсчет количества вхождений элементов в кортеже
    for element in input_tuple:
        if element in element_counts:
            element_counts[element] += 1
        else:
            element_counts[element] = 1

    # Создаем кортеж из пар элементов и их количества вхождений
    result_tuple = tuple((element, count) for element, count in element_counts.items())

    return result_tuple

input_tuple1 = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)
input_tuple2 = ('55', '6', '777', 54, 6, 7777, 9, 777, 6)
input_tuple3 = ((1, 2, 3), (['A', 'B']), (1, 2, 3), (['A']))

# Вызываем функцию и выводим результат
output_tuple1 = count_element_occurrences(input_tuple1)
output_tuple2 = count_element_occurrences(input_tuple2)
output_tuple3 = count_element_occurrences(input_tuple3)

print("Sample Output 1:")
print(output_tuple1)

print("Sample Output 2:")
print(output_tuple2)

print("Sample Output 3:")
print(output_tuple3)

#Task 1.5
def create_data_type_tuples(input_data):
    integer_tuple = tuple()  # Создаем пустой кортеж для целых чисел
    float_tuple = tuple()    # Создаем пустой кортеж для чисел с плавающей точкой
    string_tuple = tuple()   # Создаем пустой кортеж для строк

    for item in input_data:
        if isinstance(item, int):
            integer_tuple += (item,)  # Если элемент - целое число, добавляем его в кортеж целых чисел
        elif isinstance(item, float):
            float_tuple += (item,)    # Если элемент - число с плавающей точкой, добавляем его в кортеж чисел с плавающей точкой
        elif isinstance(item, str):
            string_tuple += (item,)   # Если элемент - строка, добавляем его в кортеж строк

    # Выводим результирующие кортежи
    if integer_tuple:
        print(integer_tuple)
    if float_tuple:
        print(float_tuple)
    if string_tuple:
        print(string_tuple)

# Пример входных данных
input_data1 = (55, 6, 777, 70.0, '7', 'A')

# Вызываем функцию
create_data_type_tuples(input_data1)

#Task 2.1
def create_set_from_input():
    try:
        user_input = input("Введите строку без пробелов: ")
        if not user_input:
            raise ValueError("Ввод не должен быть пустым.")
        user_input = user_input.strip()  # Удалить начальные и конечные пробелы, если они есть

        # Создаем множество, используя set comprehension
        input_set = {char for char in user_input}

        # Выводим созданное множество
        print("Созданное множество:")
        print(input_set)

    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Вызываем функцию для запуска кода
create_set_from_input()

#Task 2.2
set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}

# Создаем множество, представляющее разницу между set_A и set_B
result_set = set_A.difference(set_B)

print(result_set)

#Task 2.3
set_A = {1, 2, 3, 4, 5}
set_B = {5, 7, 8, 9, 2, 10}

# Удаляем элементы из set_A, которые также присутствуют в set_B
set_A.difference_update(set_B)

print(set_A)

#Task 2.4
set_A = {1, 2, 3, 4, 7}
set_B = {8, 7, 9, 4, 2, 0, 10}
set_C = {4, 0, 1}

# Проходим по элементам множества set_A
for element in set_A.copy():
    if element in set_C:
        set_A.remove(element)
        set_B.add(element)

# Выводим обновленное множество set_C
print("Updated set_C =", set_C.union(set_B))

#Task 2.5
from itertools import combinations #библиотека для комбинации

A = {1, 2, 3, 4, 5, 6}
n = 3
m = 5

# Создаем список множеств заданного размера n
list_of_sets = []

# Генерируем уникальные комбинации и добавляем их в список
for combo in combinations(A, n):
    if len(list_of_sets) == m:  # Проверяем размер списка
        break
    list_of_sets.append(set(combo))
print(list_of_sets)

#Task 3
from itertools import groupby

# Пример входных данных
cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'),
             ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]

# Сортируем список автомобилей по производителю
sorted_cars = sorted(cars_list, key=lambda x: x[0])

# Группируем отсортированные автомобили по производителю
grouped_cars = groupby(sorted_cars, key=lambda x: x[0])

# Выводим сгруппированные данные
for manufacturer, cars in grouped_cars:
    cars = list(cars)
    car_count = len(cars)
    print(f"{manufacturer} {car_count}")

    for car in cars:
        print(f"- {car[1]}")
