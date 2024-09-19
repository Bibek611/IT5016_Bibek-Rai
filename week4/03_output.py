#def show_output():
   # number=1
    #count=10
    #value=4

    #while count>4:
       # count=count-2
       # print(str(number)+":", count, value)
       # value+=count
        #number+=1
    
    #print()
   # print(str(number)+":", count, value)

#def main():
    #show_output()
#main()

def show_output():
    total=0
    for number in range(9,20):
        if number%2==0 or number%3==0:
            total+=1
        print(total)
def main():
    show_output()
main()






