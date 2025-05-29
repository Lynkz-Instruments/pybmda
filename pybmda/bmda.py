"""Representation classes and helper functions"""

import re
from typing import List, Optional

from .utils import BMDA


def discover_bmps() -> List["BMP"]:
    """
    Return list of all BlackMagicProbes connected and detected by BMDA

    Returns:
        List of BMPs

    """
    bmps = []

    for line in BMDA.exec(args=["-l"]):
        match = re.search(r"\b7f[a-fA-F0-9]+\b", line, re.IGNORECASE)

        if match:
            bmp = BMP(match.group(0))
            bmps.append(bmp)

    return bmps


class BMP:
    """
    BlackMagicProbe representation from bmda
    """

    def __init__(self, serial: str) -> None:
        """
        Create new BlackMagicProbe instance

        Arguments:
            serial: Serial number of the BMP to connect to
        """
        self.serial: str = str(serial)
        return

    def Erase(self, hwreset: bool = False) -> None:
        args = ["-E"]
        args.extend(self._GetSerialArg())
        if hwreset:
            args.extend(["-C"])

        BMDA.exec(args=args)

    def Flash(self, filename: str, verify: bool = False, hwreset: bool = False) -> None:
        args = self._GetSerialArg()
        args.extend(["-w"])
        if verify:
            args.extend(["-V"])
        args.extend([filename])
        if hwreset:
            args.extend(["-C"])
        BMDA.exec(args=args)

    def _GetSerialArg(self) -> list:
        return ["-s", f"{self.serial}"]
