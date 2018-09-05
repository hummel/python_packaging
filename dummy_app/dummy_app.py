# dummy_app.py
# Jacob Hummel
# Created 2018-05-31
"""
Dummy App for demostrating Jenkins Pipeling for Python Continuous Integration.
"""
import os
def main():
    """Dummy function."""
    print("Hello World!")
    print("Working directory:", os.getcwd())
    return 42

if __name__ == '__main__':
    main()
