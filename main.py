# Test application for pybmda
# Copyright (c) 2025 Lynkz Instruments Inc. Amos, Qc Canada

from pybmda.utils import BMDA
from pybmda import BMP, discover_bmps

# Testing BMDA
print("BMDA Version:", BMDA.version())
print("BMP object", BMP("Serial"))
print("List of connected BMPs:")
bmplist = discover_bmps()
for bmp in bmplist:
    print(bmp.serial)
testbmp = BMP(bmplist[0].serial)
print("Erasing target")
testbmp.Erase(True)
print("Flashing target")
testbmp.Flash("test.bin", True, True)
