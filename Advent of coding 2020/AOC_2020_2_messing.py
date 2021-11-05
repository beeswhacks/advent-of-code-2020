test_str = '1-5 k: kkkkhkkkkkkkkkk'

entry = {
    "start"         : test_str[:test_str.index('-')],
    "end"           : test_str[test_str.index('-') + 1 : test_str.index(' ')],
    "target_letter" : test_str[test_str.index(':') - 1 : test_str.index(':')],
    "password"      : test_str[test_str.index(':') + 1 :]
}

print("Start = " + entry["start"])
print("End = " + entry["end"])
print("Target letter = " + entry["target_letter"])
print("Target = " + entry["password"])