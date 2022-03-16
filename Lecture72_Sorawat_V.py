menuList = []

def showBill():
    print("======= My Shop ======= ")
    totalP = 0
    for i in range(len(menuList)):
        print(str(i+1)+".",menuList[i],"THB")
        totalP += menuList[i][1]
    print("======================= ")
    print("Total Price =",totalP, "THB")

while True:
    menuName = input("Please Enter Menu (or Exit) : ")
    if menuName.lower() == "exit":
        break
    else :
        menuPrice = int(input("Price : "))
        menuList.append([menuName,menuPrice])

showBill()