import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="FMHash",
    version="1.0",
    author="Erik Shagdar",
    author_email="erik.shagdar@gmail.com",
    description="Converts between python FileMaker SRF dictionaries.",
    long_description="Converts between python dictionaries and Filemaker's SixFriedRice-style dictionaries.",
    long_description_content_type="text/markdown",
    url="https://github.com/ericgarig/FMHash",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
