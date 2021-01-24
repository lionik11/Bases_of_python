class Worker:
    name = ''
    surname = ''
    position = ''
    money = {'wage': 0.0, 'bonus': 0.0}
    _income = 0

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self.money['wage'] = float(wage)
        self.money['bonus'] = float(bonus)
        self._income = self.money['wage'] + self.money['bonus']
        self.checking()

    def checking(self):
        if type(self.name) != str or not self.name.isalpha():
            raise ValueError("Вы некорректно ввели имя. Пожалуйста, введите имя в кавычках.")
        if type(self.surname) != str or not self.surname.isalpha():
            raise ValueError("Вы некорректно ввели фамилию. Пожалуйста, введите фамилию в кавычках.")
        if type(self.position) != str:
            raise ValueError("Вы некорректно ввели должность. Пожалуйста, введите должность в кавычках.")
        if not str(self.wage).isdigit():
            raise ValueError("Вы некорректно ввели число. Пожалуйста, введите заработную плату числом.")
        if not str(self.bonus).isdigit():
            raise ValueError("Вы некорректно ввели число. Пожалуйста, введите премию числом.")


class Position(Worker):

    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        return full_name

    def get_total_income(self):
        print(f'Доход сотрудника {self.get_full_name()} равен {self._income}')


t = Position('Игнат', 'Михайлов', 'аналитик', 20000, 5000)
print(t.get_full_name())
t.get_total_income()
