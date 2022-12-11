

def update():
    if len(race) == 0:
        print("\nNo Data! Cannot Update.")
    else:
        view()
        print()
        index = int(input("Enter Index that you want to Update: "))
        race[index] = input("Enter New Race: ")
        name[index] = input("Enter New Name: ")
        skills[index] = input("Enter New Skill: ")
        role[index] = input("Enter new Role: ")
        item[index] = input("Enter new Item: ")
        personality[index] = input("Enter new Personality: ")
        print("\nSuccessfully Updated.")

    
menu()
option = int(input("\nEnter choice: "))

while option != 5:
    if option == 1:
        create()
    
    elif option == 2:
        view()
        
    elif option == 3:
        delete()
        
    elif option == 4:
        update()
        
    elif option == 5:
        exit
        
    else:
        print("Invalid Input!")
        
    menu()
    option = int(input("Enter choice: "))

