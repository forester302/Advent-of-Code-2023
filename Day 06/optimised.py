import get_data
import math
import time

def get_wins(t, d):
    def solve_quadratic(a, b, c):
        x1: float = (-b + math.sqrt(b**2 - 4*a*c))/(2*a)
        x2 = (-b - math.sqrt(b**2 - 4*a*c))/(2*a)
        return [x1, x2]

    values = solve_quadratic(-1, t, -d)
    # if values are integers adjust them so correct range is given
    if values[0].is_integer():
        values[0] += 1
    if values[1].is_integer():
        values[1] -= 1
    values[0] = math.ceil(values[0])
    values[1] = math.floor(values[1])
    return values[1] - values[0] + 1

def get_int_list(data):
    data = data.strip(" ").split(" ")
    data2 = []
    for d in data:
        if d:
            data2.append(int(d))
    return data2

def get_long_int(data):
    intlist = get_int_list(data)
    return int(str(intlist[0]) + str(intlist[1]) + str(intlist[2]) + str(intlist[3]))

def calculate(times, distances):
    product = 1
    for i, time in enumerate(times):
        distance = distances[i]
        wins = get_wins(time, distance)
        if wins:
            product *= wins
    print(product)

def main():
    start = time.perf_counter()
    (_, times), (_, distances) = [line.split(":") for line in get_data.get_data().split("\n")]
    print("Part1: ", end="")
    calculate(get_int_list(times), get_int_list(distances))
    print("Part2: ", end="")
    print(get_wins(get_long_int(times), get_long_int(distances)))
    print(f"Time: {time.perf_counter()-start}")

if __name__ == "__main__":
    main()