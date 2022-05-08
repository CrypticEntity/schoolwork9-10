chickenStripCost = 150
juiceCost = 300
milkCost = 300
pastyCost = 350
toastyCost = 400
waterCost = 200
wrapCost = 450


def sureChecker(): 
    sureCheck = input("Are you sure:")
    if sureCheck == "yes":
        return True
    else:
        return False
                

def updateMoneyVariable():
    moneyFile = open("money", "r")
    money = int(moneyFile.readline())
    moneyFile.close()
    return money


def addMoney():
    money = updateMoneyVariable()

    if money == 0:        
        addMoneyConfirm = input("you don't have any money, you would like to add some:")

    else:    
        addMoneyConfirm = input("You Have $"+ str(money / 100)+ " You would like to add more:")
        if addMoneyConfirm == "no":
            main()

    if addMoneyConfirm == "yes":
        addMoneyAmount = int(input("How Much $:"))
        money += addMoneyAmount * 100       
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
    firstTimeRun = 0
    if firstTimeRun <= 0:
        orderTotal = 0
    firstTimeRun += 1

    money = updateMoneyVariable()
    print("You Have $"+str(money / 100))
    print("What would you like to buy?")
    print("Type number to proceed")
    print("1: Food")
    print("2: Drink")
    menuResponse = int(input("Option:"))
    print("\n\n")
    if menuResponse == 1:
        print("What Food do You Want")
        print("Type Number To Proceed")
        print("1: Chicken Strip, $1.50")
        print("2: Chichen Wrap, $4.50")
        print("3: Pasty, $3.50")
        print("4: Toasty, $4.00")
        menuResponse = input("Option:")
        if menuResponse == 1:
            if sureChecker() == True:
                orderTotal += chickenStripCost


    if menuResponse == 2: 
        print("What Drink do You Want")
        print("Type Number To Proceed")
        print("1: Milk, $3.00")
        print("2: Juice, $3.00")
        print("3: Water, $2.00")
        menuResponse = input("Option:")



def main():
    print("\n\n\n")
    print("Welcome to the Tuckshop")
    print("**********************")
    print("Type number to proceed")
    print("1: Buy Somethin")
    print("2: Add to Balence")
    menuResponse = int(input("Option:"))
    print("\n\n\n")
    
    if menuResponse == 1:
        buySomething()
    if menuResponse == 2:
        addMoney()



if __name__ == '__main__':
    addMoney()
