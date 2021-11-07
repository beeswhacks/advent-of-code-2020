# read password policies into a list so that i can loop through them
with open('/Users/jack/Repos/side/Advent of coding 2020/AOC_2020_2_input.txt') as in_file:
    in_file_list = in_file.readlines()
    
# remove newline characters
for i in in_file_list:
    i = i.replace('\n','')
        
# parse each password policy into a dictionary object
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

print(valid_password_count, "passwords are valid.")