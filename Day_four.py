f = open("input_files/passports.txt")
# print(f)
x = f.read().split('\n\n')
# print(x)
y = list(filter(None, x))

# print('List of passports = ', y)
import re

def valid_passport(list_of_passports, matches):
    valid = 0
    for passports in list_of_passports:
        # print('Passports = ', passports)
        print('Potential tuple?: ',re.split(' |\n', passports))
        if all(x in passports for x in matches):
            print('Valid Passport = ', passports)
            valid += 1
    print('number of valid passports: ', valid)


def valid_ecl(passport, matches):
    if any(ecl in passport for ecl in matches):
        return True
    else: return False

# def valid_4_digits(passport, lower, upper):
    # if passport

matches = ['ecl:', 'pid:', 'eyr:', 'hcl:', 'byr:', 'iyr:', 'hgt:']
# valid_passport(y, matches)
ecl_matches = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

# print(valid_ecl('bnnn',ecl_matches))

# user_email = 'braderz@amd.com'
# email_services = ["amb", "gmail", "yahoo"]
# email_contains_service = any(email_service in user_email for email_service in email_services)
#
# print(email_contains_service)
def dict_creator(list_of_strings):
    list_of_dict = []
    for passports in list_of_strings:
        individual_strings = re.split(' |\n', passports)
        d = {}
        for b in individual_strings:
            i = b.split(':')
            d[i[0]] = i[1]
        list_of_dict.append(d)
        # print(d)
    print(list_of_dict[0]['eyr'])
    return d


dict_creator(y)
# a = ['Tests run: 1', ' Failures: 0', ' Errors: 0']

# d = {}
# for b in a:
#     i = b.split(': ')
#     d[i[0]] = i[1]
#
# print d