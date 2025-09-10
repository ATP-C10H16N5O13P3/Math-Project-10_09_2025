scoreP = 0
scoreT = 0
TotalComparison = 0
Times = [0, 0, 0, 0]

for i in range(4):
    with open(f"temp/temp{i}.txt", "r") as file:
        lines = file.readlines()
        temp = float(lines[3].strip())
        lines = [int(line.strip()) for line in lines if line.strip().isdigit()]
        lines.append(temp)
        if len(lines) < 4:
            print(f"File temp/temp{i}.txt does not have enough lines: {lines}")
            continue
        scoreP += lines[0]
        scoreT += lines[1]
        TotalComparison += lines[2]
        Times[i] = lines[3]

print(f"Score of Pseudorandom Generator: {scoreP}")
print(f"Score of Truly Random Generator: {scoreT}")
print(f"Total Score: {scoreP + scoreT}")
print(f"Total Comparison: {TotalComparison}")
print(f"Elapsed Time: {1363.3581183999995}")
print(f"Process 0 Elapsed Time: {Times[0]}")
print(f"Process 1 Elapsed Time: {Times[1]}")
print(f"Process 2 Elapsed Time: {Times[2]}")
print(f"Process 3 Elapsed Time: {Times[3]}")

with open("Score.txt", "a") as output:
    print(f"Score of Pseudorandom Generator: {scoreP}", file=output)
    print(f"Score of Truly Random Generator: {scoreT}", file=output)
    print(f"Total Score: {scoreP + scoreT}", file=output)
    print(f"Total Comparison: {TotalComparison}", file=output)
    print(f"Elapsed Time: {1363.3581183999995}", file=output)
    print(f"Process 0 Elapsed Time: {Times[0]}", file=output)
    print(f"Process 1 Elapsed Time: {Times[1]}", file=output)
    print(f"Process 2 Elapsed Time: {Times[2]}", file=output)
    print(f"Process 3 Elapsed Time: {Times[3]}", file=output)