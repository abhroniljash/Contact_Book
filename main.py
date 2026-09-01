while True:  
    print("=== Welcome to contact book === ")
    print("1.Add a contact")
    print("2.View all contact")
    print("3.Searching name")
    print("4.exit")

    choise = input("Enter your choise [1/2/3/4]: ")

    if choise == "1":
        name = input("Enter your name: ")
        phoneNum = input("Enter your Phone Number: ")
        with open("contacts.txt","a") as file:
            file.write(name + "," + phoneNum +"\n")
            

    elif choise == "2":
        with open ("contacts.txt","r") as file:
            for line in file:
                name , phone= line.strip().split(",")  #Remove the Newline character from a line , split it using a comma to separate the name and phone number and then store them in two separate variables.
                print("Name: "+name+","+"   "+"Phone Number: "+phone)



    elif choise == "3":
        searchName = input("Enter Searching Name: ").lower()
        found = False
        with open ("contacts.txt","r") as file:
            for line in file:
                stored_name , stored_phone= line.strip().split(",")
                if stored_name.lower() == searchName.lower():
                    print("Name: "+stored_name+","+"   "+"Phone Number: "+stored_phone)
                    found = True
                    break
        if not found:
            print("Contact not found")

             

    elif choise == "4":
        print("Thank you")
        break