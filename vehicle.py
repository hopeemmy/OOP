"""
    Name: vehicle.py
    Author: Hope Ogbonda
    Created: 5/2/25
    Purpose: OOP that models a vehicle
"""


# Print title banner 
print("=" * 50)
print("🚗 The Intelligent Ride".center(50))
print("A Python OOP Simulation of a Smart Vehicle".center(50))
print("=" * 50) #+ '\n' )
print()

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

    # Method to accelerate the vehicle
    def accelerate(self, speed_increase):
        if self.is_engine_on:
            self.speed += speed_increase
            print(f"{self.name} accelerated to {self.speed} mph.")  # Show new speed
        else:
            print("Engine is off. Please start the engine first.")


    # Method to brake the vehicle
    def brake(self):
        self.speed = 0
        print(f"{self.name} has stopped.")


#4. Collect user input for vehicle name and model year
vehicle_name = input("Enter the vehicle name: ")
vehicle_year = int(input("Enter the model year: "))

# Create an instance of the Vehicle class using the user inputs.
my_vehicle = Vehicle(vehicle_name, vehicle_year)

#Use the methods and print the updated vehicle state after each action.
my_vehicle.start_engine()       # Start the engine
my_vehicle.accelerate(30)       # Accelerate by 30 mph
my_vehicle.brake()              # Apply brakes
my_vehicle.stop_engine()        # Stop the engine


# Add sound to the engine started
# Add sound to the accelerate