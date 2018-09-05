# my_pypackage.py
# Jacob Hummel
# Created 2018-09-05
"""
Dummy package for demonstrating how to package up python code for distribution.
"""
import os
def main():
    """Dummy function."""
    print("Hello World!")
    print("Working directory:", os.getcwd())
    return 42

if __name__ == '__main__':
    main()
