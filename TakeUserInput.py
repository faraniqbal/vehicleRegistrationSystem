from Registration import Registration

def GetVehicleDetails():
    from Vehicle import Vehicle

    print("1. Enter Car details: ")
    print("Make: ")
    make = input()
    print("Model: ")
    model = input()
    print("Price: ")
    price = input()
    print("Color: ")
    color = input()
    vehicle = Vehicle(make, model, price, color)
    return vehicle

def MainMenu():
    print("Welcome to Vehicle Registration System")
    print("Please Select")
    print("1- Vehicle Registration")
    print("2- Find Registered Vehicle by Number")
    userInput = input()

    if userInput:
        if userInput == "1":
            return GetVehicleDetails()
        elif userInput == "2":
            print("Enter Vehicle Number:")
            registrationNumber = input()
            return Registration().getVehicleDetails(int(registrationNumber))
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")


