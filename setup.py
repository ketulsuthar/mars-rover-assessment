import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="app",
    version="0.0.1",
    author="Ketulkumar Suthar",
    author_email="rk2lsuthar@gmail.com",
    description="Package to mars rover",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['app', 'mars_rover', ''],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points='''
        [console_scripts]
        app=app:cli
    '''
)