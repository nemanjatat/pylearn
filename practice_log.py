class Vacation:
    def __init__(self, location, accommodation, duration):
        self.location = location
        self.accommodation = accommodation
        self.duration = duration

    def display_vacation_info(self):
        print(f"Location:       {self.location}\nAccommodation: {self.accommodation}\nDuration:     {self.duration} weeks")

print("Where would you like to go?")
location = input()

print("What type of accommodation would you like?(Hotel/Hostel/Other)")
accommodation = input()

print("How long are you staying?(in weeks)")
duration = input()

vacation = Vacation(location, accommodation, duration)

vacation.display_vacation_info()