import re
tree = dict()
holds = set()
holdsnt = set()

class child:
    def __init__(self, quantity, name):
        self.quantity = quantity
        self.name = name

def checkPt1(tree, node, lookFor):
    children = tree[node]
    if (not children) or (node in holdsnt):
        holdsnt.add(node)
        return False
    if (lookFor in [child.name for child in children]) or (node in holds):
        holds.add(node)
        return True
    if True in [checkPt1(tree, child.name, lookFor) for child in children]:
        holds.add(node)
        return True

def checkPt2(tree, node):
    children = tree[node]
    if not children:
        result = 1
    else:
        result = sum([child.quantity * checkPt2(tree, child.name) for child in children]) + 1
    return result

def part1(tree, lookFor):
    for key in tree:
        checkPt1(tree, key, lookFor)
    return len(holds)

def part2(tree, startFrom):
    return checkPt2(tree, startFrom) - 1
    # the minus one removes an off-by-one added by the starter bag
    

with open("07-input.txt", "r") as file:
    for line in file:
        line = [elem.strip() for elem in line.split('bags contain')]
        contents = [re.sub(r' *bag(s?) *|[.]','',elem) for elem in line[1].split(',')]
        if contents[0] == "no other":
            contents = False
        else:
            contents = [child(int(re.findall(r'\d+', elem)[0]), re.sub(r'\d+', '', elem).strip()) for elem in contents]
        container = line[0]
        tree[container] = contents

print(part1(tree, "shiny gold"))
print(part2(tree, "shiny gold"))
