"""Calculate the total wholesale cost for 60 copies
Author:Bibek Rai
"""
cost_of_abook= 24.95
discount =0.40
number_of_copies=60
rate_after_discount = (cost_of_abook - discount*cost_of_abook)

Total_cost_after_discount=(number_of_copies*rate_after_discount)

rate_first_shipping_cost=3
rate_remaining_shipping_cost=0.75
total_shipping_cost= (rate_first_shipping_cost +rate_remaining_shipping_cost*(number_of_copies-1))

Total_Wholesale_cost=(Total_cost_after_discount + total_shipping_cost) 

print("Total_Wholesale_cost is $", Total_Wholesale_cost, sep="")
