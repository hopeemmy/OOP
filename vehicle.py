"""
    Name: vehicle.py
    Author: Hope Ogbonda
    Created: 5/2/25
    Purpose: OOP that models a vehicle
"""

import pygame
import time
from rich.console import Console
from rich.text import Text

# Initializing the mixer
pygame.mixer.init()

# Create a rich Console object for output
console = Console()

# Print title banner 
console.print("=" * 50, style="bold yellow")
console.print("🚗 The Intelligent Ride".center(50), style="bold green")
console.print("A Python OOP Simulation of a Smart Vehicle".center(50), style="italic blue")
console.print("=" * 50, style="bold yellow")
console.print()

def play_sound(sounds):
    pygame.mixer.music.stop()               # Stop anything already playing
    pygame.mixer.music.load(sounds)         # Load the new sound
    pygame.mixer.music.play()               # Play it once
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
        console.print("[cyan]Door opened. Welcome in![/cyan]")
        play_sound("sounds/door_open.mp3")

    # Method to start the engine
    def start_engine(self):
        self.is_engine_on = True                 # Turn the engine on
        console.print(f"[bold green]{self.name}'s engine started[/bold green]")    # Inform the user
        play_sound("sounds/engine_start.mp3")

    # Method to stop the engine
    def stop_engine(self):                         
        self.is_engine_on = False                   # Turn the engine off
        self.speed = 0                              # Reset the speed to 0
        console.print(f"[red]{self.name}'s engine stopped.[/red]")     # Informs the user

    # Method to accelerate the vehicle
    def accelerate(self, speed_increase):
        if self.is_engine_on:
            self.speed += speed_increase
            play_sound("sounds/accelerate.mp3")
            console.print(f"[yellow]{self.name} accelerated. current speed: {self.speed} mph.[/yellow]")  # Show new speed
            
        else:
            console.print("[bold red]Engine is off. Please start the engine first.[/bold red]")


    # Method to brake the vehicle
    def brake(self):
        if self.speed > 0:
            console.print(f"[magenta]{self.name} is braking from {self.speed} mph to a stop. . .[/magenta]")
            play_sound("sounds/brake.mp3")
        else:
            print(f"[bold cyan{self.name} is already stopped.[/bold cyan]")
            
        self.speed = 0
        time.sleep(10)
        console.print(f"[bold green]{self.name} has stopped.[/bold green]")

    
    # Exiting the vehicle
    def exit_vehicle(self):
        console.print(f"[bold blue] You stepped out of the car[/bold blue]")
        time.sleep(1)
        console.print(f"[bold blue]Door closed.[/bold blue]")
        play_sound("sounds/door_open.mp3")

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
time.sleep(1)

# Show menu options after engine starts
while my_vehicle.is_engine_on:
    console.print("\n[bold]Choose an action[bold]")
    console.print("1. Drive")
    console.print("2. Brake")
    console.print("3. Stop Engine and Exit")
    user_choice = input("Enter selection (1/2/3): ")

    if user_choice =="1":
        console.print("[bold green]\nEntering driving mode. . .[bold green]")
        while True:
            user_input = (input("hit the accelerator to acelerate more (or press Enter to brake): ")).strip()

            if user_input == "":
                my_vehicle.brake()
                break                       # Exit driving mode and return to main menu

            try:
                increase = int(user_input)
                my_vehicle.accelerate(increase)

            except ValueError:
                console.print("[bold red]Please enter a valid number or type 'brake'.[/bold red]")
        

    elif user_choice == "2":
        my_vehicle.brake()

    elif user_choice == "3":
        my_vehicle.stop_engine()
        my_vehicle.exit_vehicle()
        break

    else:
        console.print("[bold red]Invalid inout. Try again.[/bold red]")

       