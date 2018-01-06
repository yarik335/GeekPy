eimport pprint


def check_arguments(x, y):
    try:
        int(x)
        int(y)
        temp = x * y
        temp = x + y
        temp = x - y
        temp = x / y
    except (TypeError, ValueError):
        print("Error! Maybe you have  entered a line but number is required")
        return True


class Calc:
    """Class which represent Calculator"""

    last_result = None

    def __init__(self):
        """Assign last_result to empty string"""
        self.last_result = ""

    def multiplication(self, a, b):
        """ Multiply two numbers and assign outcome to last_result

        :argument a: digital number
        :argument b: digital  number

        """
        if not check_arguments(a, b):  # check if arguments are numbers
            self.last_result = a * b

    def division(self, a, b):
        """ Divide two numbers and assign outcome to last_result

        :argument a: digital number
        :argument b: digital  number

        """
        if not check_arguments(a, b):  # check if arguments are numbers
            self.last_result = a / b

    def subtraction(self, a, b):
        """ Subtract two numbers and assign outcome to last_result

        :argument a: digital number
        :argument b: digital  number

        """
        if not check_arguments(a, b):  # check if arguments are numbers
            self.last_result = a - b

    def addition(self, a, b):
        """ Add two numbers and assign outcome to last_result

        :argument a: digital number
        :argument b: digital  number

        """
        if not check_arguments(a, b):  # check if arguments are numbers
            self.last_result = a + b


class Person:
    """Class which represent Person"""

    def __init__(self, first_name, last_name, age, gender="male", number_of_children=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.name = first_name.strip() + ' ' + last_name.strip()
        self.gender = gender
        self.number_of_children = number_of_children

    def show_age(self):
        print(self.age)

    def print_name(self):
        print(self.age)

    def show_all_information(self):
        """Print all Person info"""
        return self.__dict__
        # print(self.first_name)
        # print(self.last_name)
        # print(self.age)
        # print(self.name)
        # print(self.gender)
        # print(self.number_of_children)


def main():
    c = Calc()
    c.subtraction(22, 22)
    c.multiplication(22, 22)
    c.division(22, 22)
    c.addition(22, 22)

    p1 = Person("yarik", "mokhurenko", 20, number_of_children=0)
    p2 = Person("vasya", "pupkin", 30, gender="male", number_of_children=5)
    pprint.pprint(p1.show_all_information())
    pprint.pprint(p2.show_all_information())
    p1.profession = "trubadur"
    p2.profession = "noisemaker"
    pprint.pprint(p1.show_all_information())


if __name__ == '__main__':
    main()
