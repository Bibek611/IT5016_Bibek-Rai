"""
Calculate the radius of  a circle, given the area
Author=Bibek Rai
"""
import math
area=float(input("Enter the area value:")) #input area value
radius=math.sqrt(area/math.pi)
print("Radius of a circle", radius)