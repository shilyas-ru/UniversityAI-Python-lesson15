"""

Задание
1. Создать новый проект ""Игра лото""
2. Правила игры можно посмотреть ниже в комментах.
3. Написать игру лото.

Карточки игроков выводятся на экран.
Если в файл сможете сохранить - то же можно.
В принципе, запускаем игру и карточки формируются и выводятся для каждого игрока на экран.
Числа желательно расположить как в правилах - чтобы красиво было.
Если не получится, то как угодно, главное, чтобы было 3 строки по 5 случайных чисел в строке

В идеале: 3 строки по 9 клеток, заполнены по 5 чисел в каждой строке.
Сначала есть карточка с числами.
Потом новый ход, зачеркнули, снова карточки выводятся с зачеркнутыми числами.

Каждый ход выводится карточка заново.
Как отображается ход в игре - ниже в правилах.


Возможные подходы к решению задачи:
1) Проектирование на основании предметной области. Подумать какие объекты есть в игре и
какие из них можно перенести в программу. Для них создать классы с соответствующими
свойствами и методами. Проверить каждый класс отдельно.
Написать программу с помощью этих классов;

2) Метод грубой силы + рефакторинг. Написать программу как получиться.
После этого с помощью принципа DRY убрать дублирование в коде;

3) Процедурное программирование.

4. Минимальные требования: 2 игрока - человек играет с компьютером;
5. (Дополнительно *) возможность выбирать тип обоих игроков (компьютер или человек)
таки образом чтобы можно было играть: компьютер - человек, человек - человек,
компьютер - компьютер;
6. (Дополнительно *) возможность играть для любого количества игроков от 2 и более;

7. Выложите проект на github;


-------------------------------- Лото --------------------------------
---------------------------- Правила игры ----------------------------

Игра состоит из специальных карточек, на которых отмечены числа, и бочонков с цифрами

Всего 90 бочонков с цифрами от 1 до 90 (В жизни они обычно достаются из мешка,
чтобы можно было вытянуть случайно)

Каждая карточка содержит 3 строки по 9 клеток. 5 каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны.

Так выглядит пример карточки:
--------------------------
__  9 43 62 __ __ __ 74 90
 2 __ 27 __ 75 78 __ 82 __
__ 41 56 63 __ __ 76 __ 86
--------------------------

В игре 2 игрока: пользователь и компьютер (*так же может быть 2 пользователя или 2 компьютера).
Каждому в начале выдается случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
       Если цифра есть на карточке - она зачеркивается и игра продолжается.
       Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
       Если цифра есть на карточке - игрок проигрывает и игра завершается.
       Если цифры на карточке нет - игра продолжается.

Компьютер всегда правильно зачеркивает свои цифры, если они есть, и продолжает, если их нет.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода (как может выглядеть интерфейс игры):
 -- (знаком минус) отмечены уже зачеркнутые цифры
 __ (знаком подчёркивания) отмечены пустые клетки в карточке
    Теоретически, можно заменить на пробелы.
Под номер отводится два символа. Соответственно, если номер 
состоит из единственной цифры, то слева он дополняется пробелом.

Так выглядит ход игры:

          Новый бочонок: 70 (осталось 76)

          ----- Ваша карточка ------
           6  7 __ __ 43 62 __ 74 90
          __ 14 26 __ -- __ 78 __ 82
          23 33 __ 38 __ 48 __ 71 __
          --------------------------

          -- Карточка компьютера ---
           7 87 __ -- 14 __ 11 __ __
          __ __ 16 49 __ 55 88 __ 77
          __ 15 20 __ -- __ -- 76 __
          --------------------------

          Зачеркнуть цифру? (у/n)

Подсказка: для работы с псевдослучайными числами удобно использовать модуль random:
- http://docs.python.org/3/library/random.html
- https://docs-python.ru/standart-library/modul-random-python/

Подсказка: для написания программы удобно использовать ООП,
примеры возможных классов: Игрок, Бочонок, Мешок, Карточка, ...

Так же можно придумать свою структуру классов либо воспользоваться процедурным программированием

"""


# Игрок - Player, Бочонок - Barrel, Мешок - Bag, Карточка - Card
import random


class Bag:
    """
    Это мешок с бочонками.
    Должен уметь:
    - Формировать (инициилизировать) бочонки в мешке (номера от 1 до 90 включительно).
    - Перемешивать имеющиеся в нём бочонки.
    - Вытаскивать бочонок, удаляя его из мешка.
    - Печатать содержимое мешка (для служебных целей).
    - Выдавать количество оставшихся в мешке бочонков.
    """
    def __init__(self):
        """
        Формировать (инициилизировать) бочонки в мешке (номера от 1 до 90 включительно)
        """
        super().__init__()
        self.barrel_in_bag = list(range(1, 91))

    def shuffle_barrels(self):
        """
        Перемешиваем все номера
        Изменяет свойство self.barrel_in_bag
        """
        random.shuffle(self.barrel_in_bag)

    def get_barrel(self):
        """
        Вытаскиваем номер, удаляя его из списка номеров.
        Изменяет свойство self.barrel_in_bag
        :return: Выбранный из списка номер
        """
        self.shuffle_barrels()
        barrel_num = self.barrel_in_bag[-1]
        del self.barrel_in_bag[-1]
        return barrel_num

    def print_barrels(self):
        """
        Печатаем (выводим на экран) все номераЮ оставшиеся в мешке
        """
        for i in range(len(self.barrel_in_bag)):
            print((' ' if self.barrel_in_bag[i] < 10 else ''),
                  self.barrel_in_bag[i], sep='', end=' ')
            if (i+1) % 10 == 0:
                print()

    def remaining_barrels_num(self):
        """
        Считаем, сколько бочонков осталось в мешке
        :return: Количество оставшихся в мешке бочонков
        """
        return len(self.barrel_in_bag)

class Card:
    """
    Это карточка с номерами.
    Должна уметь:
    - Формировать (инициилизировать) карточку из 3 строк по 9 ячеек,
      на каждой строке по 5 чисел (номера от 1 до 90 включительно)
    - Отрисовывать карточку на экране
    - Искать по заданному номеру - имеется ли такой номер в карточке
    - Вычёркивать заданный номер, если он имеется в карточке
    - Отмечать в карточке вычеркнутые ячейки, пустые ячейки и ячейки c номерами
      Значения, которые могут находиться в карточке:
      - положительные значения - это номера бочонков.
      - 0 (ноль) это пустая ячейка
      - -1 (минус один) - это ячейка с зачёркнутым числом
    - Проверять, все ли элементы в карточке вычеркнуты
    """
    def __init__(self):
        def create_list(start=1, end=90, num=5, rows=3):
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

        barrel_list = []
        tmp_barrel_list = create_list()  # Создали из 15 элементов список
                                         # номеров в диапазоне [1..90].
                                         # Это числа, которые должны быть в карточке
        for i in range(3):  # Формируем карточку - расставляя пустые ячейки
            tmp_zero_list = create_list(start=1, # Создали из 4 элементов список
                                        end=9,   # номеров в диапазоне [1..9]
                                        num=4,   # Это номера "пустых" ячеек
                                        rows=1)  # В строке 9 ячеек, 5 с числами.
            for j in range(1, 10):   # Формируем строку в карточке - расставляя пустые ячейки
                if j in tmp_zero_list:
                    # Заполняем сгенерированный номер в ячейку карточки
                    barrel_list.append(0)
                else:
                    # Указываем, что ячейка пустая
                    barrel_list.append(tmp_barrel_list[0])
                    del tmp_barrel_list[0]

        self.init_card = barrel_list  # Исходная карточка
        self.card = self.init_card[:] # Текущая карточка. В этой карточке отражаются все ходы

    def get_card(self, sep='  ', init_card=False):
        """
        Метод отрисовывает карточку на экране.
        :param sep: Заполнитель для пустых ячеек (для тех, у которых в списке номер 0)
        :param init_card: Искать в исходной или в текущей карточке
               - True: Искать в исходной карточке (self.init_card)
               - False: Искать в текущей карточке (self.card)
        :return: Кортеж из двух элементов:
               - Карточка, состоящая из нескольких строк.
               - Заполнитель для пустых ячеек
        """
        # Так как заполнитель для пустых ячеек может вводить пользователь,
        # то требуется сформировать заполнитель из двух символов.
        placeholder = (sep[:2] if len(sep) >= 2
                               else (sep * 2 if len(sep) == 1
                                                       else '  '))
        card = self.init_card if init_card else self.card
        line = ''
        for i in range(3):
            for j in range(9):
                if card[j + 9*i] == 0:          # пустая ячейка
                    line += placeholder
                elif card[j + 9*i] == -1:       # зачеркнутая ячейка
                    line += '--'
                elif card[j + 9*i] < 10:        # заполненная ячейка, номером из одного разряда
                    line += ' ' + str(card[j + 9*i])
                else:
                    line += str(card[j + 9*i])  # заполненная ячейка
                line += ' '                     # это разделитель ячеек в карточке
            line += '\n'                        # Перешли на новую строку в карточке
        return (line, placeholder)

    def find_num(self, num, init_card=False):
        """
        Метод ищет по заданному номеру - имеется ли такой номер в карточке.
        :param num: Номер для поиска в карточке
        :param init_card: Искать в исходной или в текущей карточке
               - True: Искать в исходной карточке (self.init_card)
               - False: Искать в текущей карточке (self.card)
        :return: Возвращает:
               - Индекс элемента, если номер найден.
               - -1, если номер отсутствует в карточке.
        """
        if num in (self.init_card if init_card else self.card):
            idx = (self.init_card if init_card else self.card).index(num)
        else:
            idx = -1
        return idx

    def del_num(self, oper_type, num):
        """
        Метод вычёркивает заданный номер, если он имеется в карточке.
        Считается, что номер в карточке ОБЯЗАН!!! присутствовать
        :param oper_type: Тип операции:
                          - 1: Удалить элемент по индексу.
                          - 2: Удалить элемент по значению.
        :param num: Номер для удаления в карточке.
        :return: Ничего не возвращает, если число найдено, то по этому номеру записывает-1
                 Если число для удаления в списке отсутствует, то ничего не делается.
        """
        if oper_type == 2:
            idx = self.find_num(num)
        else:
            idx = num
        if idx != -1:
            self.card[idx] = -1


    def empty_card(self, init_card=False):
        """
        Метод проверяет, есть ли в карточке не вычеркнутые элементы.
        :param init_card: Проверять на пустоту исходную или текущую карточку
               - True: Проверять на пустоту исходную карточку (self.init_card)
               - False: Проверять на пустоту текущую карточку (self.card)
        :return: Возвращает:
               - True: Все элементы в карточке вычеркнуты.
               - False: В карточке имеется ячейка с не вычеркнутым числом.
        """
        # Значения, которые могут находиться в карточке:
        #  - положительные значения - это номера бочонков.
        #  - 0 (ноль) это пустая ячейка
        #  - -1 (минус один) - это ячейка с зачёркнутым числом
        return max(self.init_card if init_card else self.card) <= 0


class Step:
    """
    Это информация о конкретном ходе.
    Имеет свойства:
    - Номер бочонка, вытащенного из мешка (номера от 1 до 90 включительно)
    - Выбранное игроком действие (1 - "зачеркнуть", 0 - "продолжить")
    - Кортеж: номер_столбца_(1..3), номер_строки_(1..9)
      Это номер ячейки в карточке, по которому зачёркивается цифра
    - Ссылка на следующий ход. Тип: class Step
    """
    def __init__(self, barrel_num, player_action, sel_num):
        self.barrel_num = barrel_num        # Номер бочонка.
        self.player_action = player_action  # Выбранное игроком действие
                                            # (1 - "зачеркнуть", 0 - "продолжить").
        self.sel_num = sel_num              # Кортеж: номер ячейки в карточке,
                                            # по которому зачёркивается цифра.
                                            # Может быть значение None, если ход пропускается 
                                            # (то есть, номер в карточке отсутствует).
        self.next_step = None               # Ссылка на следующий ход.

    def str_player_action(self):
        return "зачеркнуть" if self.player_action else "продолжить"


class History:
    """
    Это история ходов.
    Имеет свойства:
    - Корень записи ходов - указатель на самый первый ход в
      истории ходов. Тип: class Step
    - Указатель на последний ход в истории ходов. Нужен для того,
      чтобы не требовалось обходить всю историю для добавления
      хода. Тип: class Step
    Должен уметь:
    - Добавить текущий ход в историю.
    - Выводить историю.
    """
    def __init__(self, player=1):
        self.root = None
        self.last_step = None

    def add_step(self, barrel_num, player_action, sel_num):
        """
        Добавляет текущий ход в историю.
        :param barrel_num: Номер, с которым производится действие.
        :param player_action: Действие игрока: 1 - "зачеркнуть", 0 - "продолжить"
        :param sel_num: Кортеж: номер_столбца_(1..3), номер_строки_(1..9)
                        Это номер ячейки в карточке, по которому зачёркивается цифра.
                        Может быть значение None, если ход пропускается 
                        (то есть, номер в карточке отсутствует).
        :return: Ничего не возвращает, но изменяет свойство self.root и self.last_step,
                 добавляя очередной ход в конец истории
        """
        if self.root is None:
            self.root = Step(barrel_num, player_action, sel_num)
            self.last_step = self.root
        else:
            step = Step(barrel_num, player_action, sel_num)
            self.last_step.next_step = step
            self.last_step = self.last_step.next_step

    def get_history(self):
        """
        Собирает историю действий в одну переменную.
        :return: История действий с переносами строк.
        """
        step = self.root
        i = 0
        result = ''
        while step is not None:
            i += 1
            result += f'Шаг {i}.'
            result += f'   Вытащили из мешка бочонок номер {step.barrel_num}.\n'
            # s = step.str_player_action()
            # action = "зачеркнуть" if step.player_action == 0 else "продолжить"
            # result += f'   Выбрали действие: {action}.\n'
            result += f'   Выбрали действие: {step.str_player_action()}.\n'
            if step.sel_num is not None:
                result += ('   Номер ячейки в карточке, по которому зачёркивается ' +
                           f'цифра (строка, колонка): {step.sel_num}.\n')
            else:
                result += '   Не зачёркивали цифру.\n'
            step = step.next_step
        return result


class Player:
    """
    Это игрок.
    Имеет свойства:
    - Имя игрока.
    - компьютер или обычный игрок. Смысл в том, что если компьютер, то он может
      запросить информацию - имеется ли номер на карточке или не имеется ДО того,
      как выберет опцию зачеркнуть номер
    - Исходная карточка. Это исходная карточка и во время игры не меняется. 
      Карточка хранится только для истории, если историю потребуется записать 
      в файл. Тип: class Card
    - Текущая карточка. Это карточка, в которой отражается каждый ход и она
      показывает итоговое состояние. Тип: class Card
    - История ходов. Тип: class History
    Должен уметь:
    - добавить текущий ход в историю. При этом требуется изменить и содержимое в 
      текущей карточке.
    - Выводить тип игрока.
    - Печатать в консоль карточки игрока (как исходную, так и текущую).
    - Печатать в консоль историю действий игрока.
    - Сохранять в файл историю игры по игроку: информация об игроке (имя и тип),
      исходная и текущая карточки, результат игры (выиграл или проиграл)Ю история ходов.
    - Искать по заданному номеру - имеется ли такой номер в текущей карточке.
    - Вычёркивать заданный номер, если он имеется в текущей карточке.
    - Отмечать в текущей карточке вычеркнутые ячейки, пустые ячейки и ячейки с номерами.
      Это делается:
      - при создании представителя класса (пустые ячейки и ячейки с номерами);
      - при вычёркивании заданного номера (ячейка с зачёркнутым числом).
      Значения, которые могут находиться в карточке:
      - положительные значения - это номера бочонков.
      - 0 (ноль) это пустая ячейка
      - -1 (минус один) - это ячейка с зачёркнутым числом
    - Проверять, все ли элементы вычеркнуты в карточке.
    """

    def __init__(self, name=None, player=1):
        self.player_name = name     # Имя игрока
        self.player_type = player   # 1 - игрок, 0 - компьютер
        # При создании класса Card() появляются две карточки в свойствах:
        # self.init_card и self.card
        # То есть, доступ будет такой:
        #  - self.player_card.card к текущей карточка
        #  - self.player_card.init_card к исходной карточка
        self.player_card = Card()
        self.history = History()

    def get_player_type(self):
        """
        Выводим тип игрока в зависимости от значения в self.player_type.
        1 - игрок, 0 - компьютер.
        :return: Возвращается тип игрока в виде строки
        """
        return 'Тип игрока: ' + ('игрок' if self.player_type else 'компьютер') + '.'

    def print_player_type(self):
        """
        Выводим тип игрока в зависимости от значения в self.player_type.
        1 - игрок, 0 - компьютер.
        :return: Ничего не возвращается
        """
        print(self.get_player_type())

    def add_history(self, barrel_num, player_action, sel_num_idx):
        """
        Добавляет текущий ход в историю.
        :param barrel_num: Номер, с которым производится действие.
        :param player_action: Действие игрока: 1 - "зачеркнуть", 0 - "продолжить"
        :param sel_num_idx: Порядковый номер ячейки в карточке, по которому 
                            зачёркивается цифра. Начинается с нуля.
                            Фактически, это индекс элемента в списке.
                            Может быть значение None, если ход пропускается 
                            (то есть, номер в карточке отсутствует).
        :return: Ничего не возвращает, но изменяет свойство self.history.root и
                 self.history.last_step, добавляя очередной ход в конец истории.
        """
        # Преобразовываем порядковый номер ячейки в кортеж,
        # где счёт начинается с 1, а не с 0.

        if (sel_num_idx is None) or not sel_num_idx:
            # отслеживаем значения None и 0
            sel_num_tpl = None
        else:
            sel_num_tpl = (1 + sel_num_idx // 9, 1 + sel_num_idx % 9)

        # Должны в параметре sel_num передать кортеж:
        # номер_столбца_(1..3), номер_строки_(1..9)
        # Это номер ячейки в карточке, по которому зачёркивается цифра.
        self.history.add_step(barrel_num, player_action, sel_num_tpl)

    def print_history(self):
        history = self.history.get_history()
        print(history)

    def save_history(self, sep='  ',
                     winners=True, result=1,
                     filename='history_json.txt'):
        """
        Сохраняем историю по игроку в файл.
        :param sep: Заполнитель для пустых ячеек (для тех, у которых в списке номер 0)
        :param winners: Показывает наличие победителейц в игре:
                       - True: в игре присутствует победитель
                       - False: игра закончилась, так как кто-то из игроков сделал ошибку.
        :param result: Результат игры:
                       - 1: Игрок выиграл.
                       - -1: Игрок проиграл.
                       -  0: Спорный результат, зависит от значения параметра winners
        :param filename: Имя файла, куда сохранять историю.
        :return: Ничего не возвращает, сохраняет историю в файл.
        """
        if ( (self.player_name is None) or
             (self.player_name == '') ):
            history = 'Имя игрока не задано.\n'
        else:
            history = 'Имя игрока: ' + self.player_name + '.\n'

        history += self.get_player_type() + '\n'

        if result == 1:
            history += 'Игрок выиграл.'
        elif result == -1:
            history += 'Игрок проиграл.'
        else:
            if winners:
                history += ('Считаем, что этот игрок проиграл, так как ' +
                            'другой игрок закрыл всю карточку.')
            else:
                history += ('Несмотря на то, что игрок карточку не закрыл, он ' +
                            'считается выигравшим, так как другой игрок сделал ошибку.')
        history += '\n\n'

        history += '\nИсходная карточка.\n'
        card, sep = self.player_card.get_card(sep, init_card=True)
        history += f'Заполнитель для пустых ячеек обозначается: "{sep}"\n'
        history += 'Зачёркнутая ячейка обозначается: "--"\n'
        history += f'Карточка:\n{card}\n'

        history += '\nИтоговая карточка:\n'
        card, sep = self.player_card.get_card(sep, init_card=False)
        history += f'Заполнитель для пустых ячеек обозначается: "{sep}"\n'
        history += 'Зачёркнутая ячейка обозначается: "--"\n'
        history += f'Карточка:\n{card}\n'

        history += '\nИстория действий игрока:\n'
        history += self.history.get_history()
        # Сохранение в файл
        try:
            # Источник:
            # https://python-school.ru/blog/io-files/?ysclid=l6vzzgh3n4282073634
            # Если текст на русском языке, то можно посмотреть кодировки с поддержкой
            # кириллицы, которые есть в документации Python.
            # Например, явно указать UTF-8 или cp1251:
            # f = open('somefile.txt', encoding='utf-8')
            #
            # f = open('somefile.txt', encoding='cp1251')
            with open(filename, 'w', encoding="utf_8") as f:
                f.write(history)
        except OSError:
            # Исключение OSError - ошибка, связанная с системой.
            # Например, не хватает места на диске.
            print(f'   Произошла ошибка при сохранении истории.')
        else:
            print('   История сохранена в файл')
        # Оператор try: with open('data_files-dirs_json.txt', 'w', encoding="utf_8") as f: закончился

    def print_card(self, sep='  ', init_card=False):
        """
        Метод отрисовывает карточку на экране.
        :param sep: Заполнитель для пустых ячеек (для тех, у которых в списке номер 0)
        :param init_card: Искать в исходной или в текущей карточке
               - True: Искать в исходной карточке (self.init_card)
               - False: Искать в текущей карточке (self.card)
        :return:
        """
        print(self.player_card.get_card(sep, init_card)[0])

    def find_num(self, num, init_card=False):
        """
        Метод ищет по заданному номеру - имеется ли такой номер в карточке.
        :param num: Номер для поиска в карточке
        :param init_card: Искать в исходной или в текущей карточке
               - True: Искать в исходной карточке (self.init_card)
               - False: Искать в текущей карточке (self.card)
        :return: Возвращает:
               - Индекс элемента, если номер найден.
               - -1, если номер отсутствует в карточке.
        """
        return self.player_card.find_num(num, init_card)

    def del_num(self, oper_type, num):
        """
        Метод вычёркивает заданный номер, если он имеется в карточке.
        Считается, что номер в карточке ОБЯЗАН!!! присутствовать
        :param oper_type: Тип операции:
                          - 1: Удалить элемент по индексу.
                          - 2: Удалить элемент по значению.
        :param num: Номер для удаления в карточке.
        :return: Ничего не возвращает, если число найдено, то по этому номеру записывает-1
                 Если число для удаления в списке отсутствует, то ничего не делается.
        """
        self.player_card.del_num(oper_type, num)

    def empty_card(self):
        """
        Метод проверяет, есть ли в текущей карточке не вычеркнутые элементы.
        :return: Возвращает:
               - True: Все элементы в карточке вычеркнуты.
               - False: В карточке имеется ячейка с не вычеркнутым числом.
        """
        # Значения, которые могут находиться в карточке:
        #  - положительные значения - это номера бочонков.
        #  - 0 (ноль) это пустая ячейка
        #  - -1 (минус один) - это ячейка с зачёркнутым числом

        return self.player_card.empty_card()


"""
Алгоритм.

Начальные действия
1.  Запрашиваем у пользователя кто играет. Пользователь указывает типы двух игроков
    Варианты:
    - пользователь
    - компьютер
2.  Инициилизируем карточку для каждого игрока.
3.  Инициилизируем мешок с бочонками

Начало игры.
4.  Мешок встряхивает (перемешивает) номера и выдаёт один номер.
    Выбранный номер удаляется из списка номеров в мешке.
5.  Смотрим тип игрока 1. 
    Если компьютер, то проверяем наличие номера в карточке. При наличии 
    выбранного номера в карточке - номер в карточке зачёркиваем.  
    Если игрок - то выдаётся запрос: "Зачеркнуть цифру ("да" - "д")?"
6.  Смотрим тип игрока 2. 
    Если компьютер, то проверяем наличие номера в карточке. При наличии 
    выбранного номера в карточке - номер в карточке зачёркиваем.  
    Если игрок - то выдаётся запрос: "Зачеркнуть цифру ("да" - "д")?"
7.  Если игрок 1 - пользователь, то проверяем условия:
    - Если игрок выбрал "зачеркнуть":
        Если цифра есть на карточке - она зачеркивается и игра продолжается.
        Если цифры на карточке нет - игрок проигрывает и игра завершается.
    - Если игрок выбрал "продолжить":
        Если цифра есть на карточке - игрок проигрывает и игра завершается.
        Если цифры на карточке нет - игра продолжается.
8.  Записываем в историю действия игрока 1. 
9.  Если игрок 2 - пользователь, то проверяем условия:
    - Если игрок выбрал "зачеркнуть":
        Если цифра есть на карточке - она зачеркивается и игра продолжается.
        Если цифры на карточке нет - игрок проигрывает и игра завершается.
    - Если игрок выбрал "продолжить":
        Если цифра есть на карточке - игрок проигрывает и игра завершается.
        Если цифры на карточке нет - игра продолжается.
10. Записываем в историю действия игрока 2. 
11. Проверяем, что все игроки продолжают игру - то есть, нет проигрыша 
    и/или выигрыша у кого-нибудь из игроков. 
12. Если игра продолжается, то идём на пункт 4.
13. Игра завершилась - записываем историю с файл
"""

# d = Bag()
# d.print_barrels()
# print()
# n = d.get_barrel()
# d.print_barrels()
# print()
# print(n)
# print()
# d.shuffle_barrels()
# d.print_barrels()


# s = Card()
# s.print_card(sep=' ')
# barrel_list = s.init_card
# # print(barrel_list[:9])
# print(barrel_list[9:18])
# print(barrel_list[18:])

# while True:
#     num = int(input('Число для поиска: '))
#     print('индекс:', s.find_num(num))
#     s.del_num(num)
#     s.print_card(sep='  ')
#     print()
#     s.print_card(sep=' ', init_card=True)

# d = Player()
# d.print_player_type()
# # d.add_history(1, 0, (1, 1))
# # d.add_history(2, 0, (2, 2))
# # d.print_history()
# sep='_'
# d.print_card(sep=sep)
# for i in range(1):
#     num = int(input('Число для поиска: '))
#     idx = d.find_num(num)
#     print('индекс:', idx)
#     d.del_num(num)
#     d.print_card(sep=sep)
#     d.add_history(num, d.player_type, (1 + idx // 9, 1 + idx % 9))
#     d.print_history()
#     d.save_history(sep=sep)

"""
Начальные действия
1.  Запрашиваем у пользователя кто играет. Пользователь указывает типы двух игроков
    Варианты:
    - пользователь
    - компьютер
2.  Инициилизируем карточку для каждого игрока.
3.  Инициилизируем мешок с бочонками
"""
print('Внимание!!!')
print('Корректность ввода не проверяется!!!\n')
num_players = int(input(f'Введите количество игроков: '))
# num_players = 2

# players_lst - список игроков, в котором хранятся словари:
# (player, заполнитель, результат_игры):
# - игрок ('player'): это экземпляр класса Player()
# - заполнитель ('sep'): это символ(ы), которыми рисуются пустые ячейки
# - результат_игры ('result')- определяет, что делать после очередного хода.
#   Принимает значения:
#   - -1: Игрок проиграл
#   -  0: Игра продолжается
#   -  1: Игрок выиграл

# В игре может быть только проигравший, если пользователь сделает не правильный ход.
# Для отслеживания победителей и используется переменная winners
winners = False

players_lst = []
for i in range(num_players):
    player_name = input(f'\nВведите имя игрока {i+1} (не обязательно): ').strip(' .,\'"\\|/!@#№$;%:^?&*()-_=+[]{}')
    if player_name == '':
        player_name = 'Имя не задано'
    # 1 - игрок, 0 - компьютер
    # При вводе всё, что может быть преобразовано в False (0, пустая строка) будет
    # преобразовано в False, а затем в ноль.
    sep = input('Введите символы для заполнения пустой ячейки (не более двух): ')
    player_type = 0 if input('Введите тип игрока (0 - компьютер, остальное - игрок): ') == '0' else 1
    players_lst.append({'player': Player(name=player_name, player=player_type),
                        'sep': sep,
                        'result': 0})

bag_of_barrels = Bag()

"""
Начало игры.
4.  Мешок встряхивает (перемешивает) номера и выдаёт один номер.
    Выбранный номер удаляется из списка номеров в мешке.
5.  Смотрим тип игрока 1. 
    Если компьютер, то проверяем наличие номера в карточке. При наличии 
    выбранного номера в карточке - номер в карточке зачёркиваем.  
    Если игрок - то выдаётся запрос: "Зачеркнуть цифру ("да" - "д")?"
"""
print('\nВведите режим выбора бочонков: ручной или автоматический.')
print('В ручном режиме номера бочонков вводятся с клавиатуры.')
print('В автоматическом режиме номера бочонков выбираются случайным образом.')
print('В ручном режиме количество бочонков в мешке не уменьшается.')
manual_control = input('\nВводить номера бочонков "в ручном режиме" ("да" - 1)? ') == '1'

play_game = True
while play_game:
    if manual_control:
        barrel_num = int(input('Номер бочонка: '))
    else:
        bag_of_barrels.shuffle_barrels()
        barrel_num = bag_of_barrels.get_barrel()

    print(f'\n========= Новый бочонок: {barrel_num} (осталось ' +
          f'{bag_of_barrels.remaining_barrels_num()}) =========')

    for i in range(num_players):
        print(f'\nХод игрока {i+1} с именем {players_lst[i]["player"].player_name}.')
        print(f'Вытащили бочонок: {barrel_num}.')
        print('Ваша карточка:')
        players_lst[i]['player'].print_card(sep=players_lst[i]['sep'])
        if players_lst[i]['player'].player_type:
            # 1 - игрок
            # Действие игрока: 1 - "зачеркнуть", 0 - "продолжить"
            player_action = (input(f'Зачеркнуть цифру {barrel_num} ("да" - 1)? ') == '1')
            # player_action = 1 - "зачеркнуть", 0 - "продолжить"
            idx = players_lst[i]['player'].find_num(barrel_num)
            players_lst[i]['player'].add_history(barrel_num, player_action, idx)
            if player_action and (idx >= 0):
                # Зачеркнуть цифру
                # Номер найден в карточке
                # При удалении тип операции:
                #  - 1: Удалить элемент по индексу.
                #  - 2: Удалить элемент по значению.
                players_lst[i]['player'].del_num(1, idx)
                # Проверяем, что все числа зачёркнуты.
                if players_lst[i]['player'].empty_card():
                    players_lst[i]['result'] = 1
                    winners = True
            elif not player_action and (idx == -1):
                # Пропустить ход
                # Номер отсутствует в карточке
                pass
            else:
                # Находимся в ситуации, когда игрок:
                # - выбрал "Зачеркнуть цифру", но номер не найден в карточке
                # - выбрал "Продолжить", но номер найден в карточке
                # В обоих случаях игрок проиграл.
                players_lst[i]['result'] = -1
        else:
            # 0 - компьютер
            # Действие игрока: 1 - "зачеркнуть", 0 - "продолжить"
            # player_action = 1 - "зачеркнуть", 0 - "продолжить"
            idx = players_lst[i]['player'].find_num(barrel_num)
            player_action = (1 if idx >= 0 else 0)
            players_lst[i]['player'].add_history(barrel_num, player_action, idx)
            if idx >= 0:
                # Зачеркнуть цифру
                # Номер найден в карточке
                # При удалении тип операции:
                #  - 1: Удалить элемент по индексу.
                #  - 2: Удалить элемент по значению.
                print(f'Игрок зачёркивает число {barrel_num}')
                players_lst[i]['player'].del_num(1, idx)
                # Проверяем, что все числа зачёркнуты.
                if players_lst[i]['player'].empty_card():
                    players_lst[i]['result'] = 1
                    winners = True
            else:
                print(f'Вынутое число не обнаружено.')

    # После сделанного всеми игроками хода, проверяем статус игроков:
    # есть ли выигравшие или проигравшие. Если есть, то игра заканчивается.
    for i in range(num_players):
        if players_lst[i]['result'] != 0:
            # Какой-то игрок проиграл или выиграл.
            # Завершаем игру.
            play_game = False
            break

print('Итог игры:')

for i in range(num_players):
    print()
    if players_lst[i]['result'] == 1:
        print(f'Выиграл игрок {i+1} с именем {players_lst[i]["player"].player_name}.')
    elif players_lst[i]['result'] == -1:
        print(f'Проиграл игрок {i+1} с именем {players_lst[i]["player"].player_name}.')
    else:
        print(f'Игра закончилась, но карточка не вся закрыта у игрока {i+1} ' +
              f'с именем {players_lst[i]["player"].player_name}.')
        if winners:
            print('Считаем, что этот игрок проиграл, так как другой игрок закрыл всю карточку.')
        else:
            print('Несмотря на то, что игрок карточку не закрыл, он игрок ' +
                  'считается выигравшим, так как другой игрок сделал ошибку.')


# Печатаем историю и сохраняем в файл
for i in range(num_players):
    print(f'\nРезюме по игроку {i + 1} с именем {players_lst[i]["player"].player_name}.')
    if input('Печатать историю в консоль ("да" - 1)? ') == '1':
        players_lst[i]['player'].print_history()
    if input('Сохранять историю в файл ("да" - 1)? ') == '1':
        filename = input('Введите имя файла с историей: ')
        players_lst[i]['player'].save_history(sep=players_lst[i]['sep'],
                                              winners=winners,
                                              result=players_lst[i]['result'],
                                              filename=filename+'.txt')