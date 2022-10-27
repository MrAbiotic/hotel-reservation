class Hotell:
    def __init__(self, places: int=10, luksusrom: int=2) -> None:
        self.places = places

    def check_availible_room(self):
        pass

    def assign_room(self):
        guest_count = self.guest_count
        room_of_4 = guest_count // 4
        guest_count %= 4 # Fjerner antallet fra 4-rom
        room_of_2 = guest_count // 2
        guest_count %= 2
        room_of_1 = guest_count

class Customer:
    def __init__(self, name: str, guest_count: int) -> None:
        self.name = name
        self.guest_count = guest_count
