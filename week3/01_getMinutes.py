def get_minutes(hours, minutes):
    total=hours*60+minutes
    return total

hours=float(input(" Enter hours:"))
minutes=float(input("Enter minutes:"))
total_minutes=get_minutes(hours, minutes)
print("1.", total_minutes, "minutes")

#total_minutes=get_minutes(3,44)
#print("2.", total_minutes, "minutes")

"""another method for calculation of minutes
author:Jun chan
"""
print("3.", get_minutes(11,540), "minutes")

