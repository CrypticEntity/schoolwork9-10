def addMoney():
    moneyFile = open("money", "r")
    money = int(moneyFile.readline())

    
    if money == 0:        
        addMoneyConfirm = input("you don't have any money, you would like to add some:")

    else:    
        addMoneyConfirm = input("You Have $"+ str(money)+ " You would like to add more:")

    if addMoneyConfirm == "yes":
        addMoneyAmount = int(input("How Much:"))
        money = money + addMoneyAmount
        main()
    
    else:
        print("did not understand, type yes or no")
        returnToMain = input("Would you like to return to main menu")
        if returnToMain == "no":
            addMoney()
        else:
            main()
        


def main():
    print("Welcome to the Tuckshop, you would like by something:")
    print("**********************")
    print("Type number to proceed")
    print("1: Buy Somethin")
    print("2: Add to Balence")
    menuReponse = input("Option:")
    
    if menuReponse == 1:
        buyMenu()
    if menuResponse == 2:
        addMoney()




addMoney()
main()


