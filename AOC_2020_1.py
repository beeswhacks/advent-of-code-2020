# initialise puzzle input
puzzle_input = []

# get puzzle input from text file
with open('/Users/jack/Repos/advent-of-code-2020/AOC_2020_1_input.txt') as in_file:

    # use readlines to split text file into list
    in_file_list = in_file.readlines()

    # remove newline characters and convert string values to integers
    for i in in_file_list:
        puzzle_input.append(int(i.replace('\n','')))

# PART ONE: finding two numbers that sum to 2020

# for each item in the puzzle input
for i in range(len(puzzle_input)):
    # loop through the remaining puzzle items
    for j in range(len(puzzle_input)):
        # check if the sum of the two elements is 2020, and that the two elements aren't identical
        if i != j and (puzzle_input[i] + puzzle_input[j]) == 2020:
            first_value = puzzle_input[i]
            second_value = puzzle_input[j]            
            answer = puzzle_input[i] * puzzle_input[j]
            break

print("First value: ", first_value)
print("Second value: ", second_value)
print("Answer: ", answer)
print("\n")

# PART TWO: finding three numbers that sum to 2020

# for each item in the puzzle input
for i in range(len(puzzle_input)):
    # loop through the remaining puzzle items
    for j in range(len(puzzle_input)):
        # and for each combination of the first two, loop through the remaining puzzle items again
        for k in range(len(puzzle_input)):
            # check if the sum of the three elements is 2020, and that the three elements aren't identical
            if i != j and j != k and i != k and (puzzle_input[i] + puzzle_input[j] + puzzle_input[k]) == 2020:
                first_value = puzzle_input[i]
                second_value = puzzle_input[j]  
                third_value = puzzle_input[k]            
                answer = puzzle_input[i] * puzzle_input[j] * puzzle_input[k]
                break

print("First value: ", first_value)
print("Second value: ", second_value)
print("Third value: ", third_value)
print("Answer: ", answer)
print("\n")