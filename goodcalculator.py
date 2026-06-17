#simple calculator program that allows user to insert numbers and operations as wanted
class goodCalculator:

    #addition function
    def add(self, num1, num2):
        return num1 + num2

    #subtraction function
    def subtract(self, num1, num2):
        return num1 - num2

    # multiply function
    def multiply(self, num1, num2):
        return num1 * num2

    # division function
    def divide(self, num1, num2):
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2

    # allows user to input number and desired operation
    def calculate(self):
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation // add, subtract, multiply, divide: ")
        num2 = float(input("Enter second number: "))

        if operation == "add":
            print(f"{num1}+{num2}=", self.add(num1, num2))
        elif operation == "subtract":
            print(f"{num1}-{num2}=", self.subtract(num1, num2))
        elif operation == "multiply":
            print(f"{num1}*{num2}=", self.multiply(num1, num2))
        elif operation == "divide":
            print(f"{num1}/{num2}=", self.divide(num1, num2))
        else:
            print("Invalid operation")


if __name__ == "__main__":
    goodCalc = goodCalculator()
    goodCalc.calculate()
