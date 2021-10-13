from datetime import date

class VehicleTax:

    taxAmount = None
    taxPaymentDate = None
    taxRenewalDate = None

    def __init__(self, taxAmount=0):
        self.taxAmount = taxAmount
        self.taxPaymentDate = date.today()
        self.taxRenewalDate = date.today()
        self.taxRenewalDate = self.taxRenewalDate.replace(year=date.today().year + 1)

    #
    # def deleteTaxNumber(self):
    #     del self.taxRegNumber

    def calculateVehicleTax(self, vehiclePrice):
        if(vehiclePrice > 1000000):
            self.taxAmount = vehiclePrice * 0.10
            return self
        taxAmount = 0
        return self

