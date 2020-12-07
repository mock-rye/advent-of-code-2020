import re
tree = dict()

class child:
    def __init__(self, quantity, name):
        self.quantity = quantity
        self.name = name
    

def checkFromNode(tree, node):
    children = tree[node]
    if not children:
        result = 1
    else:
        result = sum([child.quantity * checkFromNode(tree, child.name) for child in children]) + 1
    return result

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
##        print(container, contents)

##print(tree)

print(checkFromNode(tree, "shiny gold") - 1) ##had an off by one here lmfao

##print(len(holds))
