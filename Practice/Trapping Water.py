def trapping_water(region):
    max_left = [0]*len(region)
    max_right = [0]*len(region)
    water_level = [0]*len(region)

    # get left boundaries
    max_seen = region[0]
    for i in range(1, len(region)-1):
        max_left[i] = max_seen
        max_seen = max(max_seen, region[i])

    # get right boundaries
    max_seen = region[-1]
    for i in range(len(region)-2, 0, -1):
        max_right[i] = max_seen
        max_seen = max(max_seen, region[i])

    # calculate water levels between left and right boundaries
    for i in range(1, len(region)-1):
        level = min(max_left[i], max_right[i]) - region[i]
        water_level[i] = max(level, 0)

    return sum(water_level)

region = [1,2,1,3,4,4,5,1,2,0,3]
region = [0,1,0,2,1,0,1,3,2,1,2,1]

print trapping_water(region)