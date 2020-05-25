# import modelV3.py
import os
import sys

def main():
    f = open("results.txt","a+")
    for rnaught in range(0.5, 3.5, 1): #step size 0.1
        for cfr in range(0.05, 0.5, .1): #step size 0.05
            for dinf in range(0, 1): #????
                for psev in range(0.1, 0.8, 0.2): # ????
                    os.system('python3 modelV3.py -plot true')
                    f.write("R0-" + str(rnaught))

if __name__ == "__main__":
    main()