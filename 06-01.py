with open("06-input.txt", "r") as file:
#needs an extra newline character at input's EOF
#TODO: get that sorted
    result = 0
    st = set()
    for line in file:
        line = line.strip()
        [st.add(char) for char in line]
        if not line:
            result = result + len(st)
#            print(result, len(st), ''.join([elem for elem in sorted(st)]))
            st.clear()
print(result)
