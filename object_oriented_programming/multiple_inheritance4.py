class Cusine:

    cusine_name:str

    def __init__(self,cusine_name):

        self.cusine_name=cusine_name

    def display_cusine_info(self):

        print(self.cusine_name)

class MealType:

    mealtypename:str

    def __init__(self,mealtypename):

        self.mealtypename=mealtypename

    def display_mealtype_info(self):

        print(self.mealtypename)

class Dish(Cusine,MealType):

    dishname:str

    def __init__(self,cusine_name,mealtypename,dishname):

        Cusine.__init__(self,cusine_name)

        MealType.__init__(self,mealtypename)

        self.dishname=dishname

    def display_dish_info(self):

        self.display_cusine_info()

        self.display_mealtype_info()

        print(self.dishname)

dish_instance=Dish("Indian","Breakfast","Masala Dosa")

dish_instance.display_dish_info()



    