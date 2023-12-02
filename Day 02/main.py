import get_data

def part1():
    cubes = {"red": 12, "green": 13, "blue": 14}
    total = 0
    data = {int(game.split(":")[0].split(" ")[1]): [{item.split(" ")[1]:int(item.split(" ")[0]) for item in round.split(", ")} for round in game.split(": ")[1].split("; ")] for game in get_data.get_data().split("\n")}
    for game in data:
        for round in data[game]:
            for item in round:
                if cubes[item] < round[item]:
                    break
            else:
                continue
            break
        else:
            total += game
    return total

def part2():
    data = {int(game.split(":")[0].split(" ")[1]): [{item.split(" ")[1]:int(item.split(" ")[0]) for item in round.split(", ")} for round in game.split(": ")[1].split("; ")] for game in get_data.get_data().split("\n")}
    total = 0
    for game in data:
        cubes = {"red": 0, "green": 0, "blue": 0}
        for round in data[game]:
            for item in round:
                if round[item] > cubes[item]:
                    cubes[item] = round[item]
        power = cubes["red"] * cubes["green"] * cubes["blue"]
        total += power
    return total


def main():
    print(f"Part1: {part1()}")
    print(f"Part2: {part2()}")

    
if __name__ == "__main__":
    main()
