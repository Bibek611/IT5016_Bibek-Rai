original_string=input("Enter a string")

reversed_string=""

for char in original_string:
  reversed_string=char+reversed_string

print("Original:", original_string)
print("Reversed:", reversed_string)