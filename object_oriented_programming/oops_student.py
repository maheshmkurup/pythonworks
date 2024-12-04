class Student:

    name:str

    rollno:int

    age:int

    course=str

    def set_Student(self,name,rollno,age,course):

        self.name=name

        self.rollno=rollno

        self.age=age

        self.course=course

    def display(self):

        print(self.name,self.rollno,self.age,self.course)

Student_instance1=Student()

Student_instance2=Student()

Student_instance1.set_Student("Mahesh",17,22,"Python Django")

Student_instance1.display()


#student

#employee

 