f = open("input_files/passwords.txt", "r")
x = f.read()
passwords = x.split()
# print(passwords)

password = [passwords[x:x + 3] for x in range(0, len(passwords), 3)]


# print(password[0])
# print(len(passwords))
# print(len(password))

def password_character_number_checker(password_list_of_list):
    i = 0
    correct_passwords = 0
    for i in range(len(password_list_of_list)):
        # print(password_list_of_list[i])
        password_and_rules = password_list_of_list[i]
        # print(password_and_rules[j])
        allowed_range = password_and_rules[0].split('-')
        lower_bound = int(allowed_range[0])
        upper_bound = int(allowed_range[1])
        # print(lower_bound, upper_bound)
        required_char = password_and_rules[1][0]
        number_of_char = password_and_rules[2].count(required_char)
        # print(number_of_char)
        if lower_bound <= number_of_char <= upper_bound:
            correct_passwords += 1
        else:
            pass
        i = i + 1
    # return correct_passwords
    print("Number of correct passwords: based off of number of characters ", correct_passwords)


def password_character_placement_checker(password_list_of_list):
    i = 0
    correct_passwords = 0
    for i in range(len(password_list_of_list)):
        password_and_rules = password_list_of_list[i]
        allowed_range = password_and_rules[0].split('-')
        lower_bound = int(allowed_range[0]) - 1
        upper_bound = int(allowed_range[1]) - 1
        required_char = password_and_rules[1][0]
        single_password = password_and_rules[2]
        print(single_password)
        password_length = len(single_password)
        if upper_bound > password_length:
            pass
        if lower_bound > password_length:
            pass
        if single_password[lower_bound] == required_char and single_password[upper_bound] == required_char:
            pass
        elif single_password[lower_bound] == required_char or single_password[upper_bound] == required_char:
            correct_passwords += 1
        else:
            pass
        # 13 - 17 s: ssssssssssssgsssj
        # 7 - 9 p: pnlzhcppvl
    print("correct number of passwords based off of character placement: ", correct_passwords)


# password_character_number_checker(password)

password_character_placement_checker(password)
