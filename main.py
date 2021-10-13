from TakeUserInput import MainMenu
from Registration import Registration
from VehicleTax import VehicleTax

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        vehicle = MainMenu()
        if vehicle:
            if vehicle.registration:
                vehicle.printVehicleDetails()
            else:
                registration = Registration()
                vehicle.registration = registration.generateRegistrationNumber()
                vehicleTax = VehicleTax()
                vehicle.tax = vehicleTax.calculateVehicleTax(int(vehicle.price))
                registration.setRegisteredVehicles(vehicle)
                vehicle.printVehicleDetails()

        else:
            print("vehicle not found")



