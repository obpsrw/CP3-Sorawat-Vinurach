class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added to",self.name,self.lastname+"'s Cart")

customer1 = Customer()
customer1.name = "Pob"
customer1.lastname = "Vinurach"
customer1.addCart()

customer2 = Customer()
customer2.name = "Preme"
customer2.lastname = "Ped"
customer2.addCart()

customer3 = Customer()
customer3.name = "Fern"
customer3.lastname = "Naja"
customer3.addCart()