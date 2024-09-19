def function1(n1,n2,n3):
    sum=n1+n2+n3
    minimum=min(n1,n2,n3)
    return sum-minimum

n1=int(input("number1:"))
n2=int(input("number2:"))
n3=int(input("number3:"))
print("1.", function1(n1,n2,n3))

