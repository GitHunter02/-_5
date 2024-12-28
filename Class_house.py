class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floor:
            print('Данный этаж не предусмотрен в планировке здания')
        else:
            for i in range(1, new_floor):
                print(f"Проехали {i} этаж")
            print(f"Вы доехали до {new_floor} этажа")

    def __len__(self):
        return self.number_of_floor

    def __eq__(self, other):
        return self.number_of_floor == other.number_of_floor

    def __lt__(self, other):
        return self.number_of_floor < other.number_of_floor

    def __le__(self, other):
        return self.number_of_floor <= other.number_of_floor

    def __gt__(self, other):
        return self.number_of_floor > other.number_of_floor

    def __ge__(self, other):
        return self.number_of_floor >= other.number_of_floor

    def __ne__(self, other):
        return self.number_of_floor != other.number_of_floor

    def __add__(self, value):
        self.number_of_floor += value
        return self

    def __radd__(self, value):
        return self + value

    def __iadd__(self, value):
        self.number_of_floor += value
        return self

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floor}"


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

#  __len__
print(len(h1))
print(len(h2))

# __eq__
print(h1 == h2)

# __add__
h1 = h1 + 10
print(h1)
print(h1 == h2)

# __iadd__
h1 += 10
print(h1)

# __radd__
h2 = 10 +h2
print(h2)

# __gt__
print(h1 > h2)

# __ge__
print(h1 >= h2)

# __lt__
print(h1 < h2)

# __le__
print(h1 <= h2)

# __ne__
print(h1 != h2)