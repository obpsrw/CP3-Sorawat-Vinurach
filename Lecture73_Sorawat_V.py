systemMenu = {"ข้าวหมกไก่":50,"ข้าวมันไก่":50,"ข้าวหน้าเนื้อ":80}
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
        menuList.append([menuName,systemMenu[menuName]])

showBill()