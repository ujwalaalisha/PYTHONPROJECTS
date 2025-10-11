class Calci:
    def __init__(self):
        self.brand="casio"
        self.color="black"
    def add(self,a,b):
       c=a+b
       return c
c1=Calci()
print(c1.brand)
x=10
y=20
res=c1.add(x,y)
print(res)