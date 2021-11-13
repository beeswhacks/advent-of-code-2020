from operator import xor

# ------------------------------ PART 1 ------------------------------
# In part 1, the password is valid if the number of instances of the 
# target letter in the password is within a given window.

# read password policies into a list so that i can loop through them
with open('/Users/jack/Repos/advent-of-code-2020/AOC_2020_2_input.txt') as in_file:
    in_file_list = in_file.readlines()
    
# remove newline characters
for i in in_file_list:
    i = i.replace('\n','')
        
# parse each password policy into a dictionary object.
# puzzle_input is a list of dictionary objects, meaning
# the components of each policy can be referenced by name, and
# each individual policy can be referenced by number e.g.
# the target letter of the nth password policy can be accessed
# as puzzle_input[n]["target_letter"]. 
puzzle_input = []
for i in in_file_list:
    puzzle_input.append({
    "lower_lim"     : int(i[:i.index('-')]),
    "upper_lim"     : int(i[i.index('-') + 1 : i.index(' ')]),
    "target_letter" : i[i.index(':') - 1 : i.index(':')],
    "password"      : i[i.index(':') + 1 :]
    })

# loop through password policies
valid_password_count = 0
for i in puzzle_input:
    # count instances of target letter in each policy
    target_letter_count = i["password"].count(i["target_letter"])
    # count how many passwords meet the policy requirements
    if target_letter_count >= i["lower_lim"] and target_letter_count <= i["upper_lim"]:
        valid_password_count += 1

print(valid_password_count, "passwords are valid in part 1.")

# ------------------------------ PART 2 ------------------------------
# In part 2, the password is valid if the target letter is at only one 
# of two specified positions in the password. The first position is given
# by lower_lim, the second position is given by upper_lim. 

valid_password_count = 0
for i in puzzle_input:

    # check if target letter is at position 1
    if i["password"][i["lower_lim"]] == i["target_letter"]:
        position_1 = True
    else:
        position_1 = False

    # check if target letter is at position 2
    if i["password"][i["upper_lim"]] == i["target_letter"]:
        position_2 = True
    else:
        position_2 = False

    # mark password valid if target letter appears in one position only
    password_valid = xor(position_1,position_2)

    if password_valid == True:
        valid_password_count += 1

print(valid_password_count, "passwords are valid in part 2.")