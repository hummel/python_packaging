# standard_lib.py
# Jacob Hummel
# Created 2018-09-05
"""
Dummy package for demonstrating how to package up python code for distribution.
"""
import os
def get_cwd():
    """Dummy function."""
    print("\nHello World!")
    print("Working directory:", os.getcwd(), "\n")
    return 42

if __name__ == '__main__':
    get_cwd()
