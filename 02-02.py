counter = 0

with open("02-input.txt", "r") as file:
    for line in file:
        temp_list = line.split()
        pos = [int(i) for i in temp_list[0].split('-')]
        letter = temp_list[1].replace(':','')
        password = temp_list[2]
        first = pos[0] - 1
        second = pos[1] - 1
        if (password[first] == letter) != (password[second] == letter):
            counter = counter + 1
            
print(counter)
