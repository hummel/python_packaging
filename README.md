Python Packaging Primer
=======================
##### Leveling up from writing ugly scripts to building shareable python libraries.

I strongly recommend the following resources for more details on this process:
* [The Python Packaging User Guide](https://python-packaging-user-guide.readthedocs.io/overview/)
* [The Hitchhiker's Guide to Python](https://docs.python-guide.org/shipping/packaging/)
* [Mahmoud Hashemi's "Python Packaging Gradient" Talk](https://www.youtube.com/watch?v=iLVNWfPWAC8)
	- [link to slides](https://speakerdeck.com/pybay/2017-the-packaging-gradient)

## **_Level 0:_** [Ugly scripts](https://github.com/hummel/python_packaging/blob/master/my_pypackage/ugly_script.py)
We all start making scripts like this.  Basically, taking command entered in the python REPL, and saving them to a file.

## **_Level 1:_** [Modules](https://github.com/hummel/python_packaging/blob/master/my_pypackage/standard_lib.py)
Level up to writing _pretty_ scripts that can be imported as modules.

## **_Level 2:_** [Multi-File Modules](https://github.com/hummel/python_packaging/blob/master/my_pypackage/__init__.py)
Adding an `__init__.py` file allows for the creation of hierarchical modules.

## **_Level 3:_** [Local Installation](https://github.com/hummel/python_packaging/blob/master/setup.cfg)
We can then install these modules locally by introducing a [`setup.py`](https://github.com/hummel/python_packaging/blob/master/setup.cfg) file and running `pip install -e .`.

## **_Level 4:_** Building a Package
Use python's setuptools to turn your module into an acutal installable artifact: `python setup.py sdist`

## **_Level 5:_** Uploading to pypi.org
`twine upload --repository-url https://test.pypi.org/legacy/ dist/*`