class Animal:
    def __init__(self,species:str,age:int,sound:str):
        self.species:str=species
        self.age:int=0
        self.sound:str=sound

    def __str__(self)->str:
        return f"{self.species}:{self.age}:{self.sound}"

    def ageBy(self, increment:int)->None:
        self.age+=increment
        
        
    #def 

def main():
    animal:Animal=Animal("",0,"")
    while True:
        line:str=input()
        print("$"+line)
        args:list[str]=line.split(" ")
        
        if args[0]=="end":
            break
        #elif args[0]=="init":
            species:str=args[1]
            age:int=args[2] # type: ignore
            sound:str=args[3]
            animal=Animal(species,age,sound)
        elif args[0]=="show":
            print(animal)

main()