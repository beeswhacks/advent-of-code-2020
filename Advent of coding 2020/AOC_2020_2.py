# firstly, need to get a list where each element is a list containing: lower lim, upper lim, letter, and password
puzzle_input = []

with open('/Users/jack/Repos/side/Advent of coding 2020/AOC_2020_2_input.txt') as in_file:
    in_file_list = in_file.readlines()
    
for i in in_file_list:
    puzzle_input.append(i.replace('\n',''))

puzzle_input_split_raw = []
puzzle_input_split = []
for count, i in enumerate(puzzle_input):
    puzzle_input_split_raw.append(i.split())
    puzzle_input_split[0] = puzzle_input_split_raw[0]
#    list_of_lists[count] = split(i)
        
print(puzzle_input_split)
# loop through passwords

# if the password meets the requirements, increment by 1