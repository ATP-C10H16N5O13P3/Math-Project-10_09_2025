import itertools

# program to find all the combination from the binomial coefficient nCr(n,r)
n = 20
r = 10
elements = list(range(1, n + 1))

with open("AllCombinations.txt", "w") as file:
    for k in range(5):
        for combo in itertools.combinations(elements, r):
            # print(combo, file=file)
            for i in combo:
                print(str(i+20*k-1), end=",", file=file) # print the combination into a file with comma separating the num
            print("", file=file) # print to separate the combination