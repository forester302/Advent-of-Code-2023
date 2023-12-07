import get_data
import time

decode = {
    "A": 12,
    "K": 11,
    "Q": 10,
    "T": 8,
    "9": 7,
    "8": 6,
    "7": 5,
    "6": 4,
    "5": 3,
    "4": 2,
    "3": 1,
    "2": 0,
    "J": -1
}

def add_to_list(order: list, card_type, newcard, bid):
    if len(order) == 0:
        order.append((card_type, newcard, bid))
        return
    for i, card in enumerate(order):
        if card_type < card[0]:
            order.insert(i, (card_type, newcard, bid))
            return
        if card_type == card[0]:
            for j, cardchar in enumerate(card[1]):
                cardchar = decode[cardchar]
                newchar = newcard[j]
                newchar = decode[newchar]
                if newchar < cardchar:
                    order.insert(i, (card_type, newcard, bid))
                    return
                elif newchar > cardchar:
                    break
    else:
        order.append((card_type, newcard, bid))

def main(part2 = False):
    data = [(line.split(" ")[0], line.split(" ")[1]) for line in get_data.get_data().split("\n")]

    order = []

    for line in data:
        card = (len(set(line[0])), line[0])
        bid = line[1]
        if card[0] == 1 or (card[0] == 2 and 'J' in card[1] and part2):
            #Five of a kind
            add_to_list(order, 6, card[1], bid)
        elif card[0] == 2 or (card[0] == 3 and 'J' in card[1] and part2):
            #Four of a kind or Full house
            if 'J' not in card[1] or not part2:
                n = card[1].count(card[1][0])
                if n == 4 or n == 1:
                    #four of a kind
                    add_to_list(order, 5, card[1], bid)
                else:
                    #full house
                    add_to_list(order, 4, card[1], bid)
            else:
                # check for two pair
                if {card[1].count(i) for i in set(card[1])} == {2, 2, 1} and card[1].count('J') != 2:
                    #full house
                    add_to_list(order, 4, card[1], bid)
                else:
                    #four of a kind
                    add_to_list(order, 5, card[1], bid)
        elif card[0] == 3:
            if {card[1].count(i) for i in set(card[1])} == {2, 2, 1}:
                # two pair
                add_to_list(order, 2, card[1], bid)
            else:
                #three of a kind
                add_to_list(order, 3, card[1], bid)
        elif card[0] == 4:
            #One pair
            if part2 and 'J' in card[1]:
                add_to_list(order, 3, card[1], bid)
            else:
                add_to_list(order, 1, card[1], bid)
        else:
            #High card
            if part2 and 'J' in card[1]:
                add_to_list(order, 1, card[1], bid)
            else:
                add_to_list(order, 0, card[1], bid)

    winnings = 0
    for i, card in enumerate(order):
        winnings += (i+1)*int(card[2])
    return winnings

if __name__ == "__main__":
    start = time.perf_counter()
    print(f"Part1: {main()}")
    print(f"Part2: {main(True)}")
    print(f"Completed in: {time.perf_counter()-start}")
