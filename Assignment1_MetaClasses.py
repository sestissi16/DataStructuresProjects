#Sari Stissi
#Assignment 1

#https://www.python-course.eu/python3_abstract_classes.php; https://docs.python.org/3/library/abc.html
#-used websites above to learn more about abstract base classes
#Textbook page 85 for how to get make, model, mileage, and price from Car class
#I assume that people will not enter the full weight of the truck so I add the inital weight of the truck to their values
#Asked Shana about whether or not I need set functions for private variables and if I need to add the weight of the truck in myself


from abc import ABCMeta, abstractmethod

class Car(metaclass=ABCMeta):
    #A type of car
    #This would be the parent class for the two specific car classes

    def __init__(self, make, model, mileage, price):
        """Creates a new car instance
            make: make of the car
            model: model of the car
            mileage: mileage of the car
            price: current price of the car
        """
        self._make = make
        self._model = model
        self._mileage = mileage
        self._price = price
        if not isinstance(make, (str)):
            raise TypeError("The make of a car is a string, words/characters with quotes around them")
        if not isinstance(model, (str)):
            raise TypeError("The model of a car is a string, words/characters with quotes around them")
        if not isinstance(mileage, (int or float)):
            raise TypeError("The mileage cannot be a string")
        if not isinstance(price, (int or float)):
            raise TypeError("The price cannot be a string")

    def get_make(self):
        #Return the make of a car
        return self._make

    def get_model(self):
        #Return the model of a car
        return self._model

    def get_mileage(self):
        #Return how much mileage the car has
        return self._mileage

    def get_price(self):
        #Return current price of the car
        return self._price
    
    def set_make(self, newMake):
        #Set a new make for the car
        if not isinstance(newMake, (str)):
            raise TypeError("The make of a car is a string, words/characters with quotes around them")
        self._make = newMake

    def set_model(self, newModel):
        #Set a new model for the car
        if not isinstance(newModel, (str)):
            raise TypeError("The model of a car is a string, words/characters with quotes around them")
        self._model = newModel

    def set_mileage(self, newMileage):
        #set a new mileage for the car
        if not isinstance(newMileage, (int or float)):
            raise TypeError("The mileage cannot be a string")
        self._mileage = newMileage

    def set_price(self, newPrice):
        #set a new price for the car
        if not isinstance(newPrice, (int or float)):
            raise TypeError("The price cannot be a string")
        self._price = newPrice
           
    @abstractmethod
    def drive(miles):
        #abstract method for the subclasses since they each have drive(miles)
        pass
    

class Sedan(Car):
    #An extension of Car that adds a specific sedan

    def __init__(self, make, model, mileage, price, passengers):
        """Creates a new Sedan instance
        Get make, model, mileage, price from car class with super
        initialize passengers:  number of passengers for the current drive
        """
        #Gets stuff from the super class for the car
        super().__init__(make, model, mileage, price)
        #Sets new info for Sedans
        self._passengers = passengers
        if not isinstance(passengers, (int)):
            raise TypeError("The number of passengers cannot be a string or a float")

    def get_passengers(self):
        #Returns the number of passengers for the car
        return self._passengers

    def set_passengers(self, newPassengers):
        #Sets a new number of passengers
        if not isinstance(newPassengers, (int)):
            raise TypeError("The number of passengers cannot be a string or a float")
        self._passengers = newPassengers

    def drive(self, miles):
        #increase the mileage of the car by the specified miles
        self._mileage = self._mileage + miles
        #multiply the miles parameter by the number of passengers
        milesxPass = miles * self._passengers
        #reduce the price by the product above
        self._price = self._price - milesxPass

class Truck(Car):
    #An extension of Car that creates a specific truck instance

    def __init__(self, make, model, mileage, price, load, maxLoad):
        """Creates a new truck instance
        inherits from the car class
        initializes load: the current load of the truck &
                    maxLoad: the maximum allowed load for the truck
        """
        #get make, model, mileage, price from Car class
        super().__init__(make, model, mileage, price)
        #sets new info of load and maxLoad for trucks
        self._load = 500 + load
        self._maxLoad = 500 + maxLoad
        if not isinstance(load, (int or float)):
            raise TypeError("The load cannot be a string")
        if not isinstance(maxLoad, (int or float)):
            raise TypeError("The max load cannot be a string")

    def get_load(self):
        #Returns the load of the truck
        return self._load

    def get_maxLoad(self):
        #Returns the maxLoad of the truck
        return self._maxLoad

    def set_load(self, newLoad):
        #Sets a new load for the truck
        if not isinstance(newLoad, (int or float)):
            raise TypeError("The load cannot be a string")
        self._load = 500 + newLoad

    def set_maxLoad(self, newMaxLoad):
        #Sets a new Maximum load for the truck
        if not isinstance(newMaxLoad, (int or float)):
            raise TypeError("The max load cannot be a string")
        self._maxLoad = newMaxLoad

    def drive(self, miles):
        #increase the mileage by the specified miles
        self._mileage = self._mileage + miles
        #the product of the miles parameter and the load/100
        milesxLoad = miles * (self._load / 100)
        #reduce the price by the product above
        self._price = self._price - milesxLoad


#commented out main block so the professor can run their tests

"""if __name__ == '__main__':

    carSedan = Sedan("Toyota", "Sienna Le", 350000, 20000, 8)
    carTruck = Truck("Ford", "F150", 230687, 40000, 700, 2300)

    print("Sedan things:")
    print("Make: ", carSedan.get_make())
    print("Model: ", carSedan.get_model())
    print("Mileage: ", carSedan.get_mileage())
    print("Price: ", carSedan.get_price())
    print("Passengers: ", carSedan.get_passengers())
    carSedan.drive(1000)
    print("Drive function with 1000 miles: ", carSedan.get_mileage(), ", ", carSedan.get_price())
    print("---------------------------------")
    print("Truck things:")
    print("Make: ", carTruck.get_make())
    print("Model: ", carTruck.get_model())
    print("Mileage: ", carTruck.get_mileage())
    print("Price: ", carTruck.get_price())
    print("Load: ", carTruck.get_load())
    print("Max Load: ", carTruck.get_maxLoad())
    carTruck.drive(1000)
    print("Drive function with 1000 miles: ", carTruck.get_mileage(), ", ", carTruck.get_price())
    print("---------------------------------")"""
    
    
        
        
        

    

    

    

        
        
        

    


