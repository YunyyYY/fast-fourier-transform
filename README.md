# A simple implementation of Fast Fourier Transform

Just out of curiosity: how to build a python package. A simple FFT based on the article https://jakevdp.github.io/blog/2013/08/28/understanding-the-fft/.

The test script should be run as a module,
```python
python -m tests.test_fft
```
When using the `-m` command-line flag, Python will import a module or package, then run it as a script. When not using the `-m` flag, the file just run as a script.

When running
```python
python -m foo.bar.baz
```
foo.bar is imported and relative imports will work correctly with foo.bar as the starting point.

To run a package with `-m`, create a `__main__.py` module. When naming a package for running with `-m`, Python looks for that `__main__` module contained in that package and executes it as a script.

Reference:
1. https://packaging.python.org/tutorials/packaging-projects/.
2. https://www.programiz.com/python-programming/modules
3. https://stackoverflow.com/a/22250157/12705269
