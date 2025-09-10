import random

times = 10000 # 10,000 number per file
num = None

for i in range(100): # generate 100 file
    with open(f"data_pseudorandom/data-{i}.txt", "w") as file:
        for i in range(times): # repeat it times amount
            num = random.randint(1,10) # random number gen
            print((num), file=file) # print to file