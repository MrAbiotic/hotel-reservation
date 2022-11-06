"""
etgdemo = {
        1: {
            1: [0, 1],
            2: [0, 1],
            },
        2: {
            3: [0, 2],
            4: [0, 2],
            }
        }
"""

etg_quantity = 2
room_1 = [1 for x in range(20)]
room_2 = [2 for x in range(20)]
room_4 = [4 for x in range(40)]
room_total = room_1 + room_2 + room_4
rooms_per_etg = len(room_total) // etg_quantity

etg = {x: {} for x in range(1, etg_quantity+1)}
room_dic = {x: [0, room_total[x-1]] for x in range(1, len(room_total)+1, 1)}

for etg_active in range(etg_quantity):
    for room in range(1, rooms_per_etg+1):
        etg[etg_active+1].update({room+rooms_per_etg*etg_active: [0, room_total[room+rooms_per_etg*etg_active-1]]})
        #print(etg_active)
        if etg_active+1 == etg_quantity and room == rooms_per_etg and len(room_total) % etg_quantity != 0:
            print("test")
            for room in range(rooms_per_etg+1, rooms_per_etg + len(room_total)%etg_quantity+1):
                etg[etg_active+1].update({room+rooms_per_etg*etg_active: [0, room_total[room+rooms_per_etg*etg_active-1]]})


if __name__ == "main":
    print(etg)
