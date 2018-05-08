def almostIncreasingSequence(sequence):

    #Take out the edge cases
    if len(sequence) <= 2:
        return True

    #Set up a new function to see if it's increasing sequence
    def IncreasingSequence(test_sequence):
        if len(test_sequence) == 2:
            if test_sequence[0] < test_sequence[1]:
                return True
        else:
            for i in range(0, len(test_sequence)-1):
                if test_sequence[i] >= test_sequence[i+1]:
                    return False
                else:
                    pass
            return True

    for i in range (0, len(sequence) - 1):
        if sequence[i] >= sequence [i+1]:
            #Either remove the current one or the next one
            test_seq1 = sequence[:i] + sequence[i+1:]
            test_seq2 = sequence[:i+1] + sequence[i+2:]
            if IncreasingSequence(test_seq1) == True:
                return True
            elif IncreasingSequence(test_seq2) == True:
                return True
            else:
                return False
