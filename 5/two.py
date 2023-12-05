import regex as re
with open('almanac.txt', 'r') as game_record:
    lines = list(line for line in (line.rstrip() for line in game_record.readlines()) if line)

seed_numbers = []
seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []
current_map = None

for line in lines:
    if "seeds:" in line:
        seed_numbers = list(int(num) for num in re.findall(r'\d+', line))
        continue
    elif "seed-to-soil map:" in line:
        current_map = "seed-to-soil"
        continue
    elif "soil-to-fertilizer map:" in line:
        current_map = "soil-to-fertilizer"
        continue
    elif "fertilizer-to-water map:" in line:
        current_map = "fertilizer-to-water"
        continue
    elif "water-to-light map:" in line:
        current_map = "water-to-light"
        continue
    elif "light-to-temperature map:" in line:
        current_map = "light-to-temperature"
        continue
    elif "temperature-to-humidity map:" in line:
        current_map = "temperature-to-humidity"
        continue
    elif "humidity-to-location map:" in line:
        current_map = "humidity-to-location"
        continue

    current_numbers = list(int(num) for num in re.findall(r'\d+', line))

    match current_map:
        case "seed-to-soil":
            seed_to_soil_map.append(current_numbers)
        case "soil-to-fertilizer":
            soil_to_fertilizer_map.append(current_numbers)
        case "fertilizer-to-water":
            fertilizer_to_water_map.append(current_numbers)
        case "water-to-light":
            water_to_light_map.append(current_numbers)
        case "light-to-temperature":
            light_to_temperature_map.append(current_numbers)
        case "temperature-to-humidity":
            temperature_to_humidity_map.append(current_numbers)
        case "humidity-to-location":
            humidity_to_location_map.append(current_numbers)

seed_to_soil_map.sort(key=lambda x: x[1])
soil_to_fertilizer_map.sort(key=lambda x: x[1])
fertilizer_to_water_map.sort(key=lambda x: x[1])
water_to_light_map.sort(key=lambda x: x[1])
light_to_temperature_map.sort(key=lambda x: x[1])
temperature_to_humidity_map.sort(key=lambda x: x[1])
humidity_to_location_map.sort(key=lambda x: x[1])

seed_ids = []
for i in range(1, len(seed_numbers), 2) :
    for seed_id in range(seed_numbers[i-1], seed_numbers[i-1] + seed_numbers[i]):
        seed_ids.append(seed_id)
seed_numbers = seed_ids

all_locations = []
for seed in seed_numbers:
    soil = fertilizer = water = light = temp = humidity = location = None
    #print(f"Seed: {seed}")

    # Seed to Soil
    for mapping in seed_to_soil_map:
        if seed in range(mapping[1], mapping[1] + mapping[2]):
            # print(f"seed {seed} mapped in {mapping}")
            soil = mapping[0] + (seed - mapping[1])
            continue
    if not soil: soil = seed

    # Soil To Fertilizer
    for mapping in soil_to_fertilizer_map:
        if soil in range(mapping[1], mapping[1] + mapping[2]):
            # print(f"soil {soil} mapped in {mapping}")
            fertilizer = mapping[0] + (soil - mapping[1])
            continue
    if not fertilizer: fertilizer = soil

    # Fertilizer to Water
    for mapping in fertilizer_to_water_map:
        if fertilizer in range(mapping[1], mapping[1] + mapping[2]):
            # print(f"fert {fertilizer} mapped in {mapping}")
            water = mapping[0] + (fertilizer - mapping[1])
            continue
    if not water: water = fertilizer

    # Water to Light
    for mapping in water_to_light_map:
        if water in range(mapping[1], mapping[1] + mapping[2]):
            # print(f"water {water} mapped in {mapping}")
            light = mapping[0] + (water - mapping[1])
            continue
    if not light: light = water

    # Light to Temperature
    for mapping in light_to_temperature_map:
        if light in range(mapping[1], mapping[1] + mapping[2]):
            # print(f"light {light} mapped in {mapping}")
            temp = mapping[0] + (light - mapping[1])
    if not temp: temp = light

    # temperature to humidity
    for mapping in temperature_to_humidity_map:
        if temp in range(mapping[1], mapping[1] + mapping[2]):
            # print(f"temp {temp} mapped in {mapping}")
            humidity = mapping[0] + (temp - mapping[1])
            continue
    if not humidity: humidity = temp

    # Humidity to Location
    for mapping in humidity_to_location_map:
        if humidity in range(mapping[1], mapping[1] + mapping[2]):
            #print(f"humidity {humidity} mapped in {mapping}")
            location = mapping[0] + (humidity - mapping[1])
            continue
    if not location: location = humidity

    #print(f"Location: {location}")
    #print(f"--> Seed {seed}, Soil {soil}, Fertilizer {fertilizer}, Water {water}, Light {light}, Temp {temp}, Humid {humidity}, Location {location}")
    all_locations.append(location)
    seed_amount = seed_amount - 1
    print(f"{seed_amount} seeds left to process")


#print(all_locations)
all_locations.sort()
print(f"Nearest Location: {all_locations[0]}")