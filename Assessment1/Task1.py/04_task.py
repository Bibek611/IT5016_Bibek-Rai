"""
A Python function is created  
Author: Bibek Rai
"""
def staff_info(requisition_id):
    date=input("Enter the date:")
    staff_id=str(input("Enter the staff's ID:"))
    name=input("Enter staff's name:")

    unique_id=requisition_id+1 # a Unique ID is generated
    requisition_id=unique_id
  


# Output function for printing Staff Information
    print(f"\n Staff Information:")
    print(f" Date:{date}")
    print(f"Staff's ID:{staff_id}")
    print(f"Staff's Name:{name}")
    print(f"Staff's Unique ID:{unique_id}")
    
    return unique_id, requisition_id, date, staff_id,name



"""Sum of the prices of the following items!"""



def requisition_total():
    shopping_list=[]#it is a list that stores values
    total_amount=0
    while True:
        item=input("Enter the name of the item(or type 'done' to finish):")
        if item.lower()=='done':
            break
        try:
            price=float(input(f"Enter the price of '{item}':"))
            shopping_list.append((item,price))
            total_amount+=price
        except ValueError:
            print("Invalid input. please enter a numeric value for the price.")
    return shopping_list, total_amount
def main():
    print(" welcome to the shopping list program")
    shopping_list, total_amount=requisition_total()

def requisition_approval(total_amount):
     if total_amount < 500:
        status = "Approved"
        reference  = "RN19001"
     
     else:
        status= "Pending"
        reference = "RN19001."

     return status, reference

 
    
def main():
    requisition_id=10000
    unique_id, requisition_id, date, staff_id,name=staff_info(requisition_id)
    shopping_list, total_amount=requisition_total()
    status, reference=requisition_approval(total_amount)

    if not shopping_list:
        print("No items were enetred")
    else:
        print("\nShopping list:")
        for item, price in shopping_list:
            print(f"{item}, ${price:.2f}")
        print(f"\nTotal price: ${total_amount:.2f}")
        print(f"Status: {status}")
        print(f"Reference: { reference}")

main()




