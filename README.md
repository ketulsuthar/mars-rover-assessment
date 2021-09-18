# mars-rover-assessment
Interview Code Assessment

### Step for run app:

### Check Python==3.7 installed
1. sudo apt-get install python3-pip python3-dev
2. sudo apt-get install python3.7
3. sudo apt install python3-pip

### Create virtual environment and run app
1. mkdir my_app
2. cd my_app
3. python3.7 -m virtualenv app
4. source app/bin/activate
5. clone repo
6. cd mars-rover-assessment
7. pip install -r requirement.txt
8. python setup.py bdist_wheel
9. pip install dist/app-0.0.1-py3-none-any.whl
10. app --filename input.txt

### Run Unittest

1. cd mars-rover-assessment
2. python3 -m unittest discover tests/
