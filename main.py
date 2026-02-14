# Function to calculate the longest time in the array
def longest(skater):
    # Init max_time
    max_time = 0
    # Iterate over all elements in the times array
    for i in range(len(skater)):
        # if is max_time
        if max_time < skater[i]:
            # update max_time
            max_time = skater[i]
            # store lap number
            lap_number = i + 1
    return (max_time, lap_number)

def largest_difference(skater1, skater2):
    # Find longest lap and lap number of skater1
    longest_lap_1, lap_no_1 = longest(skater1)
    # Find longest lap and lap number of skater1
    longest_lap_2, lap_no_2 = longest(skater2)
    # Return number of the longest lap
    if longest_lap_1 > longest_lap_2:
        return lap_no_1
    else:
        return lap_no_2

print(largest_difference([26.11, 25.80, 25.92, 26.23, 26.07], [25.93, 25.74, 26.53, 26.11, 26.30]))