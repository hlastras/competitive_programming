import math
import sys

def parse_input(lines):
    seeds = [int(x) for x in lines[0].split()]
    maps = {}
    current_map = ""

    for line in lines[3:]:
        if line.strip().endswith('map:'):
            current_map = line.split(':')[0]
            maps[current_map] = []
        elif line.strip() and current_map:
            maps[current_map].append([int(x) for x in line.split()])

    return seeds, maps

def get_mapped_value(maps, category, value):
    for destination, source, length in maps[category]:
        if source <= value < source + length:
            return destination + (value - source)
    return value

def map_through_categories(seeds, maps):
    categories = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 
                  'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 
                  'humidity-to-location']
    mapped_values = seeds

    for category in categories:
        mapped_values = [get_mapped_value(maps, category, value) for value in mapped_values]

    return mapped_values

def find_lowest_location(seeds, maps):
    locations = map_through_categories(seeds, maps)
    return min(locations)

lines = sys.stdin.read().split("\n")
seeds, maps = parse_input(lines)
print(seeds)
lowest_location = find_lowest_location(seeds, maps)
print(lowest_location)
