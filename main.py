import room_plan

class Hotell:
    def __init__(self, places: int=10, luksusrom: int=2) -> None:
        self.places = places
        self.room = [[x, y] for room in room_plan.etg.items() for x, y in room]

    def check_availible_room(self):
        pass

class Price:
    def __init__(self) -> None:
        self.room_4_per_night = 225
        self.room_2_per_night = 250
        self.room_1_per_night = 300

class Customer(Price):
    def __init__(self, full_name: str, guest_count: int, duration: int, d_code: int) -> None:
        super().__init__()
        self.name = full_name 
        self.guest_count = guest_count
        self.room_count = self.assign_room()
        self.duration = duration
        self.discount_code = self.discount(d_code)

    def assign_room(self):
        room_of_4 = self.guest_count // 4
        self.guest_count %= 4 # Fjerner antallet fra 4-rom
        room_of_2 = self.guest_count // 2
        self.guest_count %= 2
        room_of_1 = self.guest_count
        return [room_of_4, room_of_2, room_of_1] # Vær oppmerksom på at endring av rekkefølge i denne vil forandre kode nedover

    @staticmethod
    def discount(d_code):
        if d_code == "Rabatt10":
            return 0.9
        elif d_code == "Rabatt20":
            return 0.8
        else: 
            return 1

    def price(self):
        total_price = self.room_count[0]*self.room_4_per_night
        total_price += self.room_count[1]*self.room_2_per_night
        total_price += self.room_count[2]*self.room_1_per_night
        total_price *= self.discount_code


hotell = Customer("HTHV", 9, 5, 8, 0)
print(hotell.assign_room())
