import sys
import platform
import os
from importlib.metadata import version, PackageNotFoundError

# Python version
print("Python version:", sys.version)

# Platform info
print("Platform:", platform.platform())

# Current working directory
print("Working directory:", os.getcwd())

# Check package versions
packages = ["numpy", "pandas", "matplotlib", "scipy", "requests", "pytest"]
for pkg in packages:
    try:
        print(f"{pkg} version:", version(pkg))
    except PackageNotFoundError:
        print(f"{pkg} is NOT installed")