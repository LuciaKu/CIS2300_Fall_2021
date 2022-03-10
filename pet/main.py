import pet
def main():
    pet_name=""
    my_pet_type=""
    pet_age=0
    
    #get info from user
    pet_name=input("Enter the name of your pet:\n")
    my_pet_type=input("Enter the type of your pet:\n")
    pet_age=int(input("Enter the age of your pet:\n"))
    
    #creating the object myPet 
    myPet=pet.Pet(pet_name,my_pet_type,pet_age)
    
    #mutator
    myPet.set_name("Max")
    myPet.set_age(5)
    
    print("Here is the data about the pet that you entered:\n")
    print("Pet name:",myPet.get_name())
    print("Pet animal type:",myPet.get_animal_type())
    print("Pet age:",myPet.get_age())
    
    
main()