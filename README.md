# Demo Python App

## Description
This application was created in order to demonstrate CI/CD capabilities for a Python application.

### What does it do?
The short answer - not a lot! When this application is started, it essentially just schedules a
task that fires at regular intervals (default is 5 seconds). Every interval, the application sends
a HTTP POST request to an endpoint with the following information:

* The name of this application
* The version of this application
* The name of the host on which this application is running

That's all there is to it. The application is intentionally simple.

### How can I execute the tests?
From the root directory of this repository, execute the following command:
`pytest --junitxml=build/reports/tests/test_results.xml test`

### How can I run this application locally?
From the root directory of this repository, execute the following command:
`python main.py`

### Where is the Jenkins pipeline for this application?
The build job is [here](http://52.61.105.186:8080/job/demo-python-app-pipeline/).
The deploy job is [here](http://52.61.105.186:8080/job/demo-python-app-deploy/).