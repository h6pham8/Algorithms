'''
Given: List[str]
Objective: return the shortest distance between two given words.
Note: word 1 and word 2 may be the same and they represent two individual words in the list
Return: int
'''


def shortest_word_dist(words, word1, word2):

    first_idx = None
    second_idx = None
    curr_min = None
    dup_counter = 0

    for idx, word in enumerate(words):
        if word is word1 and dup_counter == 0:
            first_idx = idx
            dup_counter = 1

        elif word is word2:
            second_idx = idx
            dup_counter = 0

        if first_idx is not None and second_idx is not None:
            if curr_min is None and first_idx - second_idx != 0:
                curr_min = abs(first_idx - second_idx)

            elif curr_min > abs(first_idx - second_idx) and first_idx - second_idx != 0:
                curr_min = abs(first_idx - second_idx)

    print curr_min
    return curr_min

shortest_word_dist(["a", "b"], "a", "b")


# examples
# ['a', 'b', 'b', 'b', 'a', 'z', 'a', 'b']

# case 1  -> standard
# case 2 -> standard, but then immediately after word 1 appears sooner
# case 3 -> same word