import os
import sys
import numpy as np
import subprocess

def main():
    f = open("results.txt","a+")
    for rnaught in np.round(np.arange(0.5, 4.5, 1.0), 2): #step size 0.1
        for cfr in np.round(np.arange(0.05, 0.55, .05), 2): #step size 0.05
            for dinf in np.arange(8, 13, 1): #step size 1
                for psev in np.round(np.arange(0.1, 0.81, 0.1), 2): #step size .1
                    modelargs = ["python3 modelV3.py", f"-r0 {rnaught}",  f"-cfr {cfr}", f"-dinf {dinf}", f"-psevere {psev}", "-population 278000"]
                    f.write(modelargs[0] + modelargs[1] + modelargs[2] + modelargs[3] + modelargs[4] +"\n")
                    subprocess.run(modelargs)

if __name__ == "__main__":
    main()
