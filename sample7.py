class Farmer:
    def __init__(self,p,t,r):
        self.principle=p
        self.time=t
        self.rate=r
    def loan(self):
        si=(self.principle*self.time*self.rate)
        print(si)
f1=Farmer(50000,5,2.5)
f2=Farmer(30000,4,2.5)
f1.loan()
f2.loan()