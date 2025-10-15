import copy
L=[10,20,30,["Mdanja","Manjula"],40,50]
print(L)
L1=copy.deepcopy(L)
print(L)
print(L1)
del L[3][1]
print(L)
print(L1)
