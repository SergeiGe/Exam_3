# Класс Company:
# 1. Создайте класс Company
# 2. Создайте статическое свойство levels, которое будет содержать (как словарь)
#     все уровни квалификации программиста: 1: junior, 2: middle, 3: senior, 4: lead.
# 3. Создайте метод __init__(), внутри которого будут определены два protected свойства:
#     1) _index передается параметром и 2) _levels - принимает из словаря levels значение с ключом _index
# 4. Создайте метод _level_up(), который будет переводить программиста на следующий уровень
# 5. Создайте метод is_lead(), который будет проверять, что программист достиг последней квалификации
#
# Класс Programmer:
# 1. Создайте класс Programmer
# 2. Создайте метод __init__(), внутри которого будут определены три динамических свойства:
#     1) name - передается параметром, является публичным, 2) age - возраст
#     3) level - уровень квалификации на основе словаря из Company
# 3. Создайте метод work(), который заставляет программиста работать, что позволяет ему становиться
#     более квалифицированным с помощью метода _level_up() родительского класса
# 4. Создайте метод info, который выведет информацию о вас: имя, возраст, квалификацию
# 5. Создайте статическое метод knowledge_base(), который выведет в консоль справку по программированию
# (просто любой текст).


class Company:
    levels = {1: 'junior', 2: 'middle', 3: 'senior', 4: 'lead'}

    def __init__(self, index):
        self._index = index
        self._levels = self.levels[self._index]

    def _level_up(self):
        if self._index == 1:
            self._index = 2
        elif self._index == 2:
            self._index = 3
        elif self._index == 3:
            self._index = 4
        return self.levels[self._index]

    def is_lead(self):
        if self._index == 4:
            print('Программист достиг последней квалификации')
        else:
            print('Программист не достиг последней квалификации')

class Programmer(Company):

    def __init__(self, name, age, index):
        self.name = name
        self.age = age
        super().__init__(index)
        self._level = self.levels[self._index]

    def work(self, test):
        self.test = test
        if 90 <= self.test <= 100:
            self._level = self._level_up()
            print(f'Тест сдан, вы перешли на уровень {self._level}')
        else:
            print(f'{self.name} вы не сдали тест')

    def info(self):
        print(self.name, self.age, self._level)

    @staticmethod
    def knowledge_base():
        print('Справка по программированию')


# company = Company()
# company.is_lead()
# programmer = Programmer('Serg', 30, 2)
# programmer.info()
# programmer.work(95)
# programmer.work(80)
# programmer.work(100)
# programmer.work(95)
# programmer.is_lead()
# programmer.info()
# Programmer.knowledge_base()























