print(" ----- Hello -----")
user = input("Username : ")
password = input("Password : ")
if user == "admin" and password == "0000":
    print("Login Success!!")
    print(" ---- Welcome to this shop ---- ")
    print("1.Milk 5 THB")
    print("2.Water 10 THB")
    print("3.Beer 30 THB")
    print("4.Tea 20 THB")
    print(" ----- Please select item ----- ")
    select = int(input("Item number : "))
    qty = int(input("Quantity : "))
    if select == 1:
        m = 5
        print(" *** Milk ***")
        print("Total Price =",m*qty,"THB")
    if select == 2:
        n = 10
        print(" *** Water *** ")
        print("Total Price =",n*qty,"THB")
    if select == 3:
        o = 30
        print(" *** Beer ***")
        print("Total Price =",o*qty,"THB")
    if select == 4:
        p = 20
        print(" *** Tea *** ")
        print("Total Price =",p*qty,"THB")
    else:
        print("Invalid selected")
elif user == "admin" and password != "0000":
    print("invalid password")
else:
    print("invalid username")
