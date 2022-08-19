import random

"""
    В этом файле я проверял работу функций по формированию списка и 
    разбирался с наследованием классов.
    
    Функции create_list и create_list_shuffle немного разным способом
    выдают один и тот же результат: Отсортированный по возрастанию
    сгенерированный список, в котором находится неповторяющихся
    num значений из диапазона [start, end]
    
    Ну и так по мелочи смотрел - что как работает.
"""


def create_list(start=1, end=90, num=15):
    """
    Функция формирует список из неповторяющихся номеров
    с заданной длиной списка
    :param start: Начальный номер (входит в диапазон)
    :param end: Конечный номер (входит в диапазон)
    :param num: Количество сгенерированных номеров (элементов в списке)
    :return: Отсортированный по возрастанию сгенерированный список, в котором
             находится неповторяющихся num значений из диапазона [start, end]
    """
    lst = []
    i = 0
    while True:
        lst_num = random.randint(start, end)
        if lst_num not in lst:
            lst.append(lst_num)
            i += 1
            if i == num:
                break
    return sorted(lst)


def create_list_shuffle(start=1, end=90, num=15):
    lst = list(range(start, end + 1))
    random.shuffle(lst)
    del lst[num:]
    return sorted(lst)


print(create_list(1, 9, 5))
print(create_list_shuffle(1, 9, 5))
print()


class Parent:  # объявляем родительский класс
    def create_list(self, start=1, end=90, num=15):
        lst = list(range(start, end + 1))
        random.shuffle(lst)
        del lst[num:]
        return sorted(lst)


class Child(Parent):  # объявляем класс наследник
    def __init__(self, start=1, end=90, num=15):
        super().__init__()
        self.card = self.create_list(start=start, end=end, num=num)
        self.card1 = self.create_list(start=start, end=end, num=num)


dd = Child(1, 19, 5)
print(dd.card)
print(dd.card1)

print()
dd = Child(1, 9, 5)
print(dd.card)
print(dd.card1)

print()
a = [2, 3, 5, 6, 8]
print(a)
del a[-1]
print(a)


def create_list2(start=1, end=90, num=5, rows=3):
    """
    Функция формирует список из неповторяющихся номеров
    с заданной длиной списка (num * rows элементов).
    Список состоит из rows пакетов, в каждом пакете num элементов.
    В рамках одного пакета номера отсортированы по возрастанию.
    :param start: Начальный номер (входит в диапазон)
    :param end: Конечный номер (входит в диапазон)
    :param num: Количество сгенерированных номеров (элементов в списке)
    :param rows: Количество "пакетов" со сгенерированными номерами.
                 То есть, список генерируется из num * rows элементов,
                 при этом в рамках одного пакета номера идут в порядке
                 возрастания.
                 Элементы во всём списке не повторяются.
    :return: Отсортированный по возрастанию сгенерированный список, в котором
             находятся неповторяющихся num значений из диапазона [start, end]
    """
    result_list = []
    whole_list = list(range(start, end + 1))
    for i in range(rows):
        random.shuffle(whole_list)
        result_list += sorted(whole_list[:num])
        del whole_list[:num]
    return result_list


a = create_list2(1, 90, 5, 3)
print('\ncreate_list2', a)
print('\ncreate_list2', sorted(a))
b = create_list2(1, 90, 5, 3)
print(a)
print(b)
while True:
    init_card = bool(int(input('номер списка (0/1): ')))
    print('init_card:', init_card)
    num = int(input('Число для поиска: '))
    if num in (a if init_card else b):
        idx = (a if init_card else b).index(num)
    else:
        idx = 0
    print(f'Число {num} ищется в списке {"a" if init_card else "b"}, индекс: {idx}')

# barrel_list = []
# tmp_barrel_list = create_list2()  # Создали из 15 элементов список
# print('\nbarrel_list', tmp_barrel_list)
#
# # номеров в диапазоне [1..90].
# # Это числа, которые должны быть в карточке
# for i in range(3):  # Формируем карточку - расставляя пустые ячейки
#     tmp_zero_list = create_list2(start=1,  # Создали из 4 элементов список
#                                 end=9,  # номеров в диапазоне [1..9]
#                                 num=4,  # Это номера "пустых" ячеек
#                                 rows=1)  # В строке 9 ячеек, 5 с числами.
#     for j in range(1, 10):  # Формируем строку в карточке - расставляя пустые ячейки
#         if j in tmp_zero_list:
#             barrel_list.append('  ')
#         else:
#             num = tmp_barrel_list[0]
#             barrel_list.append(
#                 str(num) if num > 10 else ' ' + str(num)
#             )
#             del tmp_barrel_list[0]
#
# print('\nbarrel_list')
#
# print(barrel_list[:9])
# print(barrel_list[9:18])
# print(barrel_list[18:])

# while True:
#     s = input('Число: ')
#     print(f'Число {s} принадлежит списку: {s in barrel_list}')
