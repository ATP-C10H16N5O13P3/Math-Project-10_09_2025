count = [0,0,0,0,0,0,0,0,0,0]
list(count)

# start and end file
start = 0
end = 100

# open the file
with open("countP.txt", "w") as CountP:
    for i in range(start, end):
        with open(f"data_pseudorandom/data-{i}.txt", "r") as file:
            lines = file.readlines()
            count_per_file = [0,0,0,0,0,0,0,0,0,0]
            # parsing through the 10,000 lines
            for j in range(10000):
                # counting the num
                for k in range(10):
                    if k + 1 == int(lines[j].strip()):
                        count[k] += 1
                        count_per_file[k] += 1
                        break
            # print it out
            for j in range(10):
                print(count_per_file[j], file=CountP)