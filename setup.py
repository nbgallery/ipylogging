# vim: expandtab tabstop=4 shiftwidth=4

from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), 'r') as f:
    long_description = f.read()

setup(
    name='ipylogging',
    version='2020.341.0',
    author='Bill Allen',
    author_email='photo.allen@gmail.com',
    description='Easy log messages in Jupyter notebooks.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='logging logger logs ipython jupyter notebook messages'.split(),
    url='https://github.com/nbgallery/ipylogging',
    packages=['ipylogging'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License'
    ]
)
