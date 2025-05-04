# Import necessary functions from setuptools for package setup and discovery
from setuptools import find_packages, setup

# Define a function to parse the requirements.txt file
def parse_requirements():
    with open("requirements.txt", "r") as file:
        return [line.strip() for line in file if line.strip() and not line.startswith("-e .")]

# Configure the package metadata and dependencies using setup()
setup(
    
    name="mlproject1",
    version="0.0.1",
    author="harsh",
    author_email="harshinghdps3@gmail.com",
    packages=find_packages(),
    install_requires=parse_requirements()
)