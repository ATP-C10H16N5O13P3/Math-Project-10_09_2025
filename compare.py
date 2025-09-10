import multiprocessing
import time
import os

global Pdifferences
with open("differencesP.txt", "r") as Pfile:
    Pdifferences = Pfile.readlines()
    for i in range(184756 * 5):
        Pdifferences[i] = int(Pdifferences[i].strip())

global Tdifferences
with open("differencesT.txt", "r") as Tfile:
    Tdifferences = Tfile.readlines()
    for i in range(184756 * 5):
        Tdifferences[i] = int(Tdifferences[i].strip())

def compare(offset):
    try:
        # Ensure temp directory exists
        os.makedirs("temp", exist_ok=True)
        scoreP = 0
        scoreT = 0
        TotalComparison = 0

        sTime = time.perf_counter()
        with open(f"temp/temp{offset}.txt", "w") as temp:
            # print("123", file=temp); print("123", file=temp); print("123", file=temp); print("123", file=temp);
            # Full run: all 5 blocks, full range
            for a in range(5):
                total_i = ((184756 * (a + 1)) - (184756 * a + offset) + 3) // 4  # total steps for this block
                for idx, i in enumerate(range(184756 * a + offset, 184756 * (a + 1), 4)):
                    for j in range(184756 * a + offset, 184756 * (a + 1)):
                        if Tdifferences[i] < Pdifferences[j]:
                            scoreT += 1
                        elif Pdifferences[i] < Tdifferences[j]:
                            scoreP += 1
                        else:
                            TotalComparison += 1
                    # Print progress every 100 i-steps
                    if (idx + 1) % 100 == 0:
                        print(f"Process {offset} ({a}/5) completed {idx+1}/{total_i}")
            print(scoreP, file=temp)
            print(scoreT, file=temp)
            print(scoreP + scoreT + TotalComparison, file=temp)
            print(time.perf_counter() - sTime, file=temp)
    except Exception as e:
        print(f"Process {offset} error: {e}")

sTime = time.perf_counter()

if __name__ == "__main__":
    inputs = [0,1,2,3]
    processes = []

    for i in inputs:
        p = multiprocessing.Process(target=compare, args=(i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

    tTime = time.perf_counter() - sTime

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
    print(f"Elapsed Time: {tTime}")
    print(f"Process 0 Elapsed Time: {Times[0]}")
    print(f"Process 1 Elapsed Time: {Times[1]}")
    print(f"Process 2 Elapsed Time: {Times[2]}")
    print(f"Process 3 Elapsed Time: {Times[3]}")

    with open("Score.txt", "a") as output:
        print(f"Score of Pseudorandom Generator: {scoreP}", file=output)
        print(f"Score of Truly Random Generator: {scoreT}", file=output)
        print(f"Total Score: {scoreP + scoreT}", file=output)
        print(f"Total Comparison: {TotalComparison}", file=output)
        print(f"Elapsed Time: {tTime}", file=output)
        print(f"Process 0 Elapsed Time: {Times[0]}", file=output)
        print(f"Process 1 Elapsed Time: {Times[1]}", file=output)
        print(f"Process 2 Elapsed Time: {Times[2]}", file=output)
        print(f"Process 3 Elapsed Time: {Times[3]}", file=output)