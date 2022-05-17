# Truck.py
import datetime

# This class serves to create a truck object to load packages and aid in conforming to constraints(assumptions)
# Big-O(1)
class Trucks():
    # Constructor
    # Big-O(1)
    def __init__(self):
        self.name = ''
        self.max_capacity = 16
        self.cargo = []
        self.avg_speed = 18
        self.mileage = 0
        self.time = datetime.datetime(2021, 1, 1, 1, 1, 1)

    # Calculates miles for truck and returns them
    # Big-O(1)
    def total_miles(self, truck1, truck2):
        total_miles = truck1.mileage + truck2.mileage
        return total_miles
