f = open("input_files/passports.txt")
# print(f)
x = f.read().split('\n\n')
# print(x)
y = list(filter(None, x))

print('List of passports = ', y)




def valid_passport(list_of_passports, matches):

    valid = 0
    for passports in list_of_passports:
        # print('Passports = ', passports)
        if all(x in passports for x in matches):
            print('Valid Passport = ', passports)
            valid += 1
    print('number of valid passports: ', valid)

def valid_ecl(ecl):
    ecl_regex = 'amb|blu|brn|gry|grn|hzl|oth'
    if ecl_regex in ecl:
        return True
    else: return False

matches = ['ecl:', 'pid:', 'eyr:', 'hcl:', 'byr:', 'iyr:', 'hgt:']
valid_passport(y, matches)

print(valid_ecl('gry'))
