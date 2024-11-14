from ride import Ride

class RideMatching():
    def __init__(self, drivers):
        self.drivers = drivers

    def search_driver(self, ride_request):
        pass

    def find_driver(self, ride_request):
        print("Searching for drivers......")

        # nearest_drivers = self.search_driver(ride_request)
        # if len(nearest_drivers) == 0:
        #     print("Sorry! No drivers found near you. Try Later")
        #     return

        # print(self.drivers[0])
        
        driver = self.drivers[0]
        print(f"Yay! Driver: {driver.name} found for your ride")
        ride = Ride()
        driver.accept_ride(ride)
        return ride