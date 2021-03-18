class Sklad:
    max_sklad_count = 100
    sum_count_of_items_on_sklad = 0

    def __init__(self, sklad_name):
        self.sklad_name = sklad_name

    def count_of_items_on_sklad(self):
        print(
            f"На складе занято {self.sum_count_of_items_on_sklad} позиций. "
            f"Осталось {self.max_sklad_count - self.sum_count_of_items_on_sklad} позиций.")

    @classmethod
    def change_sklad_count(cls, change_count, item):
        sum_m = cls.sum_count_of_items_on_sklad + change_count
        if sum_m <= 100:
            cls.sum_count_of_items_on_sklad = sum_m
        else:
            raise SkladIsFull(f"На складе нет места для такого количества {item}.")


class Orgtechnics:
    kind: str
    sklad_division: str
    items_on_sklad = {}

    def __init__(self, brand: str, model: str, count):
        self.brand = brand
        self.model = model
        self.count = count

    def _check_count(self):
        if type(self.count) is str:
            raise CountError("Вы ошиблись при вводе количеста позиций. Введите число в поле для количества позиций")

    def _check_item(self):
        self._check_count()
        k_check_item = self.brand + ' ' + self.model
        if k_check_item in self.items_on_sklad:
            print(f"Объект {k_check_item} есть на складе.")
        else:
            raise NoItem(f"Позиции {k_check_item} нет на складе.")

    def _recieve_item(self):
        try:
            self._check_count()
            print(
                f"{self.kind} модели {self.brand} {self.model} поступил на склад.")
        except CountError as err4:
            print(err4)

    def direct_item(self):
        k_direct_item = self.brand + ' ' + self.model
        self._recieve_item()
        try:
            Sklad.change_sklad_count(self.count, k_direct_item)
            self.items_on_sklad[(self.brand + ' ' + self.model)] = self.count
            print(
                f"{self.kind} модели {k_direct_item} направлен в отделение "
                f"{self.sklad_division} в количестве {self.count} шт.")
        except SkladIsFull as err3:
            print(err3)

    def give_item(self, give_count):
        k = self.brand + ' ' + self.model
        try:
            self._check_item()
            if give_count < self.items_on_sklad[k]:
                self.items_on_sklad[k] -= give_count
                Sklad.sum_count_of_items_on_sklad -= give_count
                print(f"Объект {k} выдан в количестве {give_count} шт. "
                      f"Данной модели оргтехники на складе осталось "
                      f"{self.items_on_sklad[k]} шт.")
            elif give_count == self.items_on_sklad[k]:
                Sklad.sum_count_of_items_on_sklad -= give_count
                print(f"Объект {k} выдан в количестве {give_count} шт. "
                      f"Данной модели оргтехники на складе не осталось.")
                self.items_on_sklad.pop(k)
            else:
                raise MinusValue(f"Вы запросили {give_count} позиций {k}. "
                                 f"Столько оргтехники выдать не получится. "
                                 f"Данной модели осталось всего"
                                 f" {self.items_on_sklad[k]} позиций.")
        except MinusValue as err:
            print(err)
        except NoItem as err1:
            print(err1)
        except CountError as err4:
            print(err4)


class Printer(Orgtechnics):
    kind = "Принтер"
    sklad_division = "О1"


class Scanner(Orgtechnics):
    kind = "Сканер"
    sklad_division = "О2"


class Xerox(Orgtechnics):
    kind = "Ксерокс"
    sklad_division = "О3"


class MinusValue(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


class NoItem(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


class SkladIsFull(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


class CountError(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


s = Sklad("k")
s.count_of_items_on_sklad()
p = Printer("hp", "x90", 10)
s1 = Scanner("hp", "fast scan", 97)
s2 = Scanner("XEROX", "s123", 2)
x = Xerox("XEROX", "x2020", "14")
p.direct_item()
s1.direct_item()
p.give_item(8)
s.count_of_items_on_sklad()
p.give_item(2)
p.give_item(10)
s1.direct_item()
s.count_of_items_on_sklad()
s2.direct_item()
s.count_of_items_on_sklad()
x.give_item(11)
x.direct_item()
