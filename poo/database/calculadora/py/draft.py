class Calculator:
    def __init__(self,batteryMax:int):
        self.batteryMax:int=batteryMax
        self.battery:int=0
        self.display:float=0.0
    
    def __str__(self):
        return (f"display = {self.display:.2f}, battery = {self.battery}")
    
    def Charge(self, increment:int)->None:
        self.battery+=increment
        if self.battery>self.batteryMax:
            self.battery=self.batteryMax
        
def main():
    calculator:Calculator=Calculator("")
    while True:
        line:str=input()
        print("$"+line)
        args:list[str]=line.split(" ")   
        
        if args[0]=="end":
            break
        if args[0]=="init":
            batteryMax:int=int(args[1])
            calculator=Calculator(batteryMax)
        if args[0]=="charge":
            increment:int=int(args[1])
            calculator.Charge(increment)
        if args[0]=="show":
            print(calculator)

main()