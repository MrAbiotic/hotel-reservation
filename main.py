class Hotell:
    def __init__(self) -> None:
        self.etasjer:int = 4
        self.etasjekapasitet = 12


class Customer:
    def __init__(self, name: str, guest_count: int) -> None:
        self.name = name
        self.guest_count = guest_count
