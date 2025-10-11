class Heroine:
    def __init__(self):
        self.name="Samantha"
        self.age=36
    def act(self):
        print("She is an actress")
h1=Heroine()
print(h1.name)
print(h1.age)
h1.act()
h1.movie ="Citadel"
print(h1.movie)
h1.age=37
print(h1.age)
h2=h1
h3=h2
print(h1.name)
print(h2.name)
print(h3.name)
del h1.age
print(h1.age)