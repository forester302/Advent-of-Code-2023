import get_data

NUMBERS = "1234567890"

def get_number(loc, data):
    number = ""
    gone_back = False
    while 0 <= loc[0] < len(data) and 0 <= loc[1] < len(data[0]) and data[loc[0]][loc[1]] in NUMBERS:
        loc = loc[0], loc[1] - 1
        gone_back = True
    if gone_back:
        loc = loc[0], loc[1] + 1
    while 0 <= loc[0] < len(data) and 0 <= loc[1] < len(data[0]) and data[loc[0]][loc[1]] in NUMBERS:
        number += data[loc[0]][loc[1]]
        loc = loc[0], loc[1] + 1
    return number

def check_up_down(loc, data):
    parts = []
    n = get_number(loc, data)
    if n: parts.append(int(n))
    else:
        newloc = loc[0], loc[1]-1
        n = get_number(newloc, data)
        if n: parts.append(int(n))
        newloc = loc[0], loc[1]+1
        n = get_number(newloc, data)
        if n: parts.append(int(n))
    return parts

def run_l_r(loc, data, gear, ratiolist, parts):
    n = get_number(loc, data)
    if n:
        if gear: ratiolist.append(int(n))
        parts.append(int(n))

def run_u_d(loc, data, gear, ratiolist, parts):
    temparts = check_up_down(loc, data)
    if temparts:
        if gear: ratiolist += temparts
        parts += temparts

def main():
    data = get_data.get_data().split("\n")
    characters = []
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char != "." and char not in NUMBERS:
                characters.append((i, j))
    parts = []
    gearparts = []
    for loc in characters:
        gear = False
        ratiolist = []
        if data[loc[0]][loc[1]] == "*":
            gear = True
        run_l_r((loc[0], loc[1] - 1), data, gear, ratiolist, parts)
        run_l_r((loc[0], loc[1] + 1), data, gear, ratiolist, parts)
        run_u_d((loc[0]-1, loc[1]), data, gear, ratiolist, parts)
        run_u_d((loc[0]+1, loc[1]), data, gear, ratiolist, parts)
        if gear and len(ratiolist) == 2:
            gearparts.append(ratiolist[0]*ratiolist[1])

    print(f"Part1: {sum(parts)}")
    print(f"Part2: {sum(gearparts)}")

if __name__ == "__main__":
    main()
