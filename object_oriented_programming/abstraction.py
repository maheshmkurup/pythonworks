from abc import ABC,abstractmethod

class Bike(ABC):

    @abstractmethod

    def start(self):

        pass

    @abstractmethod

    def accelerate(self):

        pass

    @abstractmethod

    def stop(self):

        pass

class Hunter(Bike):

    def start(self):

        print("Hunter start method")

    def accelerate(self):

        print("Hunter accelerate method")

    def stop(self):

        print("Hunter stop method")

hunter_instance=Hunter()

hunter_instance.start()

hunter_instance.accelerate()

hunter_instance.stop()
