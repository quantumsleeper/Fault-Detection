from setuptools import find_packages, setup
from typing import List


def get_requirements(filepath: str) -> List[str]:
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

        return requirements

setup(
    name='sensor',
    version='0.0.1',
    author='debarchan',
    author_email='f2015511p@alumni.bits-pilani.ac.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)