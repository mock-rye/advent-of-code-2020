counter = 0

with open("02-input.txt", "r") as file:
    for line in file:
        temp_list = line.split()
        lims = [int(i) for i in temp_list[0].split('-')]
        letter = temp_list[1].replace(':','')
        password = temp_list[2]
        if password.count(letter) in range(lims[0], lims[1]+1):
            counter = counter + 1
            
print(counter)
