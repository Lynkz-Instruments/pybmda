"""Utilities around bmda binary"""

import os
import subprocess

BMDA_BINARY = "blackmagic-bmda"
WIN_EXE_SUFFIX = ".exe"

import os

if os.name == "nt":
    BMDA_BINARY = BMDA_BINARY + WIN_EXE_SUFFIX


class BMDA:
    _version = None

    @classmethod
    def version(cls) -> str:
        if cls._version is None:
            cmd = BMDA_BINARY.split(" ")
            cmd.append("-h")

            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            if result.returncode != 0:
                raise Exception("Error getting version from bmda")

            cls._version = result.stdout.split("\n", maxsplit=1)[0]
            cls._version = cls._version.replace("Black Magic Debug App v", "")

        return cls._version

    @classmethod
    def exec(cls, args: list = None, description: bool = False) -> list:
        cmd = BMDA_BINARY.split(" ")

        if args is not None:
            cmd += args.split()

        try:
            result = subprocess.run(cmd, capture_output=True, check=True)
            stdout = result.stdout.decode()

            return stdout.split("\n")
        except subprocess.CalledProcessError as exc:
            stdout = exc.stdout.decode()
            if stdout.startswith("No probes found"):
                return []

            raise Exception(f"BMDA failed: {stdout}") from exc
