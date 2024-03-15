def ger_area(self) -> float:
    return self.__base * self.__height

def __str__(self) -> str:
    #rec
    return "Rectangle with base:" + str(self.__base) + ", height:" +str(self.height)

class Square(Rectangle):
    def __init__(self, side_length:float) -> None:
        super().__init__(side_length, side_length)
        self.__side_length = side_length

    def get_side_length(self) -> float:
        return self.__side_length

    def __str__(self) -> str:
        return "Square with side length:" + str(self.__side_length)

square1 = Square(3)
print(square1)
print("The base of square1 is", square1.get_base())
print("The height of square1 is", square1.get_height())
print("The side length of square1 is", square1.get_side_length())
print("The area of square1 is", square1._get_area())
print("The perimete of square1 is", square1.get_perimeter())
