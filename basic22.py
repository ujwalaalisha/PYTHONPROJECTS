class Laptop:
    def __init__(self):
        self.brand="hp"
        self.model="victus"
    def start(self):
        print("laptop is starting")
        self.pin="Alisha14"
l1=Laptop()
print(l1.brand)
print(l1.model)
l1.start()
print(l1.pin)
l1.color="silver"
print(l1.color)