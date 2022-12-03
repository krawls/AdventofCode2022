# helper function to convert a character to a priority value
# a..z = 1..26
# A..Z = 27..52
def convert_char_to_priority(char):
    # ASCII values:
    #   a..z = 97..122
    #   A..Z = 65..90
    #   lower case ASCII is same as upper, but with a bit in the 6th position (+32)
    #
    # get ASCII value in decimal
    ascii_val_dec = ord(char)
    if ascii_val_dec >= 97:
        priority = ascii_val_dec - 96   # 96 = 97 - 1
    else:
        priority = ascii_val_dec - 38   # 38 = 65 - 27

    return priority


# Given file of lines of sequence of letters, split string in half and 
# find characters common between the two halves. \
# These letters correspond to a priority value. Sum these values.
def rucksack_priorities(filename):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')
    
    priorities_sum = 0

    # enumerate() will return an index and element
    for i, line in enumerate(lines):
        # split the line into two equal halves
        # should be even numbers but will use // (int division) anyway for robustness
        length = len(line)
        first_half = line[:length//2]
        second_half = line[length//2:]

        # iterate through first half char by char and see if it exists in the second half
        # if it does, then add the priority value
        #
        # Note: does not account for multiple collisions, so break after one found
        #       otherwise will double count
        for c in first_half:
            if c in second_half:
                priorities_sum += convert_char_to_priority(c)
                break

    file.close()

    return priorities_sum

# Given file of lines of sequence of letters, group each three lines together
# and find the one character common between the three lines. 
# These letters correspond to a priority value. Sum these values.
def rucksack_priorities_part2(filename):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')
    
    priorities_sum = 0

    # enumerate() will return an index and element
    for i, line in enumerate(lines):
        # check for the 3rd line in a group of 3
        #
        # Note: i will index to 0, so add 1, else our modulo will be off
        line_num = i + 1 
        if line_num % 3 == 0:
            line_1 = lines[i-2]
            line_2 = lines[i-1]
            line_3 = lines[i]

            # iterare through line 1.
            # if a character does not match something in line 2, then break and try next character
            # if a character matches something in line 2, then try against line 3.
            # if it matches against line 2 and line 3, then it's common between all and that is our answer
            # to add to priorities_sum

            for c in line_1:
                if c in line_2:
                    if c in line_3:
                        priorities_sum += convert_char_to_priority(c)
                        break

    file.close()

    return priorities_sum

print("Day 03-1 Output: ", rucksack_priorities('input.txt'))
print("Day 03-2 Output: ", rucksack_priorities_part2('input.txt'))