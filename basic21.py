import time
password=1234
Balance=10000
print("Welcome to pentagon space bank")
print("insert your card:")
print("1.Yes 2.No")
choice=int(input())
if choice==1:
    print("enter your pin ")
    pin=int(input())
    if pin==password:
        print("Select the language")
        print("1.English 2.Kannada 3.Hindi")
        lang=int(input())
        if lang==1:
            print("select the option")
            print("1.balance enq 2.withdrawal")
            choice1=int(input())
            if choice1==1:
                print("your available balance is",Balance)
            elif choice1==2:
                print("enter the amount to be withdrawed")
                amt=int(input())
                if amt%100==0 and amt<Balance:
                    print("Your transaction is processing")
                    time.sleep(5)
                    print("please collect your cash")
                    time.sleep(3)
                    print("Do you want to check your balance")
                    print("1.yes 2.no")
                    choice2=int(input())
                    if choice2==1:
                        print("your available balance is",Balance-amt)
                        print("thank you visit again")
                    else:
                        print("thank you visit again")
                else:
                        print("Invalid amount")

            else:
                print("select the correct option")
        else:
            print("Please select only english")

    else:
        print("wrong pin")
else:
    print("please insert your card properly")









