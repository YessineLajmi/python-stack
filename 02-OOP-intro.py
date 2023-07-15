# ? OOP : object oriented programing

class Student:
    school="MIT"
    def __init__(self,first_name, last_name,age,marks,fav_number) :
        #instance attributes ---------values
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.marks=marks
        self.fav_number=fav_number
    def increase_age(self,):
        
        print(self.first_name,self.age,self.last_name,self.marks)
        print("befor",self.age)
        
        print("after",)

        return None
yessine = Student("yessine","lajmi",20,[12,35,80.9],15)
alex = Student("alex","mixi",40,[12,35,80.9],15)
ahmed = Student("ahmed","jouni",50,[12,35,80.9],15)
"""print("***********",yessine,"**********")   
print(f"FN: {yessine.first_name}\nLN:{yessine.last_name}")
    """
print(yessine.school)