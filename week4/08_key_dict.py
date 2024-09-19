def main():
    contacts={"Jill":3456, "James":7656, "Somon":6789}
    name="Nishan"
    if name in contacts:
        print(name, "is an extension:", contacts[name])
    else:
        contacts[name]=0

    if name in contacts:
        print(name, "is an extension:", contacts[name])
        print(contacts)
main()