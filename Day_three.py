f = open('input_files/tree_coords.txt')

tree_coords = f.read()
# # print(tree_coords)
# # print(tree_coords)
tree_list = tree_coords.splitlines()
# tree_list = [line.replace('\n','') for line in tree_list]
print(tree_list)



def tabogen_traverse(tree_list):
    x = 0
    # y = 0
    trees = 0
    for lines in tree_list:
        print(x, len(lines), x%len(lines))
        if lines[x%len(lines)] == '#':
            trees += 1
        x += 3
        # y += 1
    print(trees)





tabogen_traverse(tree_list)
