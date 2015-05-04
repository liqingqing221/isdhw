class Dimension:
    def_init_(self,x,y):
        self.x=x
        self.y=y
    def area(self):
        pass
class Ellipse(Dimension):           #定义类 Ellipse
    def_init_(self,a,b):
        Dimension._init_(self,a,b)
    def area(self):                 #椭圆面积
        return 3.14*self.x*self.y

class Square(Dimension):           #定义类Square 
    def_init_(self,c):
        Dimension._init_(self,c,0)
    def area(self):                 #正方形面积
        return self.x*self.x

class Rectangle(Dimension):           #定义类 Rectangle 
    def_init_(self,m,n):
        Dimension._init_(self,m,n)
    def area(self):                 #矩形面积
        return self.x*self.y

class Circle(Dimension):           #定义类Circle
    def_init_(self,r):
        Dimension._init_(self,r,0)
    def area(self):                 #圆面积
        return self.x*self.x

shapes=[Ellipse(10,20),Square(15),Circle(5),Rectangle(20,15),Circle(5),Square(15),Ellipse(10,20)]
total_area=compute_area(shapes)
print(total_area)
