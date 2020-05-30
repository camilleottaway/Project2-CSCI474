import os
import sys
import subprocess

def main():
    run = 0
    rnaughts = [0.8, 2.2]

    # Create folder to store generated text files
    newpath = os.getcwd()
    newpath = newpath + "\\v3\\rnaughts"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    os.chdir(newpath)

    # Generate R0 text files where social isolation is practiced
    # for x days on, 7 days off, x days on etc. where x is equal
    # to week
    for week in range(0, 52, 1):
        fname = "R" + str(week) + ".txt"
        fw = open(fname, 'w', newline='')
        rn = 0
        for day in range(0, 375, 7):
            start = rn
            if (week == 0):
                rn = rnaughts[1]
            elif (day % (week * 7) == 0):
                rn = rnaughts[1]
            else:
                rn = rnaughts[0]
            if (rn != start):
                l = f"day={day} R0={rn}\n"
                fw.write(l) 
        fw.write(f"day=400 R0={start}")
if __name__ == "__main__":
    main()
