
from user import Rider, Driver
from ride_sharing import RideSharing


niye_jao = RideSharing("Niye Jou", "www.niye_jou.com")

rider = Rider("Rider", "rider@gmail", 3242342, 0, 'Dhaka')
driver = Driver("Driver", "driver@gmail", 3242342, 0, 'Dhaka', "R15", "bike")

niye_jao.add_driver(driver)
niye_jao.add_rider(rider)

rider.load_cash(500)
rider.request_ride(niye_jao, 'Lohagara', 'car', 5)
# rider.my_rides()