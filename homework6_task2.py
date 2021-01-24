class Road:
    _length = 20  # метры
    _width = 5000  # метры

    def weight(self, asphalt_density, asphalt_thickness):
        asphalt_weight = self._width * self._length * asphalt_density * asphalt_thickness
        print(f'Масса асфальта равна {asphalt_weight/1000} т')


r = Road()
r.weight(25, 5)
