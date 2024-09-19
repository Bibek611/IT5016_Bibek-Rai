class Person():
    #constructor
    def __init__(self, name, gender) :
        self.name=name
        self.nage=10
        self.gender=gender

    def speaks(self):
        quote=input(f"What does the {self.name} say?:")
        print(quote)

    #object
person1=Person("Rashid", "male")
person2=Person("Kanchan", "Female")

person1.speaks()
    