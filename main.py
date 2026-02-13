def longest(skater):
    # Initialize Skater
    max_skater = 0
    for i in range(len(skater)):
        if max_skater < skater[i]:
            max_skater = skater[i]
            pos_skater = i + 1
    return (max_skater, pos_skater)

def largest_difference(skater1, skater2):
    max_skater1, pos_skater1 = longest(skater1)
    max_skater2, pos_skater2 = longest(skater2)
    if max_skater1 > max_skater2:
        return pos_skater1
    else:
        return pos_skater2

pos = largest_difference([26.11, 25.80, 25.92, 26.23, 26.07], [25.93, 25.74, 26.53, 26.11, 26.30])
print(pos)