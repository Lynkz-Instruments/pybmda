from pybmda.utils import BMDA
from pybmda import BMP, discover_bmps

# Testing BMDA
print("BMDA Version:", BMDA.version())
print("BMP object", BMP("Serial"))
print("List of connected BMPs:")
for bmp in discover_bmps():
    print(bmp.serial)
