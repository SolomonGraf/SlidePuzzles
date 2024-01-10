import os
import glob

def cleantemps():
    files = glob.glob('tempfiles/*')
    for f in files:
        os.remove(f)

if __name__ == "__main__":
    cleantemps()