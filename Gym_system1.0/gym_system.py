import os
import time
def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')




memory = {}




   
class Gym:
    def __init__(self, first_name, last_name, id, status="inactive"):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.status = status


    def display(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"ID: {self.id}")
        print(f"Status: {self.status}")
        print("-" * 30)



    def ask(self):
        self.first_name = input("Enter  first name: ")
        self.last_name = input("Enter  last name: ")
        self.id = input("Enter  ID: ")
        self.status = input("Enter membership status, or click enter to skip: ")


        return Gym(self.first_name, self.last_name, self.id, self.status)


while True:

    print("Welcome to the Gym Membership System!\n")
    print("Please choose an option:")
    print("1. Add a new member")
    print("2. Display all members")
    print("3. Search for a member by ID")
    print("4. Exit\n")
    choice = input("Enter your choice (1-4): ")


    if choice == "1":
        clear_screen()
        user = Gym.ask(Gym)
        memory[user.id] = user
        print("\nMember added successfully!\n")
        time.sleep(3)


    elif choice == "2":
        clear_screen()
        if not memory:
            print("No members found.\n")
        else:
            print("All Members:\n")
            for u in memory.values():
                u.display()
            input("Press enter to contenu:")

    elif choice == "3":
        clear_screen()
        print("Search by:\n")
        print("1. Membership ID:")
        print("2. First name:")
        print("3. Membership Status\n")
        search = input("Enter your choice:")
        if search == "1":
            clear_screen()
            user = input("\nEnter membership ID: ")

            if user  not in memory:
                print("\nThis member is not found, try again")
            

            else:
            #اطبع الاي دي الي هو الاوبيكت الي تم البحث عنه واستدعي داله العرض الي جوا الكائن من غير print
                print("\nyaaa its here\n")
                memory[user].display()
                input("\nPress inter to contenu")

        elif search == "2":
            clear_screen()
            user = input("\nEnter the first name to search: ")
            faund = False
            for i in memory.values():
                if user.lower() == i.first_name.lower():
                    print("\nyaaaa i fouand him....")
                    i.display()
                    faund = True
            if not faund:
                print("\nThe member is not found...")
            input("\nPress inter to contenu")
                    

        elif search == "3":
            clear_screen()
            user = input("\nEnter the status to search (active or inactive): ")
            faund = False
            for i in memory.values():
                if user.lower() == i.status.lower():
                    print("\nyaaaa i fouand him....")
                    i.display()
                    faund = True
                    
            if not faund:
                print("\nThe member is not found...")
            input("\nPress inter to contenu")
                    





        else:
            print("\ninvalid choise...")
            break


            
    elif choice == "4":
        print("\nExiting.......")
        break

    else:
        print("\ninvalid choise")
        break
            


                    



        


    



    


