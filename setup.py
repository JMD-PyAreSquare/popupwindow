import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="popupwindow",
    version="0.0.1",
    author="PyAreSquare",
    author_email="jmd.pyaresquare@gmail.com",
    description="display popups",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JMD-PyAreSquare/popupwindow",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
