"""15Створіть клас, який називається DefaultClass що має атрибути об'єкту name, symbol number . Виведіть атребути.
16Створіть словник з наступними ключами і значеннями: 'name': 'Vasya', 'l_name': 'Pupkin', 'age': 20 . Далі створіть
об'єкт з ім'ям user класу DefaultClass1за допомогою цього словника.
17Для класу DefaultClass1 визначте метод з ім'ям print_info() , що виводить на екран значення атрибутів об'єкта (name ,
l_name та age )."""


class DefaultClass:
    name = "Vasya"
    symbol = 'b'
    number = "45"


class DefaultClass1:
    def __init__(self, attr):
        for k, v in attr.items():
            setattr(self, k, v)

    def print_info(self):
        print(self.__dict__)
        print(self.name)
        print(self.l_name)
        print(self.age)


example1 = DefaultClass()
print("name: {}".format(example1.name))
print("name: {}".format(example1.symbol))
print("name: {}".format(example1.number))

dic = {'name': 'Vasya', 'l_name': 'Pupkin', 'age': 20}
user = DefaultClass1(dic)
user.print_info()
