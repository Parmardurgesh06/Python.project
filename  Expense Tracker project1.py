#Expense Tracker project

expenses = []
print("Welcome to Expense Tracker : ")

while True:
    print("====MENU====")
    print("1.Add Expense")
    print("2.View all Expense")
    print("3.View Total spent")
    print("4.Exit")

    choice = int(input("Enter your choice:-"))
    if(choice==1):
        date=input("kis date par karcha iya tha?:-")
        category=input("What type of spent is there?:- ")
        description=input("Give more information:-")
        amount=float(input("Enter the amount="))

        expense={
            "date": date,
            "category": category,
            "description": description,
            "amount": amount

        }
        expenses.append(expense)
        print("Expense is added successfully")

    elif(choice==2):
            if(len(expenses)==0):
                print("NO Expense addded. Phela karcho karo")
            else:
                print("===Ye aapka sara Expense===")
                count=1
                for e in expenses:
                    print(f"Kharcha Number{count}-> {e["date"]},{e["category"]},{e["description"]},{e["amount"]}")
                    count+=1

    elif(choice==3):
        total=0
        for eh in expenses:
            total=total+e["amount"]
            print("/nTotal kharcha=",total)


    elif(choice==4):
         print("Thanks for using our system")
         break
    else:
         print("Invalid choice")
         print("Try again")
            





