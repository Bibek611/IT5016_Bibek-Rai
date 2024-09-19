"""
Varaibles can only store one value i.e.; assisgning a new
 value to the variable means you lose the previous value
 Author:Jun Chang
"""
num1=7
num2=3
num3=2
num4=4
num5=num1
num1=num2*num1+4
num2=num5+num2
num5=num3
num3=num4-num3+1
num4=num5

print("final output",num1, num2, num3, num4, num5 )