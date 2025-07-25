balance=0
while True:
    print("welcome my canara bank:)")
    print("1-Adding your amount:)")
    print("2-withdraw amount:)")
    print("3-balance checking:)")
    print("4-Exite")
    choice=input("enter your choice[1-4]")
    if choice=="1":
        amount=float(input("enter your amount:)"))
        balance+=amount
        print("adding your amount successfully",amount)
    elif choice=="2":
        amount=int(input("enter your amount:)"))
        if balance>amount:
            balance-=amount
            print(f"withdraw amount successfully{amount}")
    elif choice=="3":
        print(f"showing amount successfullly{balance}")
    elif choice=="4":
        break
#7:19

balance=0
while True:
    print("welcome to madhaiyan mini bank")
    print("1-adding amount in bank")
    print("2-withdraw amount in bank")
    print("3-balance checking in bank")
    print("4-Exite")
    choice=input("selected your choice in bank list")
    if choice=="1":
        amount=int(input("enter in the amount"))
        balance+=amount
        print("adding in the amount successfullly:)",amount)
    elif choice=="2":
        amount=int(input("enter withdraw amount:)"))
        if balance>amount:
            balance-=amount
            print("withdraw amount successfully:)",amount)
    elif choice=="3":
        print("your current balance",balance)
    elif choice=="4":
        break
        
