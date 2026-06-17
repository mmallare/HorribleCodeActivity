class BadCalculator:
    def calculate(self, num1, num2, operation):
        if operation == "add":
            result = num1 + num2
            print(result)
            return result
        elif operation == "subtract":
            result = num1 - num2
            print(result)
            return result
        elif operation == "multiply":
            result = num1 * num2
            print(result)
            return result
        elif operation == "divide":
            if num2 == 0:
                print("Cannot divide by zero")
                return 0
            result = num1 / num2
            print(result)
            return result
        else:
            print("Invalid operation")
            return 0

if __name__ == "__main__":
    badCalc = BadCalculator()

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operation = input("Enter operation // add, subtract, multiply, divide: ")
    badCalc.calculate(num1, num2, operation)


