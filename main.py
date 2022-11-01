import room_plan

class Hotell:
    def __init__(self, places: int=10, luksusrom: int=2) -> None:
        self.places = places
        self.room = [[x, y] for room in room_plan.etg.items() for x, y in room]

    def check_availible_room(self):
        pass

class Customer:
    def __init__(self, full_name: str, guest_count: int, duration: int, d_code: int) -> None:
        self.name = full_name 
        self.guest_count = guest_count
        self.room_count = None
        self.duration = duration
        self.discount = d_code
        
    def assign_room(self):
        room_of_4 = self.guest_count // 4
        self.guest_count %= 4 # Fjerner antallet fra 4-rom
        room_of_2 = self.guest_count // 2
        self.guest_count %= 2
        room_of_1 = self.guest_count
        return [room_of_4, room_of_2, room_of_1]

hotell = Customer("HTHV", 9, 5, 8, 0)
print(hotell.assign_room())
