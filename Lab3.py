from enum import Enum


class Good:
    def __init__(self, price, weight_in_grams, producer, country):
        self.__price = price
        self.__weight_in_grams = weight_in_grams
        self.producer = producer
        self.country = country

    def __repr__(self):
        return repr(
            (
                self._Good__price,
                self._Good__weight_in_grams,
                self.producer,
                self.country,
            )
        )


class Pump(Good):
    def __init__(
        self, price, weight_in_grams, producer, country, max_pressure, nippel_type
    ):
        super().__init__(price, weight_in_grams, producer, country)
        self.max_pressure = max_pressure
        self.nippel_type = nippel_type

    def __repr__(self):
        return repr(
            (
                self._Good__price,
                self._Good__weight_in_grams,
                self.producer,
                self.country,
                self.max_pressure,
                self.nippel_type,
            )
        )


class Multitool(Good):
    def __init__(
        self, price, weight_in_grams, producer, country, size_in_mm, number_of_tools
    ):
        super().__init__(price, weight_in_grams, producer, country)
        self.size_in_mm = size_in_mm
        self.number_of_tools = number_of_tools

    def __repr__(self):
        return repr(
            (
                self._Good__price,
                self._Good__weight_in_grams,
                self.producer,
                self.country,
                self.size_in_mm,
                self.number_of_tools,
            )
        )


class Lamp(Good):
    def __init__(
        self,
        price,
        weight_in_grams,
        producer,
        country,
        number_of_LEDs,
        color_tempr_in_K,
        time_of_work_in_hours,
    ):
        super().__init__(price, weight_in_grams, producer, country)
        self.number_of_LEDs = number_of_LEDs
        self.color_tempr_in_K = color_tempr_in_K
        self.time_of_work_in_hours = time_of_work_in_hours

    def __repr__(self):
        return repr(
            (
                self._Good__price,
                self._Good__weight_in_grams,
                self.producer,
                self.country,
                self.number_of_LEDs,
                self.color_tempr_in_K,
                self.time_of_work_in_hours,
            )
        )


class Countries(Enum):
    Ukraine = 1
    Germany = 2
    Italy = 3
    USA = 4
    Spain = 5
    France = 6
    Canada = 7
    China = 8


def sort_by_weight(list_of_objects, is_reverse):
    def get_weight(Good):
        return Good._Good__weight_in_grams

    list_of_objects.sort(key=get_weight, reverse=is_reverse)


def sort_by_producer(list_of_objects, is_reverse):
    def get_producer(Good):
        return Good.producer

    list_of_objects.sort(key=get_producer, reverse=is_reverse)


def search_by_producer(list_of_objects, wanted_producer):
    for i in list_of_objects:
        if wanted_producer == i.producer:
            return i
    

def main():
    pump_objects = [
        Pump(110, 600, "Green Cycle", Countries.Ukraine.name, 100, "Type A"),
        Pump(185, 300, "Alan Bike", Countries.Italy.name, 90, "Type C"),
        Pump(114.9, 750, "American Bicycle Group", Countries.USA.name, 50, "Type B"),
    ]

    mult_objects = [
        Multitool(160, 400, "Bulls", Countries.Germany.name, 100, 6),
        Multitool(125, 150, "Cyfac International", Countries.France.name, 90, 3),
        Multitool(143.9, 220, "Comanche", Countries.Ukraine.name, 50, 4),
    ]

    lamp_objects = [
        Lamp(60, 150, "Norco Performance Bikes", Countries.Canada.name, 4, 5000, 6),
        Lamp(80, 225, "DK", Countries.USA.name, 4, 6000, 7),
        Lamp(45, 80, "GAMMA", Countries.China.name, 2, 3000, 9),
        Lamp(75, 120, "Flybikes", Countries.Spain.name, 7, 4500, 5),
    ]

    sort_by_weight(pump_objects, False)
    print(*pump_objects, sep="\n")

    print("-------------------------------------\nСортування за вагою:")

    sort_by_weight(mult_objects, True)
    print(*mult_objects, sep="\n")

    print("-------------------------------------\nСортування за виробником:")

    sort_by_producer(lamp_objects, False)
    print(*lamp_objects, sep="\n")

    print("-------------------------------------\nПошук за виробником:")

    print("Введіть бажаного виробника: ")
    #wanted_producer = input()
    wanted_producer = "Flybikes"

    lamp_by_producer = search_by_producer(lamp_objects, wanted_producer)
    print(lamp_by_producer)

if __name__ == "__main__":
    main()
