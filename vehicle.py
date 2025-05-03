"""
    Name: vehicle.py
    Author: Hope Ogbonda
    Created: 5/2/25
    Purpose: OOP that models a vehicle
"""

import pygame
import time

# Initializing the mixer
pygame.mixer.init()

# Print title banner 
print("=" * 50)
print("🚗 The Intelligent Ride".center(50))
print("A Python OOP Simulation of a Smart Vehicle".center(50))
print("=" * 50)
print()

def play_sound(car_sounds):
    pygame.mixer.music.load(car_sounds)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    

# Define a class named vehicle
class Vehicle:
    # Constructor method to initalize the vehichle's atributes
    def __init__(self, name, model_year):
        self.name = name        # Name of the vehicle
        self.model_year = model_year    # Model year of the vehicle
        self.speed = 0                  # Speed of the vehicle starts at 0
        self.is_engine_on = False       # Engine status starts as off
        

    def open_door(self):
        print("Door opened. Welcome in!")
        play_sound("door_open.mp3")

    # Method to start the engine
    def start_engine(self):
        self.is_engine_on = True                 # Turn the engine on
        print(f"{self.name}'s engine started")    # Inform the user
        play_sound("engine_start.mp3")

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
            play_sound("accelerate.mp3")
        else:
            print("Engine is off. Please start the engine first.")


    # Method to brake the vehicle
    def brake(self):
        self.speed = 0
        print(f"{self.name} has stopped.")

    
    # Exiting the vehicle
    def exit_vehicle(self):
        print(" You stepped out of the car")
        time.sleep(1)
        print("Door closed.")
        play_sound("door_open.mp3")

#--------------------- MAAIN PROGRAM --------------------------------#
# Collect user input for vehicle name and model year
vehicle_name = input("Enter the vehicle name: ")
vehicle_year = int(input("Enter the model year: "))

# Create an instance of the Vehicle class using the user inputs.
my_vehicle = Vehicle(vehicle_name, vehicle_year)



#Use the methods and print the updated vehicle state after each action
my_vehicle.open_door()
time.sleep(1)

my_vehicle.start_engine()       # Start the engine

# Show menu options after engine starts
while my_vehicle.is_engine_on:
    print("\nChoose an action")
    print("1. Drive")
    print("2. Brake")
    print("3. Stop Engine and Exit")
    user_choice = input("Enter selection (1/2/3): ")

    if user_choice =="1":
        increase = int(input("Enter speed to drive (mph): "))
        my_vehicle.accelerate(increase)
        
    elif user_choice == "2":
        my_vehicle.brake()

    elif user_choice == "3":
        my_vehicle.stop_engine()
        my_vehicle.exit_vehicle()
        break

    else:
        print("Invalid inout. Try again.")

        #my_vehicle.accelerate(30)       # Accelerate by 30 mph
        #my_vehicle.brake()              # Apply brakes
        #my_vehicle.stop_engine()        # Stop the engine


# Add sound to the engine started
# Add sound to the accelerate