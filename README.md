# centime
centime api testing framework for Aplhavantage application

api_base.py : All the basic building api methods, invoke api and get response methods are maintained here.
alpha_views.py : All utilitiy methods that supports the framework like the methods to build different APIs with different params, methods to validate schemas, methods to validate errors, response ..etc maintained here.
alpha_vantage_constants.py = All the supporting constants related to project are maintained here.
test_Daily.py : All different test cases maintained here
conftest.py : ALl the supporting fixtures maintained here.
config.properties : All the environment level test data maintained here.

Step to run the test cases:

please run requirements.txt to install all required libraries using the below command :

pip install -r ./requirements.txt

please run the following command to run the testcases and to generate a report .html file:

pytest .\test\test_Daily.py --env=test --html=reports.html



