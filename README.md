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
3. pip3.7 install virtualenv
4. python3.7 -m virtualenv app
5. source app/bin/activate
6. clone repo
7. cd mars-rover-assessment
8. pip install -r requirement.txt
9. python setup.py bdist_wheel
10. pip install dist/app-0.0.1-py3-none-any.whl
11. app --filename input.txt

### ---------- OR ----------------
1. mkdir my_app
2. cd my_app
3. clone repo
4. cd mars-rover-assessment
5. chmod 755 app.sh
6. ./app.sh input.txt

### Run Unittest

1. cd mars-rover-assessment
2. python3 -m unittest discover tests/
