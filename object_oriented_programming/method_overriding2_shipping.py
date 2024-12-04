class Shipping:

    def calculate_shipping_cost(self,weight):

        print(weight*5)

class Expressshipping(Shipping):

    def calculate_shipping_cost(self,weight):

        print(weight*20)

class StandaredShipping(Shipping):

    def calculate_shipping_cost(self,weight):

        print(weight*10)

shipping_instance=Shipping()

shipping_instance.calculate_shipping_cost(10)

express_instance=Expressshipping()

express_instance.calculate_shipping_cost(20)

standared_instance=StandaredShipping()

standared_instance.calculate_shipping_cost(30)

 

