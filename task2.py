"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
 Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
 Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
 Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
  толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""
class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def area(self):
        return self._length * self._width

class MassRoad(Road):
    def __init__(self, _length, _width, height, weight):
        super().__init__(_length, _width)
        self.height = height
        self.weight = weight
    def mass(self):
        return self.height *  self.weight
mas = MassRoad(20, 5000, 5, 0.025)
print(mas.area() * mas.mass(), 'тн')
