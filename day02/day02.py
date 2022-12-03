# Get total score using given rock-paper-scissor strategy
# A = Rock (Opponent)
# B = Paper (Opponent)
# C = Scissors (Opponent)
# X = Rock (self)
# Y = Paper (self)
# Z = Scissors (self)
# Scoring:
#   1 pt = Rock, 2 pt = Paper, 3 pt = Scissors
#   6 pt = win, 3 pt = tie, 0 pt = loss
def rps_score(filename):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')
    
    score = 0
    val_rock = 1
    val_paper = 2
    val_scissors = 3
    val_win = 6
    val_tie = 3
    val_loss = 0

    # create a dictionary with all possible results for easy lookup
    results_dict = {
        'AX': val_rock + val_tie,
        'AY': val_paper + val_win,
        'AZ': val_scissors + val_loss,
        'BX': val_rock + val_loss,
        'BY': val_paper + val_tie,
        'BZ': val_scissors + val_win,
        'CX': val_rock + val_win,
        'CY': val_paper + val_loss,
        'CZ': val_scissors + val_tie 
    }

    # enumerate() will return an index and element
    for i, line in enumerate(lines):
        #first character is opponent throw, third is my throw (space delimits)
        opponent_throw = line[0]
        self_throw = line[2]
        
        #look up throw combination in pre-built dict and add result to score
        score += results_dict[opponent_throw+self_throw] 
    file.close()

    return score

# Get total score using given rock-paper-scissor strategy
# Strategy updated where second character is indicator of needing to:
#   X = lose, Y = draw, Z = win
# Just need to update the dictionary lookup with this new information
def rps_score_update(filename):
    # open file for reading
    file = open(filename, 'r')
    # split file on newline into a list
    lines = file.read().split('\n')
    
    score = 0
    val_rock = 1
    val_paper = 2
    val_scissors = 3
    val_win = 6
    val_tie = 3
    val_loss = 0

    # create a dictionary with all possible results for easy lookup
    results_dict = {
        'AX': val_scissors + val_loss,
        'AY': val_rock + val_tie,
        'AZ': val_paper + val_win,
        'BX': val_rock + val_loss,
        'BY': val_paper + val_tie,
        'BZ': val_scissors + val_win,
        'CX': val_paper + val_loss,
        'CY': val_scissors + val_tie,
        'CZ': val_rock + val_win 
    }

    # enumerate() will return an index and element
    for i, line in enumerate(lines):
        #first character is opponent throw, third is my throw (space delimits)
        opponent_throw = line[0]
        self_throw = line[2]
        
        #look up throw combination in pre-built dict and add result to score
        score += results_dict[opponent_throw+self_throw] 
    file.close()

    return score

print("Day 02-1 Output: ", rps_score('input.txt'))
print("Day 02-2 Output: ", rps_score_update('input.txt'))