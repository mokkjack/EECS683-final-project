#test_tool.py

# === [Section 01] === #
# Python Library    
# ==================== #

from pathlib import Path
from time import sleep

# === [Section 02] === #
# Python Classes    
# ==================== #

# Test Tool Class
class TestTool:
    # Constructor Method
    def __init__(self):
        VerilogFiles = self._load()
        self.run_detail(VerilogFiles) # *Comment* this Line on Actual Test
        # self.run(VerilogFiles)    # *Uncomment* this Line on Actual Test

    # Load Method
    def _load(self):
        # Local Variables
        VerilogFolder = Path("VerilogFiles")
        VerilogList = []

        # Load Verilog into List
        for file in VerilogFolder.iterdir():
            VerilogList.append(file)

        return VerilogList

        
    
    # Ignore Comments Method
    def _ignore_c(self, line):
        inspect_line = line.split()

        # Empty Line
        if (len(inspect_line) == 0):
            return

        # Comment Line
        if (inspect_line[0].startswith("//")):
            return

        return line

    # Run Detail Method
    def run_detail(self, VerilogFolder):
        for file in VerilogFolder:
            current_file = open(file, "r")
            for raw_line in current_file:
                line = self._ignore_c(raw_line.strip())
                print(line)
            sleep(10)

            current_file.close()

        return

    # Run Method
    def run(self, VerilogFiles):
        print(f"\033[93mRunning Tests\033[0m\n")

    # String Method
    def __str__(self):
        pass

    # Representation Method
    def __repr__(self):
        pass