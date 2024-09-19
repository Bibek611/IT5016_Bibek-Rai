name= input("what is your name?:")
birth_date=input("What is your year of birth?:")
 
print(name)
print(birth_date)
birth_date=1996
current_year=2024

age= current_year-birth_date

print(f"Hello {name}, you are now {age} years of old. Wow!!!")

"""Enter the following python
Author=Bibek Rai
"""

a = 42
b = 3.14
c = "Hello, World!"
d = [1, 2, 3]
e = (1, 2, 3)
f = {"name": "John", "age": 30}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

print("="*12)
b=3.14
b_str=str(b)
print(type(b_str))
print(b_str)

print("="*12)
b=3.14
import math
exp_b=math.exp(b)
print(exp_b)

mod_result=a%b
print(mod_result)

a+=5 #Increase the value of a by 5
print(a)
a-=10 #decrease the value of a by 10
print(a)
a*=2 #multiply the value of a by 2
print(a)
a/=7 #divide the value of a by 7
print(a)

#convert c to upper case
c_upper=c.upper()
print(c_upper)

# convert "a" and "b" to str and concatenated them
a_str=str(a)
concatenate=a_str+b_str
print(concatenate)

#Reverse the content of the variable "c"
c_reversed=c[::-1]
print(c_reversed)