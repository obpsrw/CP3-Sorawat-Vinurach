num = int(input("Please input number : "))
for x in range(num):
    y = (x*2)
    print(" "*(num-x) + "*"*(y+1))