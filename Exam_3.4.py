# 4. Создайте класс на тему животных. Используйте статические и динамические переменные,
# дочерний (1 или более) классов на конкретное животное. Публичные и приватные методы.
# Полиморфизм (одинаковые названия методов info в обоих классах, которые выводят информацию о
# животных, либо о конкретном животном данного класса). Создайте объекты каждого класса и обратитесь
# к каждому методу. Напишите один staticmethod, один classmethod, к которым также обратитесь.


class Cat:
    rod = "Koschach'i"
    def_color = 'Black'
    def_weight = '2'

    def __init__(self, color = def_color, weight = def_weight):
        self.color = color
        self.weight = weight

    def sleep(self):
        print('Спит')

    def eat(self):
        print('Ест')

    @staticmethod
    def specifics(color):
        if color == 'White':
            print('Альбинос')
        else:
            print('Обычный окрас')

    @classmethod
    def toy_cat(cls):
        print('Игрушечный кот')

    def info(self):
        print(f'Род: {self.rod} \nОкрас: {self.color} \nВес: {self.weight}кг')

class Wildcat(Cat):
    def __init__(self, areal = 'Лес'):
        super().__init__()
        self.areal = areal

    def like_swimmig(self):
        if self.areal == 'Река' or 'Озеро':
            print("Любит плавать")
        else:
            print('Не любит плавать')

class HomeCat(Cat):
    def __init__(self, name_cat):
        super().__init__()
        self._name_cat = name_cat
        self.__nagradi = 0

    def uchastie_v_vistavke(self):
        self.__nagradi += 1
        return self.__nagradi

    def info(self):
        print(f'Кличка: {self._name_cat} \nОкрас: {self.color} \nВес: {self.weight}кг \nНаграды {self.__nagradi}')


my_cat = Cat()
my_cat = Cat('Red', '5')

Cat.specifics('White') # обращение к статическому методу
my_cat.specifics("Red") # обращение к статическому методу
my_cat.info()

Cat.toy_cat()# обращение к методу класса

my_wildcat = Wildcat('Озеро')
my_wildcat.like_swimmig()

my_home_cat = HomeCat('Барсик')
my_home_cat.uchastie_v_vistavke()
my_home_cat.info()

