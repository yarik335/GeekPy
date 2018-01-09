import pprint


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

    def show_last_operation(self):
        with open("results.txt", 'r')as f:
            for line in f:
                pass
            print(line)
            f.close()

    def clear_all_results(self):
        with open("results.txt", 'w')as f:
            f.write("")
            f.close()

    def multiplication(self, a, b):
        """ Multiply two numbers and assign outcome to last_result

        :argument a: digital number
        :argument b: digital  number

        """
        if not check_arguments(a, b):  # check if arguments are numbers
            self.last_result = a * b
            with open("results.txt", 'a')as f:
                f.write("a*b=" + str(self.last_result) + "\n")
                f.close()

    def division(self, a, b):
        """ Divide two numbers and assign outcome to last_result

        :argument a: digital number
        :argument b: digital  number

        """
        if not check_arguments(a, b):  # check if arguments are numbers
            self.last_result = a / b
            with open("results.txt", 'a')as f:
                f.write("a/b=" + str(self.last_result) + "\n")
                f.close()

    def subtraction(self, a, b):
        """ Subtract two numbers and assign outcome to last_result

        :argument a: digital number
        :argument b: digital  number

        """
        if not check_arguments(a, b):  # check if arguments are numbers
            self.last_result = a - b
            with open("results.txt", 'a')as f:
                f.write("a-b=" + str(self.last_result) + "\n")
                f.close()

    def addition(self, a, b):
        """ Add two numbers and assign outcome to last_result

        :argument a: digital number
        :argument b: digital  number

        """
        if not check_arguments(a, b):  # check if arguments are numbers
            self.last_result = a + b
            with open("results.txt", 'a')as f:
                f.write("a+b=" + str(self.last_result) + "\n")
                f.close()


def main():
    c = Calc()
    c.subtraction(2, 22)
    c.multiplication(22, 22)
    c.division(22, 22)
    c.addition(22, 22)
    c.addition(22, 22)
    c.division(22, 22)
    c.show_last_operation()
    c.clear_all_results()



if __name__ == '__main__':
    main()
