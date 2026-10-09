class BankAccount:
    def __init__(self,acc,id):
        self.acc = acc
        self.id = id
        self.balance =  0
    def deposit(self, amount):
            self.balance = self.balance + amount
    def withdraw (self, amount):
            self.balance = self.balance - amount
    def checkBalance(self):
            return self.balance

john = BankAccount(1234,45)

print(john.acc)
print(john.id)

print(john.balance)
print(john.deposit(400))
print(john.withdraw(200))
print(john.checkBalance())


#inheritance

class Vehicle:
      def __init__(self,model, brand, year):#attributes
            self.model = model
            self.brand = brand
            self.year = year
      def forward(self,speed):
            print(f"Car moved ar {speed}kmh {self.model}")

            

class Mercedez(Vehicle): #takes the attributes and method of class Vehicle
      def __init__(self, model, brand, year):
            super().__init__(model, brand, year)
      def forward(self,speed):
            super().forward(speed)
            print("This is from Mercedez")

mycar = Mercedez("Mercedez", 5, 2025)
mycar.forward(5)


    