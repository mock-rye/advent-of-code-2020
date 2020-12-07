import re
tree = dict()
holds = set()
holdsnt = set()

def checkFromNode(tree, node):
    children = tree[node]
    if "no other" in children or node in holdsnt:
        holdsnt.add(node)
        return False
    if "shiny gold" in children or node in holds:
        holds.add(node)
        return True
    if True in [checkFromNode(tree, n) for n in children]:
        holds.add(node)
        return True

with open("07-input.txt", "r") as file:
    for line in file:
        line = [elem.strip() for elem in line.split('bags contain')]
        contents = [re.sub(r'bag(s?)|\d+|[.]','',elem).strip() for elem in line[1].split(',')]
        #one-liner cleanup
        container = line[0]
        tree[container] = contents

for key in tree:
    checkFromNode(tree, key)

print(len(holds))
