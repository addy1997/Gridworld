#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Gridworld"
    version="0.0.1",
    author="Adwait Naik",
    author_email="adwaitnaik2@gmail.com",
    description="Grid world for openai gym",
    long_description=long_description="This package is based on openai-gym for creating the gridworld environment.",
    long_description_content_type="text/markdown",
    url="https://github.com/addy1997/Gridworld",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
 
