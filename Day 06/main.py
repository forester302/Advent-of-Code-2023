import get_data
import time

def get_wins(time, distance):
    pass
    suc_win = False
    wins = 0
    for x in range(0, time):
        d = x*(time-x)
        if d > distance:
            suc_win = True
            wins += 1
        elif suc_win:
            break
    return wins

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
    calculate([get_long_int(times)], [get_long_int(distances)])
    print(f"Time: {time.perf_counter()-start}")
    
if __name__ == "__main__":
    main()
