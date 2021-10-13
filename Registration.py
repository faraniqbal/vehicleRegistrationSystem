from Vehicle import Vehicle
import random

class Registration:
    registeredVehicles = []

    def findRegistrationNumber(self, registrationNumber):
        for reg in self.registeredVehicles:
            if reg.registration == registrationNumber:
                return True
        return False

    def getVehicleDetails(self, registrationNumber):
        for reg in self.registeredVehicles:
            if reg.registration == registrationNumber:
                return reg
        return None

    def setRegisteredVehicles(self, vehicle):
        self.registeredVehicles.append(vehicle)

    def generateRegistrationNumber(self):
        registrationNumber = random.randint(1000, 9999)
        if self.findRegistrationNumber(registrationNumber):
            self.generateRegistrationNumber()
        else:
            return registrationNumber