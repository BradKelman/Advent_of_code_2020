f = open("input_files/passports.txt")
# print(f)
x = f.read().split('\n\n')
# print(x)
y = list(filter(None, x))

# Part one
def valid_passport(list_of_passports, matches):
    valid = 0
    for passports in list_of_passports:
        # print('Passports = ', passports)
        if all(x in passports for x in matches):
            print('Valid Passport = ', passports)
            valid += 1
    print('number of valid passports: ', valid)

# matches = ['ecl:', 'pid:', 'eyr:', 'hcl:', 'byr:', 'iyr:', 'hgt:']
# valid_passport(y, matches)

# ----------------------------------------------------
# Part two

import re

def valid_ecl(passport):
    ecl_matches = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    if any(ecl in passport for ecl in ecl_matches):
        return True
    else: return False

def valid_num(yr, upper, lower):
    if len(yr) == 4:
    # to be used for validating byr, iyr, eyr
        return lower <= int(yr) <= upper


# print(valid_num('1923',2010,1920))

def valid_pid(passport):
    pid_regex = '0[0-9a-f]{8}'
    # print(pid_regex)
    if re.match(pid_regex, passport):
        return True
    else:
        return False

def valid_hcl(hcl):
    hcl_regex = '#[0-9a-z]{6}'
    if re.match(hcl_regex, hcl):
        return True


def valid_hgt(hgt):
    cm_regex = 'cm'
    in_regex = 'in'
    cm = re.search(cm_regex, hgt)
    inch = re.search(in_regex, hgt)
    if cm:
        hgt = hgt.replace('cm','')
        return 150 <= int(hgt) <= 193
    elif inch:
        hgt = hgt.replace('in','')
        return 59 <= int(hgt) <= 76
    else:
        return False

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
    # print(list_of_dict[0])
    return list_of_dict



def main(list_of_passports):

    valid = 0
    # print(list_of_passports)
    dictionary_of_passports = dict_creator(list_of_passports)
    # print(dictionary_of_passports)
    for passports in dictionary_of_passports:
        valid_passport = True
        # print(passports)
        ecl = [val for key, val in passports.items() if 'ecl' in key]
        byr = [val for key, val in passports.items() if 'byr' in key]
        eyr = [val for key, val in passports.items() if 'eyr' in key]
        iyr = [val for key, val in passports.items() if 'iyr' in key]
        pid = [val for key, val in passports.items() if 'pid' in key]
        hcl = [val for key, val in passports.items() if 'hcl' in key]
        hgt = [val for key, val in passports.items() if 'hgt' in key]
        if ecl != [] and valid_passport == True:
            if valid_ecl(ecl) == True:
                valid_passport = True
            else:
                valid_passport = False
        if byr != [] and valid_passport == True:
            # print(byr)
            if valid_num(byr,2010, 1920) == True:
                valid_passport = True
            else:
                valid_passport = False
        if eyr != [] and valid_passport == True:
            if valid_num(eyr,2030, 2020):
                valid_passport = True
            else:
                valid_passport = False
        if iyr != [] and valid_passport == True:
            if valid_num(iyr,2020, 2010):
                valid_passport = True
            else:
                valid_passport = False
        if pid != [] and valid_passport == True:
            if valid_ecl(pid) == True:
                valid_passport = True
            else:
                valid_passport = False
        if hcl != [] and valid_passport == True:
            if valid_ecl(hcl) == True:
                valid_passport = True
            else:
                valid_passport = False
        if hgt != [] and valid_passport == True:
            if valid_ecl(hgt) == True:
                valid_passport = True
            else:
                valid_passport = False
        if valid_passport == True:
            valid =+ 1
    print('valid_passports:', valid)

        # print(ecl)
        # print(byr)
        # print(eyr)
        # print(lyr)
        # print(pid)
        # print(hcl)
        # print(hgt)



# Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
# Boys = {'Tim': 18,'Charlie':12,'Robert':25}
# Girls = {'Tiffany':22}
# for key in list(Dict.keys()):
#     if key in list(Boys.keys()):
#         print(True)
#     else:
#         print(False)

# dict_creator(y)

main(y)