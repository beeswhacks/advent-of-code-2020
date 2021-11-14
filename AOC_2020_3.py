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

# set off from position (0, 0), so we start counting from first move of (+3, +1)
x_position = 3
y_position = 1
tree_count = 0

while y_position <= number_of_rows - 1:
    if puzzle_input[y_position][x_position] == '#':
        tree_count += 1

    # if x_position is not within 3 of the end of the row, increase x_position by 3
    if x_position <= last_element - 3:
        x_position += 3
    # otherwise if x_position is within 3 of the end, move up by 3 and back by row length to start from beginning of row
    else:
        x_position += 3
        x_position -= row_length

    y_position += 1

print("Number of trees: " + str(tree_count))