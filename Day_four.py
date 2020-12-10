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

def valid_num(yr, upper, lower):
    if len(yr) == 4:
    # to be used for validating byr, iyr, eyr
        return lower <= int(yr) <= upper


def valid_pid(passport):
    pid_regex = '0[0-9a-f]{8}'
    print(pid_regex)
    if re.match(pid_regex, passport):
        return True
    else:
        return False

def valid_hcl(hcl):
    hcl_regex = '#[0-9a-z]{6}'
    if re.match(hcl_regex, hcl):
        return True


def valid_hgt(hgt):
    cm_regex = 'cm$'
    in_regex = 'in'
    result = re.match(cm_regex, hgt)
    if result:
        hgt = hgt.replace('cm','')
        return 150 <= int(hgt) <= 193
    else:
        print('why you not working?!?')

print('is this a valid height?: ', valid_hgt('175cm'))

print('is this year valid?: ', valid_num('1996', 2010, 1920))
print(valid_pid('012345abc'))
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
    print(list_of_dict[0])
    return d


dict_creator(y)
# a = ['Tests run: 1', ' Failures: 0', ' Errors: 0']

# d = {}
# for b in a:
#     i = b.split(': ')
#     d[i[0]] = i[1]
#
# print d