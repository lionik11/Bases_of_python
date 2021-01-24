import time


class TrafficLight:
    _color = {'red': 7, 'yellow': 2, 'green': 5}

    def red(self):
        print('red')
        time.sleep(self._color['red'])

    def yellow(self):
        print('yellow')
        time.sleep(self._color['yellow'])

    def green(self):
        print('green')
        time.sleep(self._color['green'])

    def running(self):
        color_list = [key for key in self._color]
        color_of_light = color_list[0]
        i = 0
        while i < 10:
            i += 1
            if color_of_light == 'red':
                color_of_light = color_list[1]
                self.red()
            elif color_of_light == 'yellow':
                color_of_light = color_list[2]
                self.yellow()
            else:
                color_of_light = color_list[0]
                self.green()
        print('Stop Traffic Light!')


t = TrafficLight()
t.running()
