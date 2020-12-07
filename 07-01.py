import re
tree = dict()
holds = set()
holdsnt = set()

def checkFromNode(tree, node):
    if "no other" in tree[node] or node in holdsnt:
        holdsnt.add(node)
        return False
    if "shiny gold" in tree[node] or node in holds:
        holds.add(node)
        return True
    if True in [checkFromNode(tree, n) for n in tree[node]]:
        holds.add(node)
        return True

with open("07-input.txt", "r") as file:
    for line in file:
        line = [bit.strip() for bit in line.split('bags contain')]
        contents = [elem.replace('.','') for elem in line[1].split(', ')]
        contents = [elem.replace('bags','').replace('bag','') for elem in contents]
        contents = [re.sub(r'\d+', '', elem) for elem in contents]
        contents = [elem.strip() for elem in contents]
        container = line[0]
        tree[container] = set(contents)
#        print(container, contents)

for key in tree:
    checkFromNode(tree, key)

print(len(holds))
