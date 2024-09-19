name=input("Enter your name")
age=int(input("Enter your age"))
print("Hello", name, ".You are", age, "years old", sep="")
#fstring
print(f"Hello,{name}. you are{age} years old.")

pi=3.141592653589
print(pi)
formatted_pi= f"Value of pi to 2 decimal places:{pi: .2f}"
print(formatted_pi)

salary= float(input("Enter your weekly salary"))
print(f"Your weekly salary is ${salary: .2f}")

a=10
b=5
result=f"The result of {a} multiplied by {b} is {a*b}."
print(result)

name="James"
age=28
address="430 Queen street"
info=f"""
Name:{name}
Age:{age}
Address:{address}
"""

print(info)
