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

class Customer(Price):
    def __init__(self, full_name: str, epost: str, guest_count: int, duration: int, d_code: str=None) -> None:
        super().__init__()
        self.name = full_name
        self.epost = epost
        self.guest_count = guest_count
        self.room_count = self.room_required() # [4-, 2-, 1-mannsrom]
        self.duration = duration
        self.discount_code = self.discount(d_code)

    def assign_room(self):
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
            rooms_to_assign_left = self.room_count
            for etg in range(len(plumbum.plan)):
                for room in range(len(plumbum.plan[etg])):
                    if rooms_to_assign_left[0] > 0:
                        if plumbum.plan[etg][room][2][0] == 0 and plumbum.plan[etg][room][2][1] == 4:
                            plumbum.plan[etg][room] = self.epost
                            rooms_to_assign_left[0] -= 1
                    if rooms_to_assign_left[1] > 0:
                        if plumbum.plan[etg][room][2][0] == 0 and plumbum.plan[etg][room][2][1] == 2:
                            plumbum.plan[etg][room] = self.epost
                            rooms_to_assign_left[1] -= 1
                    if rooms_to_assign_left[2] > 0:
                        if plumbum.plan[etg][room][2][0] == 0 and plumbum.plan[etg][room][2][1] == 2:
                            plumbum.plan[etg][room] = self.epost
                            rooms_to_assign_left[2] -= 1

    def room_required(self):
        room_of_4 = self.guest_count // 4
        self.guest_count %= 4 # Fjerner antallet fra 4-rom
        room_of_2 = self.guest_count // 2
        self.guest_count %= 2
        room_of_1 = self.guest_count
        return [room_of_4, room_of_2, room_of_1] # Vær oppmerksom på at endring av rekkefølge i denne vil forandre kode nedover

    def overview(self):
        for etg in range(len(plumbum.plan)):
            print(f"{etg+1}:")
            for room in plumbum.plan[etg]:
                print(room, end=" ")

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

plumbum = Hotell()

class Employee:
    def __init__(self, full_name: str, email: str, position: str) -> None
        self.name      = full_name
        self.email     = email
        self.position  = position
        self.wage      = self.paygrade(position)    

    def paygrade(position)
        if position == "Waitress" or "Janitor" or "Logistikkarbeider":
            return 1

