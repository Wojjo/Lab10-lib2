from setuptools import setup, find_packages

setup(
    name='Lab10-lib2',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    description='Lab10-lib2',
    long_description=open('README.md').read(),
    url='https://github.com/Wojjo/Lab10-lib2.git',
    author='Przemysław Wojcinowicz',
    author_email='p.wojcinowicz@gmail.com'
)