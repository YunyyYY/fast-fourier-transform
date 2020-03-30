import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SimpleFFT",
    version="0.0.2",
    author="Yunyy",
    author_email="lyguokelly@gmail.com",
    description="A small example package implementing FFT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YunyyYY/fast-fourier-transform",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    classifiers=[  # at least the following 3 should be included
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

# setuptools.find_packages()
# Packages are only recognized if they include an __init__.py file
