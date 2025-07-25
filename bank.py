while True:
    print("welcome madhaiyan mini bank")
    print("1-adding your amount")
    print("2-withdrawal amount")
    print("3-checking bank balance")
    print("4- Exite")
    choosing=input("choosing in the number[1-4]")
    balance=0
    if choosing=="1":
        amount=int(input("enter in the amount"))
        balance+=amount
        print("adding amount successfully",amount)
    elif choosing=="2":
        amount=int(input("enter in the amount"))
        if balance>amount:
            balance-=amount
            print(f"withdraw amount successfully{amount}")
        else:
            print("sorry no check balance")
    elif choosing=="3":
        print(f"your balance check successfully{balance}")
    elif choosing=="4":
        print("sorry invalid")
        break

