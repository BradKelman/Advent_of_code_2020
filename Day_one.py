f = open("input_files/expense_report.txt", "r")

x = f.read()
# print(type(x))
y = x.split()
# print(y)


def equal_2020_2_nums(list_of_nums):
    i = 0
    j = 0
    # print('i ', 'j)
    for i in range(len(list_of_nums)):
        for j in range(len(list_of_nums)):
            if list_of_nums[i] == list_of_nums[j]:
                # print(i, j)
                pass
            elif int(list_of_nums[i]) + int(list_of_nums[j]) == 2020:
                print("This is the number you are looking for", int(list_of_nums[i]) * int(list_of_nums[j]))
                break
            else:
                # print(i, j, list_of_nums[i], list_of_nums[j], int(list_of_nums[i]) + int(list_of_nums[j]))
                # print(i, j)
                pass
            j += 1
        i = i + 1

def equal_2020_3_nums(list_of_nums):
    i = 0
    j = 0
    k = 0
    # print('i ', 'j)
    for i in range(len(list_of_nums)):
        for j in range(len(list_of_nums)):
            for k in range(len(list_of_nums)):
                if int(list_of_nums[i]) + int(list_of_nums[j]) + int(list_of_nums[k]) == 2020:
                    print("This is the number you are looking for", int(list_of_nums[i]) * int(list_of_nums[j]) * int(list_of_nums[k]))
                    break
                else:
                    pass
            j += 1
        i = i + 1
# equal_2020_2_nums(y)
equal_2020_3_nums(y)

