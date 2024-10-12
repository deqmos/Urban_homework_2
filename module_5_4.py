class House:
    houses_history = []

    def __new__(cls, *args: list, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name: str, number_of_floors: int):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            raise AttributeError("Ошибка, одна из переменных это не Класс")

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            raise AttributeError("Ошибка, одна из переменных это не Класс")

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            raise AttributeError("Ошибка, одна из переменных это не Класс")

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            raise AttributeError("Ошибка, одна из переменных это не Класс")

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            raise AttributeError("Ошибка, одна из переменных это не Класс")

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            raise AttributeError("Ошибка, одна из переменных это не Класс")

    def __add__(self, other):
        if isinstance(other, House):  # Почему бы не сложить этажи разных домов
            return House(self.name, self.number_of_floors + other.number_of_floors)
        elif not isinstance(other, int):  # Проверка на число
            raise ArithmeticError("Не операбельный оператор")
        else:
            return House(self.name, self.number_of_floors + other)

    def __radd__(self, other):
        if isinstance(other, House):  # Почему бы не сложить этажи разных домов
            return House(self.name, self.number_of_floors + other.number_of_floors)
        elif not isinstance(other, int):  # Проверка на число
            raise ArithmeticError("Не операбельный оператор")
        else:
            return House(self.name, self.number_of_floors + other)

    def __iadd__(self, other):
        if isinstance(other, House):  # Почему бы не сложить этажи разных домов
            return House(self.name, self.number_of_floors + other.number_of_floors)
        elif not isinstance(other, int):  # Проверка на число
            raise ArithmeticError("Не операбельный оператор")
        else:
            return House(self.name, self.number_of_floors + other)

    def __sub__(self, other):
        if not isinstance(other, int):  # Проверка на число
            raise ArithmeticError("Не операбельный оператор")
        else:
            return House(self.name, self.number_of_floors - other)

    def __mul__(self, other):
        if not isinstance(other, int):  # Проверка на число
            raise ArithmeticError("Не операбельный оператор")
        else:
            return House(self.name, self.number_of_floors * other)

    def __floordiv__(self, other):
        if not isinstance(other, int):  # Проверка на число
            raise ArithmeticError("Не операбельный оператор")
        else:
            return House(self.name, self.number_of_floors // other)

    def __pow__(self, other):
        if not isinstance(other, int):  # Проверка на число
            raise ArithmeticError("Не операбельный оператор")
        else:
            return House(self.name, self.number_of_floors ** other)

    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if new_floor > self.number_of_floors or new_floor < 1:
                print("Такого этажа не существует.")
                break
            else:
                print(i)

    def __del__(self):

        print(f"{self.name} снесён, но он останется в истории")


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
