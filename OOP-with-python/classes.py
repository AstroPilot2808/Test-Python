class Student:
    # The self variable is needed in the method header for any method inside a class because that is how you 
    # refer to the current object. Where else would you store name and house?
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Name is null")
        
        # This if statement is actually redundant.
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Not a valid house")
        self.name = name 

        # Since house variable has a setter, there is no point in including another if statement to validate house. 
        # Because in the line below, when self.house = house statement is ran, it will again automatically call the setter method.

        # here we do NOT refer to house as _house because we deliberately want to match the variables name 
        # in such a way so that python calls the setter method, rather than directly setting the variable
        self.house = house
        self.patronus = patronus
    
    # str method will override the default method. Defaulty, if you print a student object, 
    # it will print out the hexdecimal object. However, now it will print out what you return
    def __str__(self):
        return f"{self.name} is from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "horse"
            case "Otter":
                return "moo"
            case "Jack Russell terrier":
                return "woof woof"
            case _:
                return "/"
            
    #Getter (property lets python know that house is a property)
    @property
    def house(self):
        # _house is necessary rather than house. This is because we can't have both the instance variable, AND the method name to be the same. That is confusing to python.
        return self._house
    
    #Setter (house.setter lets python know that this function is a setter for the instance variable "house")
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name is null")
        self._name = name

def main(): 
    student = get_student()

    # Unlike java, python does not have a way to make a variable private, so the convention is that if a variable has an underscore, you are not suppose to directly manipulate it
    # however, there is nothing actually stopping you from doing student._house = "blahblah"
    print("Expecto Patronum!")
    
    # In python, if you have a setter for a field, python automatically calls the setter function, 
    # therefore disallowing to mutate the instance variable directly
    # student.house = "Goo Goo Garbage"
    print(student.charm())

def get_student(): 
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()

# int, str, list, dict are all classes