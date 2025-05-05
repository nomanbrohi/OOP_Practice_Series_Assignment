class Car():
    brand = "Honda" # Public Variable

    def start(self):    #public_method
        print("The car has Start")

# Create object of class car
car1 = Car()

print("Brand of the car", car1.brand)

# access public method()
car1.start()