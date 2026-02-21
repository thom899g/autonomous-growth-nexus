from setuptools import find_packages, setup

setup(
    name="AGNModule",
    version="0.1",
    packages=find_packages(),
    install_requires=["torch>=1.9.0", "pytorch-lightning>=1.5.0"],
)