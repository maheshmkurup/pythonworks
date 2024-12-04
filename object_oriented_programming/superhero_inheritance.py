class SuperHero:

    name:str

    suit:str

    def __init__(self,name,suit):

        self.name=name

        self.suit=suit

    def __str__(self):

        return self.name
    
class Spiderman(SuperHero):

    def __init__(self,name,suit):

        super().__init__(name,suit)

    def superpower(self):

        print("webshooting","wall-crawling ability,spider-sense")

spiderman_instance=Spiderman("Spiderman","Spider suit")

print(spiderman_instance)

spiderman_instance.superpower()

class MinnalMurali(SuperHero):

    def __init__(self,name,suit):

        super().__init__(name,suit)

    def superpower(self):

        print("strength","speed","Quick reflexes")

minnalmurali_instance=MinnalMurali("MinnalMurali","minnal_murali suit")

print(minnalmurali_instance)

minnalmurali_instance.superpower()
