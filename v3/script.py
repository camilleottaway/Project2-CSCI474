import os
import sys
import numpy as np
import subprocess
import csv

def main():

    with open('parameters.csv', 'a+') as csvfile:
        fieldnames = ['-R0', '-CFR', '-dinf', '-PSEVERE', '-N', '-run' ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

    run = 0
    for rnaught in np.round(np.arange(0.5, 4.5, 0.1), 2): #step size 0.1
        for cfr in np.round(np.arange(0.05, 0.55, .05), 2): #step size 0.05
            for dinf in np.arange(8, 13, 1): #step size 1
                for psev in np.round(np.arange(0.1, 0.81, 0.1), 2): #step size .1
                    modelargs = ["python3", "modelV3.py", "-R0", str(rnaught), "-CFR", str(cfr), "-dinf", str(dinf), "-PSEVERE", str(psev), "-N",  "278000", "-run", str(run)]
                    subprocess.run(modelargs)
                    print(str(modelargs))
                    with open('parameters.csv', 'a+') as csvfile:
                        fieldnames = ['-R0', '-CFR', '-dinf', '-PSEVERE', '-N', '-run' ]
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        params = {'-R0': rnaught, '-CFR': cfr, '-dinf': dinf, '-PSEVERE': psev, '-N':  278000, '-run': run}
                        writer.writerow(params)
                    run += 1

if __name__ == "__main__":
    main()
