tuple1=(3,6,8)
print(tuple1)
print()
tuple2=("abcde", "ghij", "klmno")
print(tuple2)

tuple3=(3,6,8)
print("1.", tuple3[1], tuple3[2], tuple3[0])
print("2.", tuple3[-1], tuple3[-2])
print()
 
tuple4=( tuple3[1], tuple3[2], tuple3[0], 1,7, 9)
print("3.", tuple4)

for element in tuple4:
    if element>3:
        print(element)


