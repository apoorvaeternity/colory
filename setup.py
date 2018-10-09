import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='colory',
    version='0.2',
    packages=find_packages(exclude=['wiki_crawl.py', 'xkcd_colors.py', 'xkcd_colors.txt']),
    include_package_data=True,
    license='BSD License',
    description='A python package to find nearest name of colors using their hex value.',
    url='https://github.com/apoorvaeternity/colory',
    author='Apoorva Pandey',
    author_email='apoorvapandey365@gmail.com',
    python_requires='>=3',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
