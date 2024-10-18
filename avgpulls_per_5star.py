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
    repetitionCount = 140605
    game = "HSR" # "Genshin" or "HSR"
    guaranteed = False
    totalRaidenPullCount = [0] * 7
    for repetitionIndex in range(repetitionCount):
        sessionRaidenPullCount = [0] * 7
        currentGuaranteed = guaranteed
        sessionPulls = 0
        raidenCount = 0
        while raidenCount <= 6:
            sessionPulls += pull()
            if fiftyfifty_won(currentGuaranteed, game):
                sessionRaidenPullCount[raidenCount] = sessionPulls
                raidenCount += 1
                currentGuaranteed = False
            else:
                currentGuaranteed = True
        # end of session
        for index in range(7):
            totalRaidenPullCount[index] += sessionRaidenPullCount[index]
        if repetitionIndex % (repetitionCount // 10) == 0:
            progress = 100 * repetitionIndex // repetitionCount
            print(f"{progress}% Done!")
    # end of simulation
    print()
    print("[Pull Count Mean]")
    for index in range(7):
        if game == "Genshin": print(end="C")
        elif game == "HSR":   print(end="E")
        print(end=f"{index}: ")
        print("{:.2f}".format(totalRaidenPullCount[index]/repetitionCount))

def pull():
    n = 0
    seed = random.random()
    for n in range(90):
        n += 1
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

# RESULT IS ROUGHLY ALWAYS THE SAME.

# CALCULATED EXACT VALUES:
# Avg: 61.50255321109338
# Avg with Losses: 87.86079030 (HSR) (Difference is 10/7)
# Avg with Losses: 89.17870216 (Genshin) (Difference is 1.45)
'''
[Pull Count Calculated Mean] (HSR)
E0: 87.86
E1: 175.72
E2: 263.58
E3: 351.44
E4: 439.30
E5: 527.16
E6: 615.02
''''''
[Pull Count Calculated Mean] (Genshin)
E0: 89.18
E1: 178.36
E2: 267.54
E3: 356.71
E4: 445.89
E5: 535.07
E6: 624.25
'''






'''
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
    guaranteed = False
    totalPulls = 0
    totalRaidenPullCount = [0] * 7
    for repetitionIndex in range(repetitionCount):
        # end of session
        totalPulls += pull()
        if repetitionIndex % (repetitionCount // 10) == 0:
            progress = 100 * repetitionIndex // repetitionCount
            print(f"{progress}% Done!")
    # end of simulation
    print()
    print(f"Avg: {totalPulls/repetitionCount}")

def pull():
    n = 0
    seed = random.random()
    for n in range(90):
        n += 1
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
'''