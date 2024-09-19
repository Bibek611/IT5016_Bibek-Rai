def bmi (weight, height):
    bmi= weight/(height/100)**2
    return bmi

weight= float(input("Enter your weight:"))
height= float(input("Enter your height:"))

print(bmi(weight,height))