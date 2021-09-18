#!/bin/sh

file=$1

pip3.7 install virtualenv > /dev/null 2>&1
python3.7 -m virtualenv appv > /dev/null 2>&1
source appv/bin/activate > /dev/null 2>&1
pip install -r requirement.txt > /dev/null 2>&1
python setup.py bdist_wheel  > /dev/null 2>&1
pip install dist/app-0.0.1-py3-none-any.whl > /dev/null 2>&1
app --filename "$file"
rm -rf appv
rm -rf dist