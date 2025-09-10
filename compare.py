import time

scoreP = 0
scoreT = 0
TotalComparison = 0

Pdifferences = None
with open("differencesP.txt", "r") as Pfile:
    Pdifferences = Pfile.readlines()
    for i in range(184756 * 5):
        Pdifferences[i] = int(Pdifferences[i].strip())

Tdifferences = None
with open("differencesT.txt", "r") as Tfile:
    Tdifferences = Tfile.readlines()
    for i in range(184756 * 5):
        Tdifferences[i] = int(Tdifferences[i].strip())

sTime = time.perf_counter()

for a in range(5):
    for i in range(184756 * a,184756 * (a + 1)):
        for j in range(184756 * a,184756 * (a + 1)):
            if Tdifferences[i] < Pdifferences[j]:
                scoreT += 1
            elif Pdifferences[i] < Tdifferences[j]:
                scoreP += 1
            else:
                TotalComparison += 1
        if (i + 1) % 100 == 0:
            tTime = time.perf_counter() - sTime
            print(f"Finished ({a}/5) {i + 1}/184756 Time: {tTime:.2}")

tTime = time.perf_counter() - sTime
print(f"Finished (5/5) 184756/184756 Time: {tTime:.2}")

TotalScore = scoreP + scoreT
TotalComparison += TotalScore

print(f"Score of Pseudorandom Generator: {scoreP}")
print(f"Score of Truly Random Generator: {scoreT}")
print(f"Total Score: {TotalScore}")
print(f"Total Comparison: {TotalComparison}")
print(f"Elapsed Time: {tTime}")

with open("Score.txt", "a") as output:
    print(f"Score of Pseudorandom Generator: {scoreP}", file=output)
    print(f"Score of Truly Random Generator: {scoreT}", file=output)
    print(f"Total Score: {TotalScore}", file=output)
    print(f"Total Comparison: {TotalComparison}", file=output)
    print(f"Elapsed Time: {tTime}", file=output)