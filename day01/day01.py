# Count the number of calories for each elf. Return the largest number.
def max_calories(filename):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')
    
    current_calories = 0
    max_calories = 0

    # enumerate() will return an index and element
    for i, line in enumerate(lines):
        # check for blank lines to mark new elf
        # if found, compare against previous max and (always) reset current_calories to 0
        # else, keep incrementing calories
        if line == '':
            if current_calories > max_calories:
                max_calories = current_calories
            current_calories = 0
        else:
            current_calories += int(line)
    file.close()
    return max_calories

# Count the number of calories for the top three elves Return the sum of the three.
def top_three_calories(filename):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')
    
    current_calories = 0
    calorie_list = []

    # enumerate() will return an index and element
    for i, line in enumerate(lines):
        # check for blank lines to mark new elf
        # if found, add calorie value to new list and (always) reset current_calories to 0
        # else, keep incrementing calories
        if line == '':
            calorie_list.append(int(current_calories))
            current_calories = 0
        else:
            current_calories += int(line)
    file.close()

    # sort list descending and add the first 3 entries
    calorie_list.sort(reverse=True)
    return sum(calorie_list[0:3])

print("Day 01-1 Output: ", max_calories('input.txt'))
print("Day 01-2 Output: ", top_three_calories('input.txt'))