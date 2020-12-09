def sumIn(lst, number):
    for l in lst:
        for j in lst:
            if l + j == number:
                return True
    return False

numbers = list()
with open("09-input.txt", "r") as file:
    inp = file.read().strip().split('\n')
    preamble = [int(elem) for elem in inp[0:25]]
    nums = [int(elem) for elem in inp[25:]]
#    print(preamble)
#    print(nums)
    for num in nums:
        if not sumIn(preamble, num):
            print(num)
        preamble.pop(0)
        preamble.append(num)
