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

num = input("No of experiments: ")
tr = input("No of steps: ")
lstdis = []
num = int(num)
firsttrial(int(tr))
for _ in range(num-1):
    trial(int(tr))

for ind in range(len(lstdis)):
    lstdis[ind] /= int(num)

plt.plot(lstdis)
plt.show()
