class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floor:
            print('Данный этаж не предусмотрен в планировке здания')
        else:
            for i in range(1, new_floor + 1):
                if i == new_floor:
                    print(f"Вы доехали до {new_floor} этажа")
                else:
                    print(f"Проехали {i} этаж")


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

h1.go_to(15)
h2.go_to(2)
