from setuptools import setup

setup(
    name="smiles2sdf",
    version="1.0",
    py_modules=["main"],
    install_requires=[
        "pandas",
        "rdkit",
        "openpyxl"
    ],
)
