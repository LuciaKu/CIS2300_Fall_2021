class Pet:
    def __init__(self,name,animal_type,age):
        self._name=name
        self._animal_type=animal_type
        self._age=age
    
    #mutators (setters)
    def set_name(self,new_name):
        self._name=new_name
    def set_animal_type(self,new_animal_type):
        self._animal_type=new_animal_type
    def set_age(self,new_age):
        self._age=new_age

    #accessors (getters)
    def get_name(self):
        return self._name
    def get_animal_type(self):
        return self._animal_type
    def get_age(self):
        return self._age 
        