import get_data

def get_points(tw_numbers):
    point = 0
    if tw_numbers > 0:
        point = 1
        tw_numbers -= 1
    while tw_numbers > 0:
        point *=2 
        tw_numbers -= 1
    return point

def calculate():
    data = [([n for n in line.split(" | ")[0].split(": ")[1].split(" ")], [n for n in line.split(" | ")[1].split(" ")]) for line in get_data.get_data().split("\n")]
    points = 0
    cards = [1 for _ in data]
    for i, (winningnumbers, numbers) in enumerate(data):
        tw_numbers = 0
        for n in numbers:
            if n in winningnumbers and n != "": tw_numbers += 1
        points += get_points(tw_numbers)
        for j in range(1, tw_numbers+1):
            cards[i+j] += cards[i]
        print(cards, i)
    return points, sum(cards)

def main():
    points, cards = calculate()
    print(f"Part1: {points}")
    print(f"Part2: {cards}")
    
if __name__ == "__main__":
    main()
