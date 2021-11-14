# import product from math library to multiply list elements together
from math import prod

# read in puzzle input
with open('/Users/jack/Repos/advent-of-code-2020/AOC_2020_3_input.txt') as in_file:
    in_file_list = in_file.readlines()
    
# remove newline characters
puzzle_input = []
for i in in_file_list:
    puzzle_input.append(i.replace('\n',''))

row_length = len(puzzle_input[0])
last_element = row_length - 1
number_of_rows = len(puzzle_input)

# list of different increment schemes
increments = [
    {
        "x_increment" : 1,
        "y_increment" : 1
    },
    {
        "x_increment" : 3,
        "y_increment" : 1
    },
    {
        "x_increment" : 5,
        "y_increment" : 1
    },
    {
        "x_increment" : 7,
        "y_increment" : 1
    },
    {
        "x_increment" : 1,
        "y_increment" : 2
    },
]

tree_count_list = []
# loop through different increment schemes
for i in increments:
    x_position = i["x_increment"]
    y_position = i["y_increment"]
    tree_count = 0

    while y_position <= number_of_rows - 1:
        if puzzle_input[y_position][x_position] == '#':
            tree_count += 1

        # if x_position is not within 3 of the end of the row, increase x_position by 3
        if x_position <= last_element - i["x_increment"]:
            x_position += i["x_increment"]
        # otherwise if x_position is within 3 of the end, move up by 3 and back by row length to start from beginning of row
        else:
            x_position += i["x_increment"]
            x_position -= row_length

        y_position += i["y_increment"]

    print("Number of trees encountered for pattern (" + str(i["x_increment"]) + ", " + str(i["y_increment"])  + ") = " + str(tree_count))    
    tree_count_list.append(tree_count)

print("Number of trees: " + str(prod(tree_count_list)))