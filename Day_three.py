f = open('input_files/tree_coords.txt')

tree_coords = f.read()
# # print(tree_coords)
# # print(tree_coords)
tree_list = tree_coords.splitlines()
# tree_list = [line.replace('\n','') for line in tree_list]
# print(tree_list)



def toboggan_traverse(tree_list):
    x = 0
    # y = 0
    trees = 0
    for lines in tree_list:
        # print('lines = ',lines)
        # print(x, len(lines), x%len(lines))
        if lines[x%len(lines)] == '#':
            trees += 1
        x += 3
        # y += 1
    print(trees)

def toboggan_traverse2(tree_list, right, down):
    x = 0
    y = 0
    trees = 0
    print('-----------', right, down, '---------------')
    for lines in tree_list[::down]:
        if lines[x%len(lines)] == '#':
            trees += 1
        x += right
    else: pass
    print(trees)
    return trees


toboggan_traverse(tree_list)

def multi_slope(slopes):
    trees = 1
    for slope in slopes:
        trees = trees * toboggan_traverse2(tree_list, slope[0], slope[1])
    print('multiplying the tres gives: ', trees)

# toboggan_traverse2(tree_list, 3, 2)

toboggan_traverse2(tree_list, 1, 1)
toboggan_traverse2(tree_list, 3, 1)
toboggan_traverse2(tree_list, 5, 1)
toboggan_traverse2(tree_list, 7, 1)
toboggan_traverse2(tree_list, 1, 2)

slopes = [(1,1), (3,1),(5,1),(7,1),(1,2)]

multi_slope(slopes)