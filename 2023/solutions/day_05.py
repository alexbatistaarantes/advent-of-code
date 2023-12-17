from re import *

class IfYouGiveASeedAFertilizer:

    def get_closest_location(almanac, seed_is_range=False):
        
        # values is the aspect current being converted (starting from seeds and ending in location)        
        values, maps = IfYouGiveASeedAFertilizer.parse_almanac(almanac, seed_is_range=seed_is_range)

        for index in range(len(values)):
            value = values[index]

        # iterate through all maps
        for map_ranges in maps.values():
            new_values = []
            # iterate through values
            for index in range(len(values)):
                value = values[index]
        
                # iterate through the ranges in the current conversion
                for map_range in map_ranges:
                    if seed_is_range:
                        # start of current value range is between map range
                        if map_range[0] <= value[0] < map_range[0]+map_range[1]:
                            # new range, from either until last value from current one (range is fully inserted in map range), or last value from map range
                            range = min(value[0]+value[1], map_range[0]+map_range[1]) - value[0]
                            new_values.append(value[0], range)
                            # 
                            value[0] = value[0] + range
                            value[1] -= range
                        # end of the current value range is between map range
                        if map_range[1] <= value[0]+value[1] < map_range[0]+map_range[1]:
                            range = min(value[0]+value[1], map_range[0]+map_range[1]) - value[0]
                            new_values.append(value[0], range)
                            value[0] = value[0] + range
                            value[1] -= range
                        
                    # if the value is in the current range, sets value to values and break
                    if  map_range[1] <= value < map_range[1] + map_range[2]:
                        new_values.append(map_range[0] + (value-map_range[1]))
                        break
                    # the value keeps the same if it didn't fell in any of the ranges
                # if there is value still out of map ranges, add to new value
                if value[1] > 0:
                    new_values.append(value)
            values = new_values
        return min(values)
    

    def get_closest_location(almanac, seed_is_range=False):
        
        # values is the aspect current being converted (starting from seeds and ending in location)        
        values, maps = IfYouGiveASeedAFertilizer.parse_almanac(almanac, seed_is_range=seed_is_range)

        # iterate through all maps
        for map_ranges in maps.values():
            new_values = []
            # iterate through values
            for index in range(len(values)):
                value = values[index]
        
                # iterate through the ranges in the current conversion
                for map_range in map_ranges:
                    
                    # GAVE UP AND USED [THIS ONE](https://github.com/mgtezak/Advent_of_Code/blob/master/2023/Day_05.py) SO I COULD MOVE ON
                    if seed_is_range: 
                        # start of current value range is between map range
                        if map_range[0] <= value[0] < map_range[0]+map_range[1]:
                            # new range, from either until last value from current one (range is fully inserted in map range), or last value from map range
                            range = min(value[0]+value[1], map_range[0]+map_range[1]) - value[0]
                            new_values.append(value[0], range)
                            # 
                            value[0] = value[0] + range
                            value[1] -= range
                        # end of the current value range is between map range
                        if map_range[1] <= value[0]+value[1] < map_range[0]+map_range[1]:
                            range = min(value[0]+value[1], map_range[0]+map_range[1]) - value[0]
                            new_values.append(value[0], range)
                            value[0] = value[0] + range
                            value[1] -= range
                        
                    # if the value is in the current range, sets value to values and break
                    if  map_range[1] <= value < map_range[1] + map_range[2]:
                        new_values.append(map_range[0] + (value-map_range[1]))
                        break
                    # the value keeps the same if it didn't fell in any of the ranges
                # if there is value still out of map ranges, add to new value
                if value[1] > 0:
                    new_values.append(value)
            values = new_values
        return min(values)

    def parse_almanac(almanac, seed_is_range=False):

        almanac = almanac.split('\n')

        # get seeds from first line
        if seed_is_range:
            seeds = [(int(seed_range.split()[0]), int(seed_range.split()[1])) for seed_range in findall(r"(\d+ +\d+)", almanac[0])]
        else:
            seeds = [int(seed) for seed in split(r"\s+", findall(r"seeds: +((\d+ *)+)", almanac[0])[0][0])]
        
        maps = {
            # seed to soil: ranges (seed, soil, range)
            # ('seed', 'soil'): [()]
        }

        for line in almanac[1:]:
            # empty lines separating maps
            if len(line) == 0:
                continue
            # line indicating what is being mapped
            mapping = match(r"(\w+)-to-(\w+) map:", line)
            if mapping:
                maps[(mapping.group(1), mapping.group(2))] = []
                continue
            # ranges
            last_mapping_key = list(maps.keys())[-1]
            dest_start, source_start, map_range = findall(r"(\d+) +(\d+) +(\d+)", line)[0]
            maps[last_mapping_key].append((int(dest_start), int(source_start), int(map_range)))

        return seeds, maps

test_input = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

#IfYouGiveASeedAFertilizer.get_closest_location(test_input, seed_is_range=True)