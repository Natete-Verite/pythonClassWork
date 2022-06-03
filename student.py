from unicodedata import name


class Student:
    school = "AkiraChix"
    def __init__(self,name,age,country,first_name,second_name):
        self.name =name
        self.age = age
        self.country = country
        self.first_name = first_name
        self.second_name = second_name
    def greeting(self):
        return f"Hello {self.name} from {self.country} welcome to {self.school}"      
    def full_name(self):
        return f"Hello {self.name}, your full name is {self.first_name} {self.second_name}"
    def year_of_birth(self):
        year = 2022 - self.age
        return f"Hello {self.name}, you were born in {year}"
    def initials(self):
        return f"Hello {self.name}, your initials are {self.first_name[0]}.{self.second_name[0]}"
        


     
                
                
                
                
