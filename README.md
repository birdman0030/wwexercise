# wwexercise

Weight Watchers International coding exercise

## Prerequisites

The following prerequisites will be needed to run the project:

#### **Install Python3**
	
Windows
	
[Windows 64-bit](https://www.python.org/ftp/python/3.8.2/python-3.8.2-amd64.exe) Installer

[Windows 32-bit](https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe) Installer

Linux
```
$ sudo apt install python3
$ sudo apt install python3-pip
```

#### **Install Chrome Browser**

[Chrome Browser Installers](https://www.google.com/chrome/) - This project supports the latest Chrome Browser Version - Build 81.X

## Get The Project

The following steps are needed to clone the project and install the dependencies:

**Clone the Project in Github:**

```
$ git clone https://github.com/birdman0030/wwexercise.git
```

**Project and install the dependencies**

**Windows**

```
$ cd wwexercise
$ pip3 install -e .
$ pip3 show wwexercise
```

**Linux**

```
$ cd wwexercise
$ sudo pip3 install -e .
$ sudo pip3 show wwexercise
```

## Running the tests

All tests are found in the "tests" directory of the project. To execute tests:

```
$ python wwexercise\test\question1.py
$ python wwexercise\test\question1.py
$ python wwexercise\test\question3.py
```
### Test Description

**Question 1**

There is a file containing a word and its possible meanings (like a Dictionary). The contents of the file look like this:

Apple – a fruit, a tech firm
Table – an object, contains rows and columns when used in context of computers
Orange – a fruit

Given a path to the file, do the following:

a)    Create a method called doesFileExist(String path) which takes the path of the file and tells the user if the file exists at that path or not. Assume all paths are relative to your project structure. If the file does not exist, catch the requisite exception.
b)    Read each word and its possible meanings and print them out. Your output should look like this:

```
Word1
Meaning 1
Meaning 2
Word2
Meaning1
Meaning2
```

**Question 2**

The following exercise does not require user login. Please use ID or class as selectors.

Steps:
1. Navigate to https://www.weightwatchers.com/us/
2. Verify loaded page title matches “WW (Weight Watchers): Weight Loss & Wellness Help”
3. On the right corner of the page, click on “Find a Studio”
4. Verify loaded page title contains “Find WW Studios & Meetings Near You | WW USA”
5. In the search field, search for meetings for zip code: 10011
6. Print the title of the first result and the distance (located on the right of location title/name)
7. Click on the first search result and then, verify displayed location name/title matches with the name of the first searched result that was clicked.
8. From this location page, print TODAY’s hours of operation (located towards the bottom of the page)
9. Create a method to print the number of meeting the each person(under the scheduled time) has a particular day of the week
e.g. printMeetings("Sun")

Write an automated test for this scenario using WebDriver.
```
Output should be:
Person A  3
Person B  1
```

**Question 3**

Generate 500 random numbers and create a method to print the nth smallest number

### Notes

question2.py - will fail as expected when checking page titles to expected results.

question2.py - Hours of operation are not available for workshops (likely due to covid updates)

If the latest version of Chrome Browser is not used, replace the chromedriver.exe in the "drivers" directory with the relavent version.

### References

[Python Installation Guide](https://realpython.com/installing-python/)
