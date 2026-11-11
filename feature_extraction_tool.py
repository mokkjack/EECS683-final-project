#feature_extraction_tool.py

# === [Section 01] === #
# Python Library    
# ==================== #

import os
import sys
import csv


# === [Section 02] === #
# Python Functions    
# ==================== #

# Main Function
def main(argc, argv):
    #Local Variables
    CurrentOperation = "REGULAR"

    # Operation Switching
    if (argc == 2):
        if argv[1] == "test":
            print("\033[94mUsing Test Module\033[0m")
            CurrentOperation = "TEST"

    # Regular Operation
    if (CurrentOperation == "REGULAR"):
        outFile = open("out.csv", "w")
        while(True):
            fName = input("Name of file: ")
            try:
                f = open(fName, "r")
                break
            except:
                print("File not found")

        f.close()
        outFile.close()

    # Exit Program
    print("\033[93mTerminating Program\033[0m")
    return 0

# Start Main on Launch
if __name__ == "__main__":
    argc = len(sys.argv)
    argv = sys.argv
    main(argc, argv)