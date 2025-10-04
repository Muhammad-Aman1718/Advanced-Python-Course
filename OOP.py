class Car:
    # Default Constructor

    def __init__(self) -> None:
        print("this is constructor  ")
        self.color = "Green"

    def fun(self, color: str):
        self.color = color
    @staticmethod
    def mixc(num:int):
        
        


objCar1 = Car()
objCar2 = Car()
objCar3 = Car()
objCar4 = Car()
print(objCar1.color)
print(objCar2.color)
print(objCar3.color)
print(objCar4.color)

objCar1.fun()
objCar1.mixc()


