import re
tree = dict()

def checkFromNode(tree, node):
    if not tree[node]:
        result = 1
    else:
        result = sum([n[0]*checkFromNode(tree, n[1]) for n in tree[node]]) + 1
    return result

with open("07-input.txt", "r") as file:
    for line in file:
        line = [bit.strip() for bit in line.split('bags contain')]
        contents = [elem.replace('.','') for elem in line[1].split(', ')]
        contents = [elem.replace('bags','').replace('bag','') for elem in contents]
        if contents[0].strip() == "no other":
            contents = False
        else:
            contents = [[int(re.findall(r'\d+', elem)[0]), re.sub(r'\d+', '', elem)] for elem in contents]
            contents = [[elem[0], elem[1].strip()] for elem in contents]
        container = line[0]
        tree[container] = contents
##        print(container, contents)

##print(tree)

print(checkFromNode(tree, "shiny gold") - 1) ##had an off by one here lmfao

##print(len(holds))
