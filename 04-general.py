import re
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
regExDict = {
    "byr": r'19[2-9][0-9]|200[0-2]',
    "iyr": r'201\d|2020',
    "eyr": r'202\d|2030',
    "hgt": r'1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in',
    "hcl": r'#([0123456789abcdef]{6})',
    "ecl": r'amb|blu|brn|gry|grn|hzl|oth',
    "pid": r'\d{9}',
    "cid": r'.*'
}
regExDict = {key: re.compile(regExDict[key]) for key in regExDict}

excluded = ["cid"]
    
def isValidPassportFirst(passport):
    for key in passport:
        if not (passport[key] or key in excluded):
            return False
    return True

def isValidPassportSecond(passport, reDict):
    for key in passport:
        if not (reDict[key].fullmatch(passport[key])):
            return False
    return True

def part1(inList):
    approvedList = []
    for passport in inList:
        if(isValidPassportFirst(passport)):
           approvedList.append(passport)
    return len(approvedList)

def part2(inList, reDict):
    approvedList = []
    for passport in inList:
        if(isValidPassportSecond(passport, reDict)):
           approvedList.append(passport)
    return len(approvedList)

with open("04-input.txt", "r") as file:
    passportList = []
    for line in file:
        if line == '\n':
            passportList.append(passportDict)
            passportDict = {key: '' for key in passportDict}
            continue
        fields = [[element for element in segment.split(':')] for segment in line.split()]
        for key, value in fields:
            passportDict[key] = value

print(part1(passportList))
print(part2(passportList, regExDict))
