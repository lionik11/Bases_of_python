class Car:
    speed = 0
    color = ''
    name = ''
    is_police = True

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'The {self.name} car is starting')

    def stop(self):
        print(f'The {self.name} car is stopping')

    def turn(self, direction):
        print(f'The {self.name} car is turning to the {direction}')

    def show_speed(self):
        print(f'The {self.name} car goes at a speed of {self.speed} km/h')

    def is_police_car(self):
        if self.is_police:
            print('And your car is police!!! WOW!!!')


class TownCar(Car):
    def hello(self):
        print(f'You choose a town car, called {self.name}!')
        if self.is_police:
            self.is_police_car()

    def show_speed(self):
        if self.speed > 60:
            print(f'The {self.name} goes at a speed of {self.speed} km/h '
                  f'and it exceeded the speed limit, because it is a town car!')
        else:
            print(f'The {self.name} car goes at a speed of {self.speed} km/h')


class SportCar(Car):
    def hello(self):
        print(f'You choose a sport car, called {self.name}!')
        if self.is_police:
            self.is_police_car()


class WorkCar(Car):
    def hello(self):
        print(f'You choose a work car, called {self.name}!')
        if self.is_police:
            self.is_police_car()

    def show_speed(self):
        if self.speed > 40:
            print(f'The {self.name} goes at a speed of {self.speed} km/h '
                  f'and it exceeded the speed limit, because it is a work car!')
        else:
            print(f'The {self.name} goes at a speed of {self.speed} km/h')


class PoliceCar(Car):
    def hello(self):
        if self.is_police:
            print(f'Wow! You choose a police car, called {self.name}!')
        else:
            print(f'Sorry, but your car is not police... '
                  f'Wright in attribute "is_police" - "True" in future if you want.')


print('')
my_car = WorkCar(90, 'blue', 'Mazda', True)
my_car.hello()
my_car.go()
my_car.turn('left')
my_car.show_speed()
my_car.stop()
print('')
my_car = PoliceCar(12, 'blue', 'Horse', False)
my_car.hello()
my_car.go()
my_car.turn('right')
my_car.show_speed()
my_car.stop()
print('')
my_car = TownCar(65, 'white', 'Lada', False)
my_car.hello()
my_car.go()
my_car.turn('75 degree from North')
my_car.show_speed()
my_car.stop()
