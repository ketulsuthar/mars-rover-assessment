# mars-rover-assessment
Interview Code Assessment

### Step for run app:

### Check Python==3.7 installed
- sudo apt-get install python3-pip python3-dev
- sudo apt-get install python3.7
- sudo apt install python3-pip

### Create virtual environment
- mkdir my_app
- cd my_app
- python3.7 -m virtualenv app
- clone repo
- cd mars-rover-assessment
- pip install -r requirement.txt
- python setup.py bdist_wheel
- pip install dist/app-0.0.1-py3-none-any.whl
- app --filename input.txt

### Run Unittest

1. cd mars-rover-assessment
2. python3 -m unittest discover tests/
