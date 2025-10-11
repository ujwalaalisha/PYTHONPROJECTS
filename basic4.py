class student():
    def __init__(self):
        self.name="alisha"
        self.age=23
        self.gender="female"
    def study(self):
        print("alisha is studying")
    def notstudy(self):
        print("alisha is not studying")
s1=student()
print(s1.name)
print(s1.age)
print(s1.gender)
s1.study()
s1.notstudy()