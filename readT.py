count = [0,0,0,0,0,0,0,0,0,0]
list(count)

# start and end file
start = 0
end = 100

with open("CountT.txt", "w") as CountT:
    for w in range(start, end):
        with open(f"data_true_random/data-{w}.txt", "r") as file:
            lines = file.readlines()
            count_per_file = [0,0,0,0,0,0,0,0,0,0]
            for i in range(500):
                line = lines[i].strip().split("\t")
                for num in line:
                    for k in range(10):
                        if k + 1 == int(num):
                            count[k] += 1
                            count_per_file[k] += 1
                            break
            for i in range(10):
                print(count_per_file[i], file=CountT)