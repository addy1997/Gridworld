#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Grid"
    version="0.0.1",
    author="Adwait Naik",
    author_email="adwaitnaik2@gmail.com",
    description="Grid world for openai gym",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/addy1997/Grid",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
 
