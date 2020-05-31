import os
import sys
import csv
import numpy as np
import subprocess

def f(defaultValues):
    
    R0FilePath = defaultValues["R0FilePath"] 
    if (UseDecayingR0):
        arrayOfR0s = GetR0DecayValues(R0FilePath)
        if (arrayOfR0s == None):
            exit()

def main():

    with open('parametersR0.csv', 'w') as csvfile:
        fieldnames = ['R0', 'CFR', 'dinf', 'PSEVERE', 'N', 'run' ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

    run = 0
    newpath = os.getcwd()
    print(newpath)

    for rnaught in range(0, 52, 1): #step size 0.1
        for cfr in np.round(np.arange(0.05, 0.55, .1), 2): #step size 0.05
            for dinf in np.arange(8, 13, 1): #step size 1
                for psev in np.round(np.arange(0.1, 0.81, 0.1), 2): #step size .1
                    modelargs = ["python3", "modelV3.py", "-decay", f"R{rnaught}.txt", "-CFR", str(cfr), "-dinf", str(dinf), "-PSEVERE", str(psev), "-N",  "278000", "-run", str(run)]
                    subprocess.run(modelargs)
                    with open('parametersR0.csv', 'a+') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        params = {'R0': f"R{rnaught}.txt", 'CFR': cfr, 'dinf': dinf, 'PSEVERE': psev, 'N':  278000, 'run': run}
                        writer.writerow(params)
                    run+=1

if __name__ == "__main__":
    main()
