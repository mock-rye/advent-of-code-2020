passportDict = {
#I have exactly zero clue why this needs to be initialized
#to all zeroes but it's what makes it work
    "byr": '0',
    "iyr": '0',
    "eyr": '0',
    "hgt": '0',
    "hcl": '0',
    "ecl": '0',
    "pid": '0',
    "cid": '0'
}
excluded = ["cid"]

def isValidPassport(passport):
    for key in passport:
        if not (passport[key] or key in excluded):
            return False
    return True

def solve(inList):
    approvedList = []
    for passport in inList:
        if isValidPassport(passport):
            approvedList.append(passport)
    return len(approvedList)

with open("04-input.txt", "r") as file:
    passportList = []
    for line in file:
        if line == '\n':
            passportList.append(passportDict)
            passportDict = {key: '' for key in passportDict}
            continue
        fields = [[thing for thing in l.split(':')] for l in line.split()]
        for key, value in fields:
            passportDict[key] = value

print(solve(passportList))
