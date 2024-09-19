class Car:
    def __init__(self, color, model, year) :
        self.color=color
        self.model=model
        self.year=year
    def drive(self):
        print(f" The {self.color}(self.model) is driving.")
    def stop(self):
        print(f" The {self.color}(self.model) has stopped.")
    def display_info(self):
        print(f"Car Info: {self.year}{self.color}{self.model}")
class ElectricCar(Car):
    def __init__(self, color, model, year, battery_capacity):
        super().__init__(color, model, year)
        self.battery_capacity=battery_capacity
    def display_info(self):
        super().display_info()
        print(f"Battery Capacity:{self.battery_capacity}KWh")
    
    #create an ElectricCar instance
my_electric_car=ElectricCar("White", "Tesla Model3", 2022, 86)
my_electric_car.drive()
my_electric_car.stop()
my_electric_car.display_info()


#Task2:Banking system with Encapsulation
class Account:
    def __init__(self, owner, balance=0):
        self.owner=owner  #Public attribute
        self.__balance=balance  #Private attribute

    def deposit(self, amount):
        if amount>0:
            self.__balance+=amount
            print(f"${amount} deposited.")
        else:
            print("Deposite amount must be positive.")
        
    def withdraw(self, amount):
        if 0<amount<= self.__balance:
            self.__balance-=amount
            print(f"${amount} withdrawn.")
        else:
            print("Insufficient balance or Invalid amount.")
    def get_balance(self):
        return self.__balance
#create an Account Object
account=Account("Kishor", 100)

 #Accessing public attribute
print(account.owner)

#Accessing private attribute(will raise an Attribute error)
#print(account.__balance)

#Using public methods to interact with private data
account.deposit(50)
print(account.get_balance())
account.withdraw(75)
print(account.get_balance())






        
    

