menuList = []
priceList = []

def showBill():
    print("======= My Shop ======= ")
    sump = 0
    for i in range(len(menuList)):
        print(str(i+1)+".",menuList[i],priceList[i],"THB")
        sump += float(priceList[i])
    print("======================= ")
    print("Total Price (exclud. Vat) =",sump,"THB")
    vat = float(sump*7/100)
    print("Vat 7% =",vat,"THB")
    print("Total Price (includ. Vat) =",sump+vat,"THB")
    print("======================= ")

while True:
    menuName = input("Please Enter Menu (or exit) : ")
    if menuName.lower() == "exit":
        break
    else :
        menuPrice = int(input("Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)
showBill()
