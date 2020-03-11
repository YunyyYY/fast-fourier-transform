# <package>/__init__.py is required to import the directory as a package
# and can simply be an empty file.

from .main_fft import fft 
# in this way fft will appear in dir(src)
# can be directly found as fft without using src.fft_main

