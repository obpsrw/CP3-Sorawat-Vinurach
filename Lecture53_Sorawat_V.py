def vatCal():
    price = float(input("Price : "))
    totalprice = price+(price*(7/100))
    return totalprice
print(vatCal())

