with open("06-input.txt", "r") as file:
    result = 0
    st = set()
    for group in file.read().split('\n\n'):
        for line in group.split():
#            print(line)
            line = line.strip()
            [st.add(char) for char in line]
        result = result + len(st)
        st.clear()
print(result)
