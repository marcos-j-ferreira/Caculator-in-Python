class Caculator: 
    
    def soma(self, x:float = 0, y:float = 0) -> int:
        return x + y
    
    def sub(self, x:float = 0, y:float = 0) -> float:
        return x - y
    
    def mult(self, x:float = 0, y:float = 0) -> float:
        return x * y
    
    def div(self, x:float = 0, y:float = 0) -> float:
        if x != 0:
            return x / y
        else:
            return "Error in Division"

def options() -> None:

    cal = Caculator()
    ope:str = " -- Chose a option --\n 1 - Soma \n 2 - Sub\n 3 - Div \n 4 - Mult\n 5 - exit"
    a:int = 0

    while a < 5:

        print(ope)
        a = int(input())
        result:float = 0

        if a == 1:
            x:float = float(input("Enter a number: "))
            y:float = float(input("Enter other number: "))
            result = cal.soma(x,y)

            print(f"A soma de ambos os números é {result} \n")
        elif a == 2:
            x:float = float(input("Enter a number: "))
            y:float = float(input("Enter other number: "))
            result = cal.sub(x,y)

            print(f"A subtração de ambos os números é: {result} \n")
        elif a == 3:
            x:float = float(input("Enter a number: "))
            y:float = float(input("Enter other number: "))
            result = cal.div(x,y)

            print(f"A multiplicação de ambos os números é {result} \n")
        elif a == 4:
            x:float = float(input("Enter a number: "))
            y:float = float(input("Enter other number: "))
            result = cal.mult(x,y)

            print(f"A divisão de ambos os números é {result} \n")
        else:
            print("Digite um número válido")
options()