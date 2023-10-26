class PetStore:
    def __init__(self):
        self.pets = []

    def store_pet(self, name, species, age, price):
        pet = {"name": name, "species": species, "age": age, "price": price}
        self.pets.append(pet)
        print(f"{name} has been added to the store.")

    def search_pet(self, name):
        for pet in self.pets:
            if pet["name"] == name:
                return pet
        return None

    def sell_pet(self, name):
        pet = self.search_pet(name)
        if pet:
            self.pets.remove(pet)
            print(f"{name} has been sold.")
            return pet
        else:
            print(f"{name} not found in the store. Sale failed.")
            return None

    def list_all_pets(self):
        print("List of all pets:")
        for pet in self.pets:
            print(f"Name: {pet['name']}, Species: {pet['species']}, Age: {pet['age']}, Price: ${pet['price']:.2f}")
