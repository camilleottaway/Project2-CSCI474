import os
import sys
from os import path
import numpy as np
import subprocess
import random
import string

def main():
    run = 0
    if(path.exists("results.csv")):
        name = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(5))
        os.rename("results.csv", "results:" + name + ".csv")
    
    for rnaught in np.round(np.arange(0.5, 4.5, 0.1), 2): #step size 0.1
        for cfr in np.round(np.arange(0.05, 0.55, .05), 2): #step size 0.05
            for dinf in np.arange(8, 13, 1): #step size 1
                for psev in np.round(np.arange(0.1, 0.81, 0.1), 2): #step size .1
                    modelargs = ["python3", "modelV3.py", "-R0", str(rnaught), "-CFR", str(cfr), "-dinf", str(dinf), "-PSEVERE", str(psev), "-N",  "278000", "-run", str(run)]
                    subprocess.run(modelargs)
                    print(str(modelargs))
                    run+=1

if __name__ == "__main__":
    main()
