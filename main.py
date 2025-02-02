class Calculator:  
    
    def soma(self, x: float = 0, y: float = 0) -> float: 
        return x + y
    
    def sub(self, x: float = 0, y: float = 0) -> float:
        return x - y
    
    def mult(self, x: float = 0, y: float = 0) -> float:
        return x * y
    
    def div(self, x: float = 0, y: float = 0) -> float:
        if y != 0:  
            return x / y
        else:
            return "Error: Division by zero"

def options() -> None:
    calc = Calculator()
    menu: str = " -- Choose an option --\n 1 - Addition \n 2 - Subtraction\n 3 - Division \n 4 - Multiplication\n 5 - Exit"
    choice: int = 0

    while choice < 5:  
        print(menu)
        choice = int(input())
        result: float = 0

        if choice == 1:
            x: float = float(input("Enter a number: "))
            y: float = float(input("Enter another number: "))
            result = calc.soma(x, y)

            print(f"The addition of both numbers is {result} \n")
        elif choice == 2:
            x: float = float(input("Enter a number: "))
            y: float = float(input("Enter another number: "))
            result = calc.sub(x, y)

            print(f"The subtraction of both numbers is {result} \n")
        elif choice == 3:
            x: float = float(input("Enter a number: "))
            y: float = float(input("Enter another number: "))
            result = calc.div(x, y)

            print(f"The division of both numbers is {result} \n")
        elif choice == 4:
            x: float = float(input("Enter a number: "))
            y: float = float(input("Enter another number: "))
            result = calc.mult(x, y)

            print(f"The multiplication of both numbers is {result} \n")
        else:
            print("Please enter a valid number")

options()
