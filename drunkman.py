import random
import matplotlib.pyplot as plt

def firsttrial(num):
    pos = {
        "xpos": 0,
        "ypos": 0
    }
    for ind in range(num):
        if random.randint(0,1) == 1:
            if random.randint(0, 1) == 1:
                pos["xpos"] += 1
            else:
                pos["xpos"] -= 1
        elif random.randint(0, 1) == 1:
            pos["ypos"] += 1
        else:
            pos["ypos"] -= 1
    
        nm = (pos["xpos"]**2+pos["ypos"]**2)**0.5
        lstdis.append(nm)

def trial(num):
    pos = {
        "xpos": 0,
        "ypos": 0
    }
    for ind in range(num):
        if random.randint(0,1) == 1:
            if random.randint(0, 1) == 1:
                pos["xpos"] += 1
            else:
                pos["xpos"] -= 1
        elif random.randint(0, 1) == 1:
            pos["ypos"] += 1
        else:
            pos["ypos"] -= 1
    
        nm = (pos["xpos"]**2+pos["ypos"]**2)**0.5
        lstdis[ind] += nm

# Getting entries
num = input("No of experiments: ")
tr = input("No of steps: ")
lstdis = []
num = int(num)

# First trial creates the list, then adds other experiments results
firsttrial(int(tr))
for _ in range(num-1):
    trial(int(tr))

# Calculation of the average values
for ind in range(len(lstdis)):
    lstdis[ind] /= int(num)

# Plotting the graph
plt.plot(lstdis)
plt.show()
