def reverse_string(s):
    reversed_str=""
    for char in s:
        reversed_str=char+reversed_str
    return reversed_str

def main():
    original_string=input("Enter a string:")
    hero=reverse_string(original_string)
    print(f"Original: {original_string}")
    print(f"Reveresed: {hero}")

main()

