def max_geodes_dp(blueprint, time_limit=24):
    # Initialize memoization table
    memo = {}

    def dp(time_left, ore, clay, obsidian, geode):
        if time_left == 0:
            return geode

        if (time_left, ore, clay, obsidian, geode) in memo:
            return memo[(time_left, ore, clay, obsidian, geode)]

        ore_robots = min(ore // blueprint["ore"], time_left)
        clay_robots = min(clay // blueprint["clay"], time_left)
        obsidian_robots = min(obsidian // blueprint["obsidian"], time_left)
        geode_robots = min(geode // blueprint["geode_obsidian"], time_left)

        max_geodes_result = 0
        for ore_robot_count in range(ore_robots + 1):
            for clay_robot_count in range(clay_robots + 1):
                for obsidian_robot_count in range(obsidian_robots + 1):
                    for geode_robot_count in range(geode_robots + 1):
                        remaining_time = time_left - (ore_robot_count + clay_robot_count + obsidian_robot_count + geode_robot_count)
                        if remaining_time < 0:
                            continue

                        new_ore = ore - ore_robot_count * blueprint["ore"] + remaining_time
                        new_clay = clay - clay_robot_count * blueprint["clay"] + remaining_time
                        new_obsidian = obsidian - obsidian_robot_count * blueprint["obsidian"] + remaining_time
                        new_geode = geode + geode_robot_count * blueprint["geode_obsidian"]

                        max_geodes_result = max(max_geodes_result, dp(remaining_time, new_ore, new_clay, new_obsidian, new_geode))

        memo[(time_left, ore, clay, obsidian, geode)] = max_geodes_result
        return max_geodes_result

    initial_ore = time_limit
    initial_clay = 0
    initial_obsidian = 0
    initial_geode = 0

    return dp(time_limit, initial_ore, initial_clay, initial_obsidian, initial_geode)

blueprints = [
    {
        "id": 1,
        "ore": 4,
        "clay": 2,
        "obsidian": 3,
        "geode_obsidian": 7
    },
    {
        "id": 2,
        "ore": 2,
        "clay": 3,
        "obsidian": 3,
        "geode_obsidian": 12
    }
]

total_quality_level = 0
for blueprint in blueprints:
    geodes = max_geodes_dp(blueprint)
    quality_level = blueprint["id"] * geodes
    total_quality_level += quality_level

print("Total Quality Level:", total_quality_level)
