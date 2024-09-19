
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


            
def staff_info(requisition_id):
    # This function should return the staff ID based on the requisition ID
    # Replace this with your actual logic to get the staff ID
    return "STAFF123"  # Example staff ID
def requisition_approval(total_amount):
     if total_amount < 500:
        status = "Approved"
        approval_reference = f"{staff_id}{str(requisition_id)[-3:]}"
        print(f"Requisition approved automatically.\nApproval Reference Number: {approval_reference}")
     
     else:
        status= "Pending"
        reference = "RN19001."

     return status, reference
     
     
def main():
      """
      The main function is to categorize the status
      and Approval Reference
      """
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


    
   


# Example usage
staff_id = "RN19"
requisition_id = 10000



