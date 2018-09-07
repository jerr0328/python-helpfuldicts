from setuptools import setup

setup(
    name='helpfuldicts',
    version='1.0',
    url='https://github.com/slezica/python-frozendict',

    author='Santiago Lezica, Jeremy Mayeres',
    author_email='slezica89@gmail.com,jeremy@mayeres.be',

    packages=['helpfuldicts'],
    license='MIT License',

    description='Helpful dictionaries, such as FrozenDict and NonelessDict',
    long_description=open('README.rst').read()
)
