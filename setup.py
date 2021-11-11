from setuptools import setup, find_packages


setup(
    name='secretsanta',
    packages=find_packages(),
    email='jonathan.birkey@gmail.com',
    author='Jonathan Birkey',
    install_requires=[
        'click'
    ],
    version='0.0.1',
    entry_points="""
    [console_scripts]
    santa=secretsanta:secretsanta
    """
)
