from abc import ABC, abstractmethod
from vehicle import Vehicle
from ride_request import RideRequest
from ride_matching import RideMatching
from ride_sharing import RideSharing

class User(ABC):
    def __init__(self, name, email, nid, intial_amount, location):
        self.name = name
        self.email = email
        self.nid= nid
        self.location= location
        self.__wallet = intial_amount
        self.my_rides = []

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError()

    @abstractmethod
    def updated_location(self):
        raise NotImplementedError()


class Rider(User):
    def __init__(self, name, email, nid, intial_amount, location):
        super().__init__(name, email, nid, intial_amount,location)

    @property
    def balance(self):
        return self._User__wallet

    @balance.setter
    def balance(self, amount):
        self._User__wallet += amount

    def display_profile(self):
        print(self)

    def updated_location(self, new_location):
        self.location = new_location

    def load_cash(self, amount):
        if amount < 0:
            print("Error: Amount can't be negative")
            return

        self.balance = amount
        print(f"Success: Cash added Succesfully, Current Balance: {self.balance}")

    def request_ride(self,ride_sharing, dest_location, vehicle_type, distance):
        ride_request = RideRequest(self,dest_location, distance, vehicle_type)
        ride_matching = RideMatching(ride_sharing.drivers)
        ride = ride_matching.find_driver(ride_request)

        estimated_fare = RideSharing.get_estimated_fare(vehicle_type, distance)

        rem_balance =  self.balance-estimated_fare
        if rem_balance < 0:
            return print(f"Error: Please load some cash, need {abs(rem_balance)} more!")

        ride.start_ride(ride_request)
        ride.end_ride()
        self.my_rides.append(ride)
        ride.driver.my_rides.append(ride)
        ride_sharing.add_ride(ride)

    def my_rides(self):
        for ride in self.my_rides:
            print(ride)


    def __repr__(self):
        profile = f"Rider: {self.name}, Wallet: {self.__wallet}"
        return profile

class Driver(User):
    def __init__(self, name, email, nid, intial_amount, location, vehicle_name, vehicle_type):
        super().__init__(name, email, nid, intial_amount, location)
        
        if RideSharing.check_vehicle_type(vehicle_type) is False:
            raise ValueError(f"{vehicle_type} not allowed")

        self.vehicle = Vehicle(vehicle_name, vehicle_type)

    @property
    def balance(self):
        return self._User__wallet

    @balance.setter
    def balance(self, fare):
        if fare < 0:
            raise ValueError("Fare can't be negative")
        self._User__wallet += fare

    def display_profile(self):
        print(self)

    def updated_location(self, new_location):
        self.location = new_location

    def accept_ride(self,ride):
        ride.set_driver(self)

    def __repr__(self):
        profile = f"Driver: {self.name}, Car: {self.vehicle.vehicle_type},  Wallet: {self.balance}"
        return profile