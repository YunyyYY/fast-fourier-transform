"""
This file can only be run as a module.
In the root directory run python tests.test_fft
"""

import os, sys
import pytest
from src import fft  # fft has been imported in __init__.py in src

def main():
    print(fft([1,2,3,4,5,6,7,8]))

if __name__ == "__main__":
	print(f"package name: {__package__}")
	print(f"name: {__name__}")
	print("Now run test:")
	main()
