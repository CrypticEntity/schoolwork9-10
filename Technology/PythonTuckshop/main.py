def addMoney():
    moneyFile = open("money", "r")
    money = int(moneyFile.readline())
    moneyFile.close()
    
    if money == 0:        
        addMoneyConfirm = input("you don't have any money, you would like to add some:")

    else:    
        addMoneyConfirm = input("You Have $"+ str(money)+ " You would like to add more:")
        if addMoneyConfirm == "no":
            main()

    if addMoneyConfirm == "yes":
        addMoneyAmount = int(input("How Much:"))
        money = money + addMoneyAmount
        
        moneyFile = open("money", "w")
        moneyFile.writelines(str(money))
        moneyFile.close()
        main()
    
    else:
        print("did not understand, type yes or no")
        returnToMain = input("Would you like to return to main menu")
        if returnToMain == "no":
            addMoney()
        else:
            main()
        
def buySomething():
    print("What would you like to buy?")
     

def main():

    print("\n \n \n")
    print("Welcome to the Tuckshop")
    print("**********************")
    print("Type number to proceed")
    print("1: Buy Somethin")
    print("2: Add to Balence")
    menuResponse = input("Option:")
    
    print("\n \n \n")
    if menuResponse == 2:
        addMoney()
    if menuResponse == 1:
        buySomething()



addMoney()
main()


