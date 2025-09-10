with open("differencesP.txt", "w") as output: # open output file
    with open("AllCombinations.txt", "r") as file: # open combination file
        with open("CountP.txt", "r") as data: # open data file
            lines = file.readlines() # read combination file
            data = data.readlines() # read data file
            for i in range(1000): # remove \n at the end of each datum
                data[i] = int(data[i].strip())
            for i in range(184756 * 5): # parse through every combination
                sum = [0,0,0,0,0,0,0,0,0,0] # sum of counts from 10 file (each combination contains 10 file)
                line = lines[i].strip() # remove \n from combination
                group = line.split(",") # split the combination to each file e.g. "1,2,3," (str) to [1,2,3,""] (list)
                group.remove("") # remove the trailing ""
                for j in range(10): # change the list from str to int
                    group[j] = int(group[j])
                for j in range(10): # this for loop is for each file fro combination
                    for k in range(10): # this for loop is for going through the number in each file
                        sum[k] += data[group[j]*10 + k] # add the number to sum
                for j in range(10): # parse through the sum
                    sum[j] -= 10000 # find the differences from the sum to the theoretical each num is 10,000
                    if sum[j] < 0: # if the result is negative
                        sum[j] *= -1 # change to positive
                differences = 0 # total differences
                for j in range(10): # add the difference from each sum to the total
                    differences += sum[j]
                print(differences, file=output) # print the total to file