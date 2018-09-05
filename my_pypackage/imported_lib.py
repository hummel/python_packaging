# imported_lib.py
# Jacob Hummel
# Created 2018-09-05
"""
Dummy package for demonstrating how to package up python code for distribution.
"""
import requests

def ping_github():
    """Check github."""
    response = requests.get('https://github.com/hummel')
    if response.status_code == 200:
    	print("\nGithub available!\n")
    else:
    	raise ConnectionError("\nGithub is down. Panic!\n")
    return response.status_code

if __name__ == '__main__':
    ping_github()
