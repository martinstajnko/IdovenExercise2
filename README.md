# DebugBear Website Testing

This project contains a suite of automated tests for the DebugBear website. The tests are written in Python using the Selenium library and Pytest framework.

## Prerequisites
Before running the tests, ensure you have the following prerequisites:

- Python 3.10 or higher installed
- Poetry for managing dependencies
- Web browsers (Chrome and/or Firefox) installed for running tests local
- Docker installed for running tests remote


## Setup 
1. Clone repo to your local machine.
2. Open the project in your favorite code editor.
3. Perform ```poetry install```.
4. Perform ```poetry shell```.


## Running tests locally:
To run the tests, execute the following command in your project directory:
```poetry run pytest tests/test_demo.py```

or with a Makefile:
```make run_tests```

To generate an HTML test report, you can use the following command:
```poetry run pytest tests/test_demo.py -n2 -v -s --html=./test_reports/debugbear.html --self-contained-html --capture sys -rP -rF```

- ```-n2```: This option specifies that pytest should run tests in parallel using 2 processes. You can adjust the number according to your system's capabilities.

- ```-v```: Enables verbose output, providing detailed information about the tests being executed.

- ```-s```: Allows pytest to display standard output (print statements) from your tests in the terminal.

- ```--html=./test_reports/debugbear.html```: This option tells pytest to generate an HTML test report and save it as debugbear.html in the test_reports directory. You can customize the filename and directory as needed.

- ```--self-contained-html```: Ensures that the HTML report is self-contained, meaning it includes all necessary resources (e.g., stylesheets and JavaScript) within the report itself.

- ```--capture sys```: Captures standard output and standard error for each test and displays it in the test report.

- ```-rP -rF```: These options control the display of test summary information. -rP displays the passed tests first, and -rF shows the failed tests first. You can adjust these options based on your preference.


## Running tests remotely:

Example is written for use of Firefox.

1. In tests/conftes.py set browser value to 'firefox' and location value to 'remote'.

2. Create network
```docker network create <mynetwork>```

3. Build tests image: 
```sudo docker build -t ui_tests:<tag> .```, where replace with <tag> with empty or e.g. ui_network 

4. Pull the Selenium WebDriver for Firefox image and run it in a container: 
```sudo docker run --network ui_network -d --rm -p 4444:4444 -e VNC_NO_PASSWORD=1 --name firefox selenium/standalone-firefox:4.12.1-20230912```

5. Run your UI tests container linked to Selenium:
```sudo docker run --network=ui_network --rm  -it ui_tests:latest poetry run pytest ./tests/test_demo.py -v -s```



