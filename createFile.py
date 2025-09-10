for i in range(100): # create 100 file for data
    with open(f"data_true_random/data-{i}.txt", "w") as file: # creating the plain text file
        print(i) # print number of file to terminal