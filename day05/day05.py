# not going to parse the initial stack states....
# just going to do it by hand
def initialize_stacks():
    l1 = ["B","V","S","N","T","C","H","Q"]
    l2 = ["W","D","B","G"]
    l3 = ["F","W","R","T","S","Q","B"]
    l4 = ["L","G","W","S","Z","J","D","N"]
    l5 = ["M","P","D","V","F"]
    l6 = ["F","W","J"]
    l7 = ["L","N","Q","B","J","V"]
    l8 = ["G","T","R","C","J","Q","S","N"]
    l9 = ["J","S","Q","C","W","D","M"]

    list = [l1,l2,l3,l4,l5,l6,l7,l8,l9]

    return list


# Given file of stack at the top and instructions starting on line 10,
# use the instructions to move the crates around,
# then return the values of the crates on the top of each stack
# Intruction format:
#   move 3 from 6 to 2
#
# Note: stacks are 1 indexed and crates are moved 1 at a time
def realign_crates_one_at_a_time(filename):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')

    list = initialize_stacks()

    # enumerate() will return an index and element
    for i, line in enumerate(lines):
        # skip the first 9 lines to get to the instructions
        if i < 10:
            continue

        # l[1] = how many to move
        # l[3] = where to move from
        # l[5] = where to move to
        # adjust for 0 indexing
        l = line.split(' ')
        move_qty = int(l[1])
        move_from = int(l[3])-1
        move_to = int(l[5])-1

        for j in range(1,move_qty+1):
            # get the top crate off the given stack
            # and append to destination stack
            list[move_to].append(list[move_from].pop())
            
    file.close()

    # iterate across list and return top value of each crate
    result = ""
    for i in range(0,len(list)):
        result += list[i][-1]

    return result

# Given file of stack at the top and instructions starting on line 10,
# use the instructions to move the crates around,
# then return the values of the crates on the top of each stack
# Intruction format:
#   move 3 from 6 to 2
#
# Note: stacks are 1 indexed and crates move by the whole stack
def realign_crates_by_stack(filename):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')

    list = initialize_stacks()

    # enumerate() will return an index and element
    for i, line in enumerate(lines):
        # skip the first 9 lines to get to the instructions
        if i < 10:
            continue

        # l[1] = how many to move
        # l[3] = where to move from
        # l[5] = where to move to
        # adjust for 0 indexing
        l = line.split(' ')
        move_qty = int(l[1])
        move_from = int(l[3])-1
        move_to = int(l[5])-1

        # pop each element off the stack and add it to the beginning
        # of the tmp_list, then append that tmp list to the new stack
        tmp_list = []
        for j in range(1,move_qty+1):
            tmp_list.insert(0,list[move_from].pop())

        # concat here, don't append
        # append will make a sublist
        list[move_to] += tmp_list
            
    file.close()

    # iterate across list and return top value of each crate
    result = ""
    for i in range(0,len(list)):
        result += list[i][-1]

    return result

print("Day 05-1 Output: ", realign_crates_one_at_a_time('input.txt'))
print("Day 05-2 Output: ", realign_crates_by_stack('input.txt'))