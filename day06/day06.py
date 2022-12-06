from collections import deque

# Given file with a stream of characters, parse characters until 
# there are <num> characters in a row that are unique.
# Return the position of the final character
def find_unique_sequence(filename, num):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')

    result = 0

    dq = deque()
    for i, char in enumerate(lines[0]):
        # add to the and of deque
        dq.append(char)

        # for the first <num>, fill up the deque before evaluation
        if len(dq) < num:
            continue

        # Convert deque to set, if that has length <num>, then 
        # there are no duplicates
        # else, take pop value off left and try again
        if len(set(dq)) == num:
            result = i+1    # add one because i is 0 indexed
            break
        else:
            dq.popleft()

    file.close()

    return result

print("Day 06-1 Output: ", find_unique_sequence('input.txt', 4))
print("Day 06-2 Output: ", find_unique_sequence('input.txt', 14))