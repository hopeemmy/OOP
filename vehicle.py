"""
    Name: vehicle.py
    Author: Hope Ogbonda
    Created: 5/2/25
    Purpose: OOP that models a vehicle
"""

# Define a class named vehicle
class Vehicle:
    # Constructor method to initalize the vehichle's atributes
    def __init__(self, name, model_year):
        self.name = name        # Name of the vehicle
        self.model_year = model_year    # Model year of the vehicle
        self.speed = 0                  # Speed of the vehicle starts at 0
        self.is_engine_on = False       # Engine status starts as off
        

    # Method to start the engine
    def start_engine(self):
        self.is_engine_on = True                 # Turn the engine on
        print(f"{self.name}'s engine started")    # Inform the user

    # Method to stop the engine
    def stop_engine(self):                         
        self.is_engine_on = False                   # Turn the engine off
        self.speed = 0                              # Reset the speed to 0
        print(f"{self.name}'s engine stopped.")     # Informs the user



#3. Define four methods:
    # - start_engine: sets is_engine_on to True
    # - stop_engine: sets is_engine_on to False
    #- accelerate: increases speed by a user-defined value
    #- brake: sets speed to 0

#4. Collect user input for vehicle name and model year
vehicle_name = input("Enter the vehicle name: ")
vehicle_year = int(input("Enter the model year: "))

#5. Create an instance of the Vehicle class using the user inputs.
my_vehicle = Vehicle(vehicle_name, vehicle_year)
#6. Use the methods and print the updated vehicle state after each action.
my_vehicle.start_engine()