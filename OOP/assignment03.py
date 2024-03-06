class Rectangle:
    def __init__(self, base: float, height: float, area: float) -> None:
        self.__base = base
        self.__height = height
        self.__area = area
        
    def get_height(self) -> float:
        return self.__height
    
    def get_base(self) -> float:
        return self.__base
    
    def get_perimeter(self) -> float:
        return 2 * self.__base + 2 * self.__height
    
    def get_area(self) -> float:
        return self.__area
 
 
 
#YOUDO>  create two rectangles.  print their base, height, perimeter, and area
#using only the methods not the fields/property/attributes
Rectangle1 = Rectangle
print("The base of Rectangle1 is", Rectangle1.get_base())
print("The height of Rectangle1 is", Rectangle1.get_height())
print("The perimeter of Rectangle1 is", Rectangle1.get_perimeter())
print("The area of Reactangle1 is", Rectangle1.get_area())

rectangle2 = Rectangle
print("The base of Rectangle1 is", rectangle2.get_base())
print("The height of Rectangle1 is", rectangle2.get_height())
print("The perimeter of Rectangle1 is", rectangle2.get_perimeter())
print("The area of Reactangle1 is", rectangle2.get_area())