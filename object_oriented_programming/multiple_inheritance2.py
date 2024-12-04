class GrandParent():

    def m(self):

        print("Grandparent class m1 method")

class Parent():

    def m(self):

        print("Parent class m2 method")

class Child(GrandParent,Parent):   #if there are methods of same names then the first class given for inheritance will be taken 

    def m3(self):

        print("Child class m3 method")

child_instance=Child()

child_instance.m3()

child_instance.m()
                     
 

 