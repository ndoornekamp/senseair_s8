import setuptools

__version__ = "0.0.11"

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="senseair_s8",
    version=__version__,
    author="Nick Doornekamp",
    author_email="nddoornekamp@gmail.com",
    description="Python module for reading CO2 concentration from a Senseair S8 sensor connected to a Raspberry Pi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ndoornekamp/senseair_s8",
    packages=setuptools.find_packages(),
    py_modules=["senseair_s8.senseair_s8"],
    install_requires=[
        'pyserial',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
