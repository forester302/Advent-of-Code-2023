import get_data
import sys
import multiprocessing
import time

class Map:
    def __init__(self, name):
        self.name = name
        self.map: dict[range, range] = {}

    def add_range(self, end_start, source_start, length):
        self.map[range(source_start, source_start + length)] = range(end_start, end_start+length)

    def map_item(self, item):
        for map_range in self.map:
            if item in map_range:
                return self.map[map_range][0] + item - map_range[0]
        return item
    
    def map_item_reverse(self, item):
        for key in self.map:
            map_range = self.map[key]
            if item in map_range:
                return key[0] + item - map_range[0]
        return item

    
    def __repr__(self):
        return self.name + ":\n" + str(self.map)
    
def make_map(map_data) -> Map:
    name = map_data[0]
    map_data = map_data[1]
    map = Map(name)
    for line in map_data:
        map.add_range(line[0], line[1], line[2])
    return map

def process_seed_range(seed_range, seed_to_soil_map, soil_to_fertiliser_map, fertiliser_to_water_map, water_to_light_map, light_to_temp_map, temp_to_humid_map, humid_to_loc_map):
    n = 0
    min_location = sys.maxsize  # Initialize with a large value
    for j in range(seed_range[0], seed_range[0] + seed_range[1]):
        
        loc = process_seed(j, seed_to_soil_map, soil_to_fertiliser_map, fertiliser_to_water_map, water_to_light_map, light_to_temp_map, temp_to_humid_map, humid_to_loc_map)

        if n > 100000:
            print(j)
            n = 0
        n += 1
        
        # Update minimum location
        min_location = min(min_location, loc)
    return min_location

def process_seed(seed, seed_to_soil_map, soil_to_fertiliser_map, fertiliser_to_water_map, water_to_light_map, light_to_temp_map, temp_to_humid_map, humid_to_loc_map):
    soil = seed_to_soil_map.map_item(seed)
    fert = soil_to_fertiliser_map.map_item(soil)
    water = fertiliser_to_water_map.map_item(fert)
    light = water_to_light_map.map_item(water)
    temp = light_to_temp_map.map_item(light)
    humid = temp_to_humid_map.map_item(temp)
    return humid_to_loc_map.map_item(humid)

def process_seed_reverse(loc, seed_ranges, seed_to_soil_map, soil_to_fertiliser_map, fertiliser_to_water_map, water_to_light_map, light_to_temp_map, temp_to_humid_map, humid_to_loc_map):
    humid = humid_to_loc_map.map_item_reverse(loc)
    temp = temp_to_humid_map.map_item_reverse(humid)
    light = light_to_temp_map.map_item_reverse(temp)
    water = water_to_light_map.map_item_reverse(light)
    fertiliser = fertiliser_to_water_map.map_item_reverse(water)
    soil = soil_to_fertiliser_map.map_item_reverse(fertiliser)
    seed = seed_to_soil_map.map_item_reverse(soil)

    for seed_range in seed_ranges:
        if seed in seed_range:
            return True
    return False

def main():
    data = [(line.split(":")[0], [[int(n) for n in section.split(" ")] for section in line.split(":")[1].strip("\n").strip(" ").split("\n")]) for line in get_data.get_data().split("\n\n")]
    seeds = data[0][1][0]
    seed_to_soil_map = make_map(data[1])
    soil_to_fertiliser_map = make_map(data[2])
    fertiliser_to_water_map = make_map(data[3])
    water_to_light_map = make_map(data[4])
    light_to_temp_map = make_map(data[5])
    temp_to_humid_map = make_map(data[6])
    humid_to_loc_map = make_map(data[7])
    
    seed_ranges = [range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

    min_loc = sys.maxsize
    for seed in seeds:
        loc = process_seed(seed, seed_to_soil_map, soil_to_fertiliser_map, fertiliser_to_water_map, water_to_light_map, light_to_temp_map, temp_to_humid_map, humid_to_loc_map)
        min_loc = min(min_loc, loc)
    print(min_loc)

    for i in range(0, 10000000000):
        print(i)
        if process_seed_reverse(i, seed_ranges, seed_to_soil_map, soil_to_fertiliser_map, fertiliser_to_water_map, water_to_light_map, light_to_temp_map, temp_to_humid_map, humid_to_loc_map):
            break

if __name__ == "__main__":
    main()
