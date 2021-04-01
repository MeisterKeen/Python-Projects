


class Vehicle:
    name = "None Entered"
    powerType = "" # Electric? Diesel? Fuel cells? Nuclear? lol!
    manufacturer = "" # This could have dozens of properties, really


    def goingPlaces():
        print("I go places and do things!")

    def vehicleNoises():
        print("Wheeeee!")

    def __init__(self, name, powerType, manufacturer): # I really like this one-line __init__() thing
        self.name = name
        self.powerType = powerType
        self.manufacturer = manufacturer

class Aircraft(Vehicle):
    wingProfile = ""
    wingSpan = "" # These two properties add onto the three of the parent

    def vehicleNoises():
        print("Whoosh!") # An example of polymorphism -- this function will override the parent function
                         # Because aircraft go "whoosh", of course!

    def __init__(self, name, powerType, manufacturer, wingConfiguration, wingSpan):
        self.name = name
        self.powerType = powerType
        self.manufacturer = manufacturer
        self.wingConfiguration = wingConfiguration
        self.wingSpan = wingSpan

    
class Boat(Vehicle):
    keelDepth = ""
    tonnage = ""
    mastsNumber = ""


if __name__ == "__main__":
    Boeing737 = Aircraft("Boeing 737", "Kerosene turbojet", "Boeing", "Fixed Swept-Back Wing", "118 ft")
    Huey = Aircraft("Bell UH-1 Iroquois 'Huey'", "Kerosene turboshaft", "Bell Helicopter", "Two-blade Helicopter", "48ft Rotor")
