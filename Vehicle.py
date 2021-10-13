class Vehicle:
    make: None
    model: None
    price: None
    color: None
    registration: None
    vehicleTax: None

    def __init__(self, make, model, price, color):
        self.make = make
        self.model = model
        self.price = price
        self.color = color
        self.registration = None
        self.tax = None

    def printVehicleDetails(self):
        print("Make: " + str(self.make))
        print("Model: " + str(self.model))
        print("Price: " + str(self.price))
        print("Color: " + str(self.color))
        if(self.registration):
            print("Registration Number: " + str(self.registration))
        if(self.tax):
            print("Tax Amount: " + str(self.tax.taxAmount))
            print("Tax Payment Date: " + str(self.tax.taxPaymentDate))
            print("Tax Renewal Date: " + str(self.tax.taxRenewalDate))
        else:
            print("Vehicle has no tax (exempted)")