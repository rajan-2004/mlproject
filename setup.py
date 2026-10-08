from setuptools import setup, find_packages





setup(   
    name="my_package",
    version="0.1.0",
    author="Rajan",
    author_email="drajansingh3@gmail.com",
    packages=find_packages(),
    install_requires=['numpy', 'pandas','scikit-learn','matplotlib','seaborn']
        
)