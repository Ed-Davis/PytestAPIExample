# PytestAPIExample
## Just a simple API Testinbg Framework using PyTest

I have been refreshing some old skills and creating some examples for myself so I can be up and running more quickly.  This example is the simplest possible API testing example, using PyTest

###Prerequisites:
In addition to a working Python3 environment, you will need to install PyTest - as described [here](https://docs.pytest.org/en/7.1.x/getting-started.html) and the Requests library [details here](https://pypi.org/project/requests/)

##Next Steps
Authenticated API; keeping creds local in a bash script which exports the api key and account details as ENV variables (keep the file local by adding it to the .gitignore in the project directory). This can accept a file to run as an argument but if your framework is simple, you could hardcode 'pytest api_main.py' in so it gets the variables at the time you run the tests.

You can then call the environment variables in an authentication function, which can nested away in the requestslib.py file.

##Another option...
Dockerize the tests?


