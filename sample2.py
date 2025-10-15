a=[]
i=0
while(True):
    print("Enter a value")
    Data=int(input())
    a.insert(i,Data)
    i=i+1
    print("Do you wish to continue?")
    print("Press 1:Yes")
    print("Press 2:No")
    choice=int(input())

    if(choice==1):
        continue
    else:
        break
print(a)