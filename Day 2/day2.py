path_name = 'puzzle_input_day2.txt'

#Part 1
'''
items = {}
f = open("puzzle_input_day2.txt")
count_valid = 0
passwds = f.readlines()
for line in passwds:
    strip_line = line.replace("-", " ")
    policy, passwd = strip_line.split(":")
    items[policy.strip()] = passwd.strip()
    c_range = [int(i) for i in policy.split() if i.isdigit()]
    letter = [str(i) for i in policy.split() if i.isalpha()]
    letter = letter[0]
    if letter in passwd:
        if passwd.count(letter) in range (c_range[0], c_range[1]+1):
            count_valid = count_valid+1
            print(count_valid)
f.close()
'''

#Part 2
items = {}
f = open("puzzle_input_day2.txt")
count_valid = 0
passwds = f.readlines()
for line in passwds:
    strip_line = line.replace("-", " ")
    policy, passwd = strip_line.split(":")
    items[policy.strip()] = passwd.strip()
    c_range = [int(i) for i in policy.split() if i.isdigit()]
    letter = [str(i) for i in policy.split() if i.isalpha()]
    letter = letter[0]

    if letter in passwd:
        if letter in passwd[c_range[0]] or letter in passwd[c_range[1]]:
            if not(letter in passwd[c_range[0]] and letter in passwd[c_range[1]]):
                count_valid = count_valid + 1

print(count_valid)
f.close()
