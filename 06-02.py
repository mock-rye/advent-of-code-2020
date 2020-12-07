with open("06-input.txt", "r") as file:
    result = 0
    st = set()
    carryover = set("abcdefghijklmnopqrstuvwxyz")
    for group in file.read().split('\n\n'):
        for line in group.split():
#            print(line)
            st.clear()
            [st.add(char) for char in line]
            carryover = carryover.intersection(st)
#            print(carryover)
        result = result + len(carryover)
#        print()
        carryover = set("abcdefghijklmnopqrstuvwxyz")
print(result)
