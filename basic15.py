class Mobile:
    def __init__(self):
        self.brand="Vivo"
        self.color="Blue"
    def disp(self):
        print("display is broken")
        print(self.color)
        print(self)
m1=Mobile()
print(m1.brand)
print(m1.color)
m1.disp()
print(m1)


