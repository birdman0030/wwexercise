# wwexercise
WWI coding exercise written in python3

## Install Python3
### Windows
[Windows 64-bit](https://www.python.org/ftp/python/3.8.2/python-3.8.2-amd64.exe)
[Windows 32-bit](https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe)

### Linux
```bash
$ sudo apt install python3
```

## Install pip
### Linux
```bash
$ sudo apt install python3-pip
```

## Install Chrome Browser
This project supports the latest version.
[Chrome Browser Installers](https://www.google.com/chrome/)

## Get the project
### Clone
```bash
$ git clone https://github.com/birdman0030/wwexercise.git
```

## Installing Project
#####1) Navigate to the Project parent directory. 

#####2) Install dependencies
(prefix with sudo on linux if not a root user)
```bash
$ pip3 install -e .
```

#####3) Verify
```bash
$ pip3 show wwexercise
```

## Run Tests
Navigate to the 'tests' directory in the project
```bash
$ python question1.py
$ python question2.py
$ python question3.py
```

## Notes:
1. question2.py - will fail as expected when checking page titles to expected results.
2. question2.py - Hours of operation are not available for workshops (likely due to covid updates)
3. If the latest version of Chrome Browser is not used, replace the chromedriver.exe with the relavent version.

## References
[Python Installation Guide](https://realpython.com/installing-python/)