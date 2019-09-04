#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools
import subprocess

# Get current version from git
__version__ = subprocess.check_output(['git', 'describe', '--abbrev=0']).strip()
__version__ = str(__version__)[2:-1]

with open("README.rst") as f:
    long_description = f.read()

setuptools.setup(
        name='studious_happiness', 
        version=__version__,
        author='Ryan Patterson',
        author_email='ryan.patterson.2015@gmail.com',
        description='Keep calm and manage your tasks!',
        long_description=long_description,
        long_description_content_type='text/x-rst',
        url='https://github.com/rbpatt2019/studious_happiness',
        package_dir={'': 'src'},
        packages=setuptools.find_packages('src'),
        entry_points={
            'console_scripts':[
                'example = example:hello']},
        classifiers=[
            'Development Status :: 1 - Planning',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Natural Language :: English',
            'Programming Language :: Python :: 3.7'
            ],
        install_requires=['click'],
        python_requires='>=3.7'
        )
