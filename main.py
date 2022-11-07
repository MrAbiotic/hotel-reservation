import room_plan


class Price:
    def __init__(self) -> None:
        self.room_4_per_night = 225
        self.room_2_per_night = 250
        self.room_1_per_night = 300

class Hotell(Price):
    def __init__(self) -> None:
        super().__init__()
        self.plan = [[[etg, x, y] for x, y in room_plan.etg[etg].items()] for etg in room_plan.etg]

    def availible_room(self):
        available_rooms = []
        for etg in self.plan:
            for room in etg:
                if room[2][0] == 0:
                    available_rooms.append(room)
        return available_rooms

    def plan_oversikt(self):
        ledig = lambda n: "Opptatt" if n != 0 else "Ledig"
        for i, etg in enumerate(self.plan):
            print(f"\n{'Etasje':->16} {i+1:-<11}")
            for j, room in enumerate(etg):
                print(f"Rom {i+1}{j+1:0>2}: {ledig(room[2][0]):<10}{'str: '+str(room[2][1]): >10}")

class Customer(Price):
    total_orders = 0

    def __init__(self, full_name: str, epost: str, guest_count: int, duration: int, d_code: str=None) -> None:
        super().__init__()
        self.name = full_name
        self.epost = epost
        self.guest_count = guest_count
        self.room_count = self.room_required() # [4-, 2-, 1-mannsrom]
        self.duration = duration
        self.discount_code = self.discount(d_code)

        self.price()
        self.your_rooms = self.assign_room()

        Customer.total_orders += 1

    def assign_room(self) -> list:
        if self.epost in plumbum.plan:
            return

        count_of_availible_4 = 0
        count_of_availible_2 = 0
        count_of_availible_1 = 0
        for etg in plumbum.plan:
            for room in etg:
                if room[2][1] == 4 and room[2][0] == 0:
                    count_of_availible_4 += 1
                if room[2][1] == 2 and room[2][0] == 0:
                    count_of_availible_2 += 1
                if room[2][1] == 1 and room[2][0] == 0:
                    count_of_availible_1 += 1
        if count_of_availible_4 >= self.room_count[0] and count_of_availible_2 >= self.room_count[1] and count_of_availible_1 >= self.room_count[2]:
            local_room_count = [x for x in self.room_count]
            for etg in range(len(plumbum.plan)):
                for room in range(len(plumbum.plan[etg])):
                    if local_room_count[0] > 0:
                        if plumbum.plan[etg][room][2][0] == 0 and plumbum.plan[etg][room][2][1] == 4:
                            plumbum.plan[etg][room][2][0] = (self.epost, self.__dict__)
                            local_room_count[0] -= 1
                    if local_room_count[1] > 0:
                        if plumbum.plan[etg][room][2][0] == 0 and plumbum.plan[etg][room][2][1] == 2:
                            plumbum.plan[etg][room][2][0] = (self.epost, self.__dict__)
                            local_room_count[1] -= 1
                    if local_room_count[2] > 0:
                        if plumbum.plan[etg][room][2][0] == 0 and plumbum.plan[etg][room][2][1] == 1:
                            plumbum.plan[etg][room][2][0] = (self.epost, self.__dict__)
                            local_room_count[2] -= 1
        self.rooms()

    def rooms(self):
        print("Dine rom:")
        for i, etg in enumerate(plumbum.plan):
            if self.epost in etg:
                print(f"{'Etasje':->16} {i+1:-<11}")
            for j, room in enumerate(etg):
                if room[2][0] != 0 and room[2][0][0] == self.epost:
                    print(f"Rom {i+1}{j+1:0>2}, {'str: '+str(room[2][1]): >10}")
        # return [count_of_availible_4, count_of_availible_2, count_of_availible_1]

    def room_required(self):
        local_guest_count = self.guest_count
        room_of_4 = local_guest_count // 4
        local_guest_count %= 4 # Fjerner antallet fra 4-rom
        room_of_2 = local_guest_count // 2
        local_guest_count %= 2
        room_of_1 = local_guest_count
        room_list = [room_of_4, room_of_2, room_of_1]
        return room_list # Vær oppmerksom på at endring av rekkefølge i denne vil forandre kode nedover

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
        total_price *= abs(self.duration)
        total_price *= self.discount_code
        print(f"Det koster totalt: {total_price} for {self.duration} antall dager")
        # input("Betalingsmetode (Kort / Vipps / PayPal)")
        return total_price

class Employee:
    def __init__(self, full_name: str, email: str, position: str) -> None:
        self.name      = full_name
        self.email     = email
        self.position  = position
        self.wage      = self.paygrade(position)    

    def paygrade(position):
        if position == "Waitress" or "Janitor" or "Logistikkarbeider":
            return 1


alle_gjester = {}
def bestill():
    navn = input("Navn: ")
    epost = input("E-post: ")
    gjester = int(input("Antall gjester: "))
    dager = int(input("Antall dager: "))
    rabatt = input("Evt. rabattkode: ")
    betalingsmetode = input("Betalingsmetode (kort / vipps / paypal: ")
    alle_gjester[navn]=Customer(navn, epost, gjester, dager, rabatt)


def guide():
    print("""
Velkommen til Plumbum Hotell!
 ~ Her er alle velkomne

For å starte din bestilling, tast:
    bestill()

Eventuelt tast:
    kommando()

Fyll deretter ut skjemaet.

OBS!
Du kan bare ha en bestilling på hotellet.
""")

def kommando():
    print("""
bestill()
guide()
kommando()

alle_gjester[<navn>].room()
help(plumbum)
plumbum.availible_rooms()
plumbum.plan
plumbum.planoversikt()
""")

room_plan.reset()

guide()
plumbum = Hotell()
user = Customer(full_name="HT", epost="HT@", guest_count=3, duration=3, d_code="Rabatt10")
plumbum.plan_oversikt()