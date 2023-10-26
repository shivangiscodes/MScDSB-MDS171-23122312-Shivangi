from petStore import PetStore

def admin_menu(pet_store):
    while True:
        print("\nAdmin Menu:")
        print("1. Add a new pet")
        print("2. List all pets")
        print("3. Exit")

        admin_choice = input("Enter your choice (1/2/3): ")

        if admin_choice == "1":
            name = input("Enter pet name: ")
            species = input("Enter pet species: ")
            age = input("Enter pet age: ")
            price = float(input("Enter pet price: "))
            pet_store.store_pet(name, species, age, price)

        elif admin_choice == "2":
            pet_store.list_all_pets()

        elif admin_choice == "3":
            print("Exiting Admin Menu.")
            break

        else:
            print("Invalid choice. Please try again.")

def user_menu(pet_store):
    while True:
        print("\nUser Menu:")
        print("1. Search for a pet")
        print("2. Buy a pet")
        print("3. List all pets")
        print("4. Exit")

        user_choice = input("Enter your choice (1/2/3/4): ")

        if user_choice == "1":
            name = input("Enter pet name to search: ")
            pet = pet_store.search_pet(name)
            if pet:
                print(f"Found pet: Name: {pet['name']}, Species: {pet['species']}, Age: {pet['age']}, Price: ${pet['price']:.2f}")
            else:
                print(f"{name} not found in the store.")

        elif user_choice == "2":
            name = input("Enter pet name to buy: ")
            pet = pet_store.sell_pet(name)

        elif user_choice == "3":
            pet_store.list_all_pets()

        elif user_choice == "4":
            print("Exiting User Menu.")
            break

        else:
            print("Invalid choice. Please try again.")

def main():
    pet_store = PetStore()

    while True:
        print("\nPet Store Menu:")
        print("1. Admin")
        print("2. User")
        print("3. Exit")

        menu_choice = input("Enter your choice (1/2/3): ")

        if menu_choice == "1":
            admin_menu(pet_store)
        elif menu_choice == "2":
            user_menu(pet_store)
        elif menu_choice == "3":
            print("Exiting the Pet Store. Thank you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
