test_str = '1-5 k: kkkkhkkkkkkkkkk'

split_string = test_str.split()

lower_and_upper = split_string[0].split('-')
lower = lower_and_upper[0]
upper = lower_and_upper[1]
print("Lower is: ", lower)
print("Upper is: ", upper)

target_letter = split_string[1][0:1]
print("Target letter is: ", target_letter)

password = split_string[2]
print("Password is: ", password)