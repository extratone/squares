from setuptools import setup, find_packages
import os
import platform

def get_data_files():
    # Install man page to the appropriate man directory depending on the OS
    if platform.system() == "Linux":
        return [("share/man/man1", ["squares/squares.1"])]
    elif platform.system() == "Darwin":
        return [("share/man/man1", ["squares/squares.1"])]
    else:
        return []

setup(
    name="squares-cli",
    version="0.1",
    description="Find the closest square numbers to a given input number from the command line.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="David Blue",
    author_email="davidblue@extratone.com",
    url="https://github.com/extratone/squares",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "squares=squares.squares:main"
        ],
    },
    data_files=get_data_files(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
