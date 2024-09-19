def value_in_cm(inch):
    inch_to_cm=inch*2.54
    return inch_to_cm

inch= int(input("Enter the value in inch:"))
print("1.", value_in_cm(inch), "cm")


def value_in_inch(cm):
    cm_to_inch=cm/2.54
    return cm_to_inch

cm= int(input("Enter the value in cm:"))
print("2.", value_in_inch(cm), "inches")