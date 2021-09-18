# mars-rover-assessment
Interview Code Assessment

### Step for run app:

### Check Python==3.7 installed
1. sudo apt-get install python3-pip python3-dev
2. sudo apt-get install python3.7
3. sudo apt install python3-pip

### Create virtual environment
1. mkdir my_app
2. cd my_app
3. python3.7 -m virtualenv app
4. clone repo
5. cd mars-rover-assessment
6. pip install -r requirement.txt
7. python setup.py bdist_wheel
8. pip install dist/app-0.0.1-py3-none-any.whl
9. app --filename input.txt

### Run Unittest

1. cd mars-rover-assessment
2. python3 -m unittest discover tests/
