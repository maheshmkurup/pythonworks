class Employee:

    id:int

    name:str

    departmant:str

    salary:str

    def set_employee(self,id,name,department,salary):

        self.id=id

        self.name=name

        self.department=department

        self.salary=salary

    def display(self):

        print(self.id,self.name,self.department,self.salary)

employee_instance1=Employee()

employee_instance2=Employee()

employee_instance1.set_employee(1,"Ajith","Accounts",40000)

employee_instance2.set_employee(2,"Vijay","HR",50000)

employee_instance1.display()

employee_instance2.display()