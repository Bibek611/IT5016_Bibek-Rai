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


def main():
    """
    Main function to collect the information about staff member submitting the requisition
    """
    requisition_id=10000
    requisition_id=staff_info(requisition_id)

main()
