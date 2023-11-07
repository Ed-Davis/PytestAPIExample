# PytestAPIExample

## Just a simple API Testing Framework using PyTest

I have been refreshing some old skills and creating some examples for myself so I can be up and running more quickly. This example is the simplest possible API testing example, using PyTest

## Prerequisites:
In addition to a working Python3 environment, you will need to install PyTest - as described here and the Requests library details here. Alternatively you can just use the requirements.txt file with ``` pip install -r requirements.txt ```

# Next Steps

Authenticated API; keeping creds local in a bash script which exports the api key and account details as ENV variables (keep the file local by adding it to the .gitignore in the project directory). This can accept a file to run as an argument but if your framework is simple, you could hardcode 'pytest api_main.py' in so it gets the variables at the time you run the tests.
To this you can also add ``` -report=HTML > file.html``` (be smart and make it a timestamp based name or you will write over the same file each time...unless that's what you want!) so you can collect reports if needed.

You can then call the environment variables in an authentication function, which can nested away in the requestslib.py file.