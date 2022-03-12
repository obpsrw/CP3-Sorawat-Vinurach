def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        print("Login Success")
        return True
    else:
        print("Error Login Please Try Again")
        login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")

def menuSelect():
    userSelected = int(input("Please Selected Number : "))
    while userSelected !=1 and userSelected != 2:
        print("Error Login Please Select Again")
        showMenu()
        menuSelect()
        break
    if userSelected == 1:
        totalPrice = int(input("Please Input Total Price : "))
        return vatCalculator(totalPrice)

    elif userSelected == 2:
        loop = int(input("Quantity of item : "))
        totalPrice = 0
        for x in range(loop):
            priceInput = int(input("item "+ str(x+1)+ " Price : "))
            totalPrice += priceInput
        print("Total Price (Exclud. Vat) = "+ str(totalPrice),"THB")
        return priceCalculator(totalPrice)

def vatCalculator(totalPrice):
        result = totalPrice * (7 / 100)
        print("Vat 7% =", result, "THB")
        return result

def priceCalculator(totalPrice):
        totalPV = print("Total Price (Includ. Vat) =",totalPrice + vatCalculator(totalPrice),"THB")
        return totalPV

login()
showMenu()
menuSelect()