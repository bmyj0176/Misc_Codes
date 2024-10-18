import random

standardPity = [
    0.00600, 0.00596, 0.00592, 0.00591, 0.00586, 0.00582, 0.00579, 0.00575, 0.00571, 0.00568, 
    0.00565, 0.00561, 0.00558, 0.00554, 0.00552, 0.00549, 0.00545, 0.00541, 0.00539, 0.00536,
    0.00531, 0.00528, 0.00525, 0.00523, 0.00519, 0.00517, 0.00513, 0.00511, 0.00507, 0.00503,
    0.00501, 0.00498, 0.00495, 0.00491, 0.00489, 0.00486, 0.00483, 0.00480, 0.00477, 0.00475,
    0.00471, 0.00469, 0.00467, 0.00464, 0.00461, 0.00457, 0.00456, 0.00453, 0.00448, 0.00447,
    0.00445, 0.00442, 0.00439, 0.00437, 0.00434, 0.00430, 0.00428, 0.00426, 0.00423, 0.00420,
    0.00418, 0.00416, 0.00413, 0.00410, 0.00408, 0.00406, 0.00404, 0.00401, 0.00399, 0.00396,
    0.00393, 0.00392, 0.00388, 0.00387, 0.00384, 0.20627, 0.13946, 0.09429, 0.06375, 0.04306,
    0.02914, 0.01970, 0.01332, 0.00901, 0.00608, 0.00411, 0.00278, 0.00187, 0.00126, 0.00265,
]
cumulativePity = [
    0.00600, 0.01196, 0.01788, 0.02379, 0.02965, 0.03547, 0.04126, 0.04701, 0.05272, 0.05840, 
    0.06405, 0.06966, 0.07524, 0.08078, 0.08630, 0.09179, 0.09724, 0.10265, 0.10804, 0.11340,
    0.11871, 0.12399, 0.12924, 0.13447, 0.13966, 0.14483, 0.14996, 0.15507, 0.16014, 0.16517,
    0.17018, 0.17516, 0.18011, 0.18502, 0.18991, 0.19477, 0.19960, 0.20440, 0.20917, 0.21392,
    0.21863, 0.22332, 0.22799, 0.23263, 0.23724, 0.24181, 0.24637, 0.25090, 0.25538, 0.25985,
    0.26430, 0.26872, 0.27311, 0.27748, 0.28182, 0.28612, 0.29040, 0.29466, 0.29889, 0.30309,
    0.30727, 0.31143, 0.31556, 0.31966, 0.32374, 0.32780, 0.33184, 0.33585, 0.33984, 0.34380,
    0.34773, 0.35165, 0.35553, 0.35940, 0.36324, 0.56951, 0.70897, 0.80326, 0.86701, 0.91007,
    0.93921, 0.95891, 0.97223, 0.98124, 0.98732, 0.99143, 0.99421, 0.99608, 0.99734, 1.00000,
]

def main():
    repetitionCount = 14000605
    game = "HSR" # "Genshin" or "HSR"
    pullCount = 419 # 273 for raiden
    guaranteed = False
    raidenCountTotal = 0
    keqingCountTotal = 0
    minRaidenCount = 1024
    minKeqingCount = 1024
    raidenCountDistribution = [0] * 1024
    keqingCountDistribution = [0] * 1024
    maxRaidenCount = 0
    maxKeqingCount = 0
    for repetitionIndex in range(repetitionCount):
        currentPullCount = pullCount
        currentGuaranteed = guaranteed
        currentRaidenCount = 0
        currentKeqingCount = 0
        currentRemainingPity = 0
        while currentPullCount > 0:
            pullsUsed = pull()
            if pullsUsed <= currentPullCount:
                currentPullCount -= pullsUsed
                if fiftyfifty_won(currentGuaranteed, game):
                    currentRaidenCount += 1
                    currentGuaranteed = False
                else:
                    currentKeqingCount += 1
                    currentGuaranteed = True
            else:
                currentRemainingPity = currentPullCount
                currentPullCount = 0
        # end of pulling cycle
        #print(f"[Session {repetitionIndex+1}] Raidens: {currentRaidenCount}, Keqings: {currentKeqingCount}, Remaining pity: {currentRemainingPity}")
        #print(f"if {repetitionIndex} % {repetitionCount/10} == 0:")
        if repetitionIndex % (repetitionCount // 10) == 0:
            progress = 100 * repetitionIndex // repetitionCount
            print(f"{progress}% Done!")
        raidenCountTotal += currentRaidenCount
        keqingCountTotal += currentKeqingCount
        raidenCountDistribution[currentRaidenCount] += 1
        keqingCountDistribution[currentKeqingCount] += 1
        if currentRaidenCount < minRaidenCount: minRaidenCount = currentRaidenCount
        if currentKeqingCount < minKeqingCount: minKeqingCount = currentKeqingCount
        if currentRaidenCount > maxRaidenCount: maxRaidenCount = currentRaidenCount
        if currentKeqingCount > maxKeqingCount: maxKeqingCount = currentKeqingCount
    # end of simulation
    print()
    print(f"[Session Count: {repetitionCount}, Pulls Per Session: {pullCount}, Start as Guaranteed: {guaranteed}]")
    print(f"[Mean] Raidens: {raidenCountTotal/repetitionCount}, Keqings: {keqingCountTotal/repetitionCount}")
    print(end=f"[Raiden Count Distribution] ")
    for count in range(minRaidenCount, maxRaidenCount+1): 
        print(end=f"{count}: {fraction_to_percentage(raidenCountDistribution[count], repetitionCount)}% | ")
    print()
    print(end=f"[Keqing Count Distribution] ")
    for count in range(minKeqingCount, maxKeqingCount+1): 
        print(end=f"{count}: {fraction_to_percentage(keqingCountDistribution[count], repetitionCount)}% | ")

def pull():
    n = 0
    seed = random.random()
    for n in range(90):
        if seed <= cumulativePity[n]:
            return n

def fiftyfifty_won(guaranteed, game):
    if guaranteed:
        return True
    seed = random.random()
    if seed <= 0.55 and game == "Genshin" or seed <= 4/7 and game == "HSR":
        return True
    else:
        return False

def fraction_to_percentage(sample, total):
    return round((sample/total)*100, 2)

if __name__ == "__main__":
    main()

# [Session Count: 14000605, Pulls Per Session: 419, Start as Guaranteed: False]
# [Mean] Raidens: 4.395004430165696, Keqings: 2.0124193204507947
# [Raiden Count Distribution] 2: 1.66% | 3: 19.44% | 4: 36.44% | 5: 27.36% | 6: 11.28% | 7: 3.07% | 8: 0.62% | 9: 0.1% | 10: 0.01% | 11: 0.0% | 12: 0.0% | 13: 0.0% |
# [Keqing Count Distribution] 0: 3.27% | 1: 23.31% | 2: 45.67% | 3: 24.54% | 4: 3.08% | 5: 0.13% | 6: 0.0% | 7: 0.0% |