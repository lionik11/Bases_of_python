class Stationery:
    title = ''

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        self.title = '"ручка"'
        print(f'Запуск отрисовки интрументом {self.title}')


class Pencil(Stationery):
    def draw(self):
        self.title = '"карандаш"'
        print(f'Запуск отрисовки интрументом {self.title}')


class Handle(Stationery):
    def draw(self):
        self.title = '"карандаш"'
        print(f'Запуск отрисовки интрументом {self.title}')


s = Stationery()
s.draw()

p1 = Pen()
p1.draw()

p2 = Pencil()
p2.draw()

h = Pencil()
h.draw()
