def main():
    contacts={"Jill":3456, "James":7656, "Somon":6789}
    contacts["Mery"]=8765
    contacts["Jill"]=9089
    contacts["Kyara"]=9089
    name1="Jill"
    name2="Kyara"
    print(name1, "is at extension:", contacts[name1])
    if contacts[name1]==contacts[name2]:
        print(name2, "has the same extension.")
    
    

    print(contacts)

main()