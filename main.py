import random
def create_list(list_lenght=10, start_value=1, end_value=10) -> list:
    new_list = []
    for _ in range(list_lenght):
        new_list.append(random.randint(start_value, end_value))
    return new_list

# Завдання 1
# Напишіть функцію, яка обчислює добуток елементів списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.
def mult_numbers(numbers):
    n = 1
    for i in numbers:
        n = i * n
    return n

#Завдання 2
#Напишіть функцію для знаходження мінімуму у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.

def find_min(numbers):
    n = min(my_number)
    return n

#Завдання 3
#Напишіть функцію, яка визначає кількість простих чисел у списку цілих.
# Список передається як параметр. Отриманий результат повертається із функції.
def count_simple_numbers(numbers):
    n = 0
    for number in numbers:
        is_simple = True
        if number < 2:
            n = n + 1
            continue
        for i in range(2, number):
            if number % i == 0:
                is_simple = False
                break
        if is_simple:
            n = n + 1
    return n

#Завдання 4
#Напишіть функцію, яка видаляє зі списку ціле задане число.
# З функції потрібно повернути кількість видаленних елементів.

def delete_input_number(numbers):
    n = int(input("Введіть число яке бажаєте видалити - "))
    r = 0
    for i in numbers:
        if i == n:
            numbers.remove(n)
            r = r + 1
    return r

#Завдання 5
#Напишіть функцію, яка отримує два списки як параметр і повертає список, що містить елементи обох списків.

def two_lists_in_elements(numbers):
    list_one = numbers
    list_two = numbers
    list_end = list_one + list_two
    return list_end

#Завдання 6
# Напишіть функцію, яка обчислює ступінь кожного елемента списку цілих.
# Значення для ступеня передається як параметр, список також передається як параметр.
# Функція повертає новий список, який містить отримані результати.

def degree_result(numbers:list, degree:int):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** degree
    return numbers

my_number = create_list()
two_elem = two_lists_in_elements(my_number)
print("Список ", my_number)
mult_number = mult_numbers(my_number)
print("Добуток всіх чисел із списку = ", mult_number)
min_list = find_min(my_number)
print("Мінімальне число із списку = ", min_list)
count_sum = count_simple_numbers(my_number)
print("Кількість простих чисел у списку ", count_sum)
print("Список з двох списків ", two_elem)
degree_pass = degree_result(my_number, 3)
print("Ступінь елементів (3) ", degree_pass)
del_numb = delete_input_number(my_number)
print("Кількість вказаних чисел, що були видалені ", del_numb)





