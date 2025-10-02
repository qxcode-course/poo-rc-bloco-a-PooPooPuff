class Car:
    def __init__(self): #Lembrete: essa daqui se chama construtor, os "Parametros" (requisitos de criação) ficam dentro dos parenteses
        self.pas:int=0
        self.gas:int=0
        self.km:int=0
        
    def __str__(self)->str: #Lembrete: essa daqui se chama ToString
        return f"pass: {self.pas}, gas: {self.gas}, km: {self.km}"
    
    def Enter(self):
        if self.pas<2:
            self.pas+=1
        else:
            print("fail: limite de pessoas atingido")
            
    def Leave(self):
        if self.pas>0:
            self.pas-=1
        else:
            print("fail: nao ha ninguem no carro")
    
    def Gas(self, increment:int)->None:
        maxGas=100
        self.gas+=increment
        if self.gas>maxGas:
            self.gas=maxGas
            
def main(): #Lembrete: esse é o main, no qual nós utilizamos pra interagir com o código, o liga/desliga, etc.
    car:Car=Car()
    while True:
        line:str=input()
        print("$"+line)
        args:list[str]=line.split(" ")
        
        if args[0]=="show":
            print(car)
        if args[0]=="end":
            break
        if args[0]=="enter":
            car.Enter()
        if args[0]=="leave":
            car.Leave()
        if args[0]=="fuel":
            increment:int=int(args[1])
            car.Gas(increment)
main()