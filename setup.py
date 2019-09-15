#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

with open("README.rst") as f:
    long_description = f.read()

setuptools.setup(
        name='ToDonePy', 
        version="0.1.0",
        author='Ryan Patterson',
        author_email='ryan.patterson.2015@gmail.com',
        description='Keep calm and manage your tasks!',
        long_description=long_description,
        long_description_content_type='text/x-rst',
        url='https://github.com/rbpatt2019/ToDonePy',
        package_dir = {"": "src"},
        packages = setuptools.find_packages('src'),
        entry_points={
            'console_scripts':[
                'hello = command_line.example:hello']
        },
        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
            'Natural Language :: English',
            'Operating System :: Unix',
            'Programming Language :: Python :: 3.7'
            ],
        install_requires=['click'],
        python_requires='>=3.7'
        )
