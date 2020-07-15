import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Isnull Find - nolannib", # Replace with your own username
    version="0.0.1",
    author="Nolanni Bartholomew",
    author_email="nolanni.bartholomew@lambdastudents.com",
    description="A package to find and show missing data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NolanniLB/lamdata-DSPT6",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
