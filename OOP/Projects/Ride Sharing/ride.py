
from datetime import datetime
from ride_sharing import RideSharing

class Ride:
    counter = 1
    def __init__(self):
        self.ride_id = self.counter
        self.start_location  = None
        self.end_location = None
        self.start_time = None
        self.end_time = None
        self.rider = None
        self.driver = None
        self.estimated_fare = 0
        self.distance = 0
        self.counter += 1

    def set_driver(self, driver):
        self.driver = driver

    def start_ride(self, ride_request):
        self.rider = ride_request.rider
        self.start_time = datetime.now()
        self.estimated_fare = RideSharing.get_estimated_fare(ride_request.vehicle_type ,ride_request.distance)
        self.start_location = ride_request.rider.location
        self.end_location = ride_request.dest_location
        self.distance = ride_request.distance

    def end_ride(self):
        self.rider.balance = -self.estimated_fare
        self.driver.balance = self.estimated_fare
        self.end_time = datetime.now()

    def __repr__(self):
        print(f"Ride Id: {self.ride_id}")
        print(f"Start Location: {self.start_location}, End Location: {self.end_location}")
        print(f"Start Time: {self.start_time}, End Time: {self.end_time}")
        print(f"Driver: {self.driver.name} Rider: {self.rider.name}")
        print(f"Estimated Fare: {self.estimated_fare}")
        print(f"Distance: {self.distance}km")
        return ""