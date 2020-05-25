# import modelV3.py
import os
import sys
import numpy as np

def main():
    f = open("results.txt","a+")
    for rnaught in np.round(np.arange(0.5, 4.5, 1.0), 2): #step size 0.1
        for cfr in np.round(np.arange(0.05, 0.5, .05), 2): #step size 0.05
            for dinf in np.arange(8, 12, 4): #???? 
                for psev in np.round(np.arange(0.1, 0.8, 0.2), 2): # ????
                    modelcall = "python3 modelV3.py "
                    modelcall += f"-r0 {rnaught} -cfr {cfr} -dinf {dinf} -psevere {psev}"
                    print(modelcall)
                    #os.system(modelcall)
                    #f.write("R0-" + str(rnaught))

if __name__ == "__main__":
    main()