#feature_extraction_tool.py

# === [Section 01]
# Python Library    
#

import csv


# 
# 
#

# Main Function
def main():
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
    print("the file is closed pookie bear")
    return 0

# Start Main on Launch
if __name__ == "__main__":
    main()