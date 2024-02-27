# Cara 1
def number(bus_stops: list[int]) -> int:
    naik: int = 0
    turun: int = 0
    for i in range(len(bus_stops)):
        naik += bus_stops[i][0]
        turun += bus_stops[i][1]

    return naik - turun


# Cara 2
def number(bus_stops: list[int]) -> int:
    return sum([bus_stops[i][0] - bus_stops[i][1] for i in range(len(bus_stops))])


# Cara 3
def number(bus_stops: list[int]) -> int:
    return sum([i[0] - i[1] for i in bus_stops])


print(number([[6, 0], [4, 3], [4, 5]]))
