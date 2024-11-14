class RideSharing:
    fare_map = {
        "cng": 50,
        "car": 80,
        "bike": 40
    }

    vehicle_type = ["cng", "car", "bike"]

    def __init__(self,name, site):
        self.name = name
        self.site = site
        self.drivers = []
        self.riders = []
        self.rides = []

    def add_driver(self, driver):
        self.drivers.append(driver)

    def add_rider(self, rider):
        self.riders.append(rider)

    def add_ride(self, ride):
        self.rides.append(ride)

    @classmethod
    def get_estimated_fare(self,vehicle_type,distance):
        return self.fare_map[vehicle_type]*distance
    
    @classmethod
    def check_vehicle_type(self, vehicle_type):
        if vehicle_type not in self.vehicle_type:
            False
        return True
    
    def __repr__(self):
        return f"Welcome to {self.name}, visit {self.site}"