class ZachsParkingGarage:
    def __init__(self):
        # Initializing the dictionary to keep track of purchased parking spots
        self.BoughtSpots = {}

    def purchase_parking_space(self, parking_spot):
        # Marking the parking spot as purchased
        self.BoughtSpots[parking_spot] = False
        print("========================= Spot Purchased =========================")
        print(f"You have purchased parking space {parking_spot}")

    def overpriced_pay_portal(self, parking_spot):
        # Checking if the parking spot exists in the dictionary
        if parking_spot in self.BoughtSpots:
            self.BoughtSpots[parking_spot] = True
            print("========================= Payment Successful =========================")
            print("Thanks for paying for our wonderful parking garage. Please tell us how we did at us at overpricedandsketchy@mostparkinggarages.com.")
        else:
            print("No one has purchsed that spot or it doesnt exist.")

    def leave_garage(self, parking_spot):
        # Checking if the parking spot exists in the dictionary
        if parking_spot in self.BoughtSpots:
            if self.BoughtSpots[parking_spot]:
                print("Thank you, have a nice day!")
                print("========================= LEAVING GARAGE =========================")
                print("========================= LEAVING GARAGE =========================")
                print("========================= LEAVING GARAGE =========================")
                print("========================= LEAVING GARAGE =========================")
                print("========================= LEAVING GARAGE =========================")
                print("========================= LEAVING GARAGE =========================")
                print("========================= LEAVING GARAGE =========================")
                print("========================= LEAVING GARAGE =========================")
                del self.BoughtSpots[parking_spot]
            else:
                print("THEIF! THEIF! Brandon from Coding Temple will come for you.")
        else:
            print("No one has purchsed that spot or it doesnt exist.")


def RunGarage():
    # Creating an instance of ZachsParkingGarage
    garage = ZachsParkingGarage()

    while True:
        print("Zach's Parking Garage")
        print("Buy a spot (sponsored byTMobile) [type 'buy']")
        print("Pay [type 'pay']")
        print("Exit [type 'exit']")
        print("Cancel [type 'cancel]")

        user_nav = input("What would you like to do? ")

        if user_nav == 'buy':
            parking_spot = input("What parking space would you you like: ")
            garage.purchase_parking_space(parking_spot)
        elif user_nav == 'pay':
            parking_spot = input("What is your parking space? ")
            garage.overpriced_pay_portal(parking_spot)
        elif user_nav == 'exit':
            parking_spot = input("What is your parking space? ")
            garage.leave_garage(parking_spot)
            break
        elif user_nav == 'cancel':
            print("Our sincerest regrets our customer service could not live up to expectations today. ")
            break
        else:
            print("We dont have that option try again! ")


if __name__ == "__main__":
    # Running the garage
    RunGarage()
