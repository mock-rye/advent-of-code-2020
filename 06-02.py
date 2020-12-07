with open("06-input.txt", "r") as file:
    result = 0
    st = set()
    carryover = set("abcdefghijklmnopqrstuvwxyz")
    for line in file:
        line = line.strip()
        if not line:
            result = result + len(carryover)
#            print(result, len(carryover), ''.join([elem for elem in sorted(carryover)]))
            carryover = set("abcdefghijklmnopqrstuvwxyz")
            continue
        [st.add(char) for char in line]
        carryover = carryover.intersection(st)
        st.clear()
print(result)
