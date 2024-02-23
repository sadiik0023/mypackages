from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_required=['numpy'],
    url='github.com',
    author='sadiik aguin',
    author_email='a.agguine@gmail.com'
)