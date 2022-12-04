# Given file of pairs of ranges, determine if one of the pairs fully contains
# the other pair. 
#   2-3,2-4 = True
#   2-3,3-4 = False
# If so, increment counter.
def overlapping_assignment_pairs_all(filename):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')
    
    count = 0

    # enumerate() will return an index and element
    for i, line in enumerate(lines):
        # first, split the line on the comma delimiter
        s1 = line.split(',')[0]
        s2 = line.split(',')[1]

        # for each of the new substrings, split on the hyphen delimter to get the
        # first and last number of the range
        v1 = s1.split('-')
        v2 = s2.split('-')

        # create a list of each of the ranges from v1,v2 lists 
        # remember to +1 the ending value of the range() function
        l1 = list(range(int(v1[0]),int(v1[1])+1))
        l2 = list(range(int(v2[0]),int(v2[1])+1))

        # check if l1 is fully conained in l2 and vice-versa
        # use handy all() function
        if all(i in l1 for i in l2) or all(i in l2 for i in l1):
            count += 1
            
    file.close()

    return count

# Given file of pairs of ranges, determine if one of the pairs overlaps
# the other pair. 
#   2-3,2-4 = True
#   2-3,3-4 = True
# If so, increment counter.
def overlapping_assignment_pairs_any(filename):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')
    
    count = 0

    # enumerate() will return an index and element
    for i, line in enumerate(lines):
        # first, split the line on the comma delimiter
        s1 = line.split(',')[0]
        s2 = line.split(',')[1]

        # for each of the new substrings, split on the hyphen delimter to get the
        # first and last number of the range
        v1 = s1.split('-')
        v2 = s2.split('-')

        # create a list of each of the ranges from v1,v2 lists 
        # remember to +1 the ending value of the range() function
        l1 = list(range(int(v1[0]),int(v1[1])+1))
        l2 = list(range(int(v2[0]),int(v2[1])+1))

        # check if any l1 is conained in l2
        # won't have to do a check the other way (l2 in l1) as its implied in the first check
        # use handy any() function
        if any(i in l1 for i in l2):
            count += 1
            
    file.close()

    return count

print("Day 04-1 Output: ", overlapping_assignment_pairs_all('input.txt'))
print("Day 04-2 Output: ", overlapping_assignment_pairs_any('input.txt'))