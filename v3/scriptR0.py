import os
import sys
import numpy as np
import subprocess
from os import path
import random
import string

def main():
    run = 0
    newpath = os.getcwd()
    print(newpath)

    if(path.exists("results.csv")):
        name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))
        os.rename("results.csv", "results:" + name + ".csv")

    for rnaught in range(0, 52, 1): #step size 0.1
        for cfr in np.round(np.arange(0.05, 0.55, .1), 2): #step size 0.05
            for dinf in np.arange(8, 13, 1): #step size 1
                for psev in np.round(np.arange(0.1, 0.81, 0.1), 2): #step size .1
                    modelargs = ["python3", "modelV3.py", "-decay", f"R{rnaught}.txt", "-CFR", str(cfr), "-dinf", str(dinf), "-PSEVERE", str(psev), "-N",  "278000", "-run", str(run)]
                    subprocess.run(modelargs)
                    print(str(modelargs))
                    run+=1

if __name__ == "__main__":
    main()
