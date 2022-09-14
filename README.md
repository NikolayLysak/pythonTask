# *SPACE Test Assignment:*
>## Condition 1:
> ### Log into the Space mobile app, set the passcode, log out and check the passcode.
>    - Language: Python
>    - Framework: Appium
>    - Platform: iOS / Android (one of them)
>    - Use a POM pattern for the test case automation
---

>## Condition 2:
> ~~~
> https://www.boredapi.com/api/activity
> ~~~
>  You’re given an open API, which generates different values with each iteration. E.g.: 
> ~~~
> { 
>   "activity": "Explore the nightlife of your city",
>   "type": "social",
>   "participants": 1,
>   "price": 0.1,
>   "link": "",
>   "key": "2237769",
>   "accessibility": 0.32
> }
> ~~~
> Please do the following:
> - Mock the endpoint in Postman, so that it returns 20 activities as a response 
> - Send a request to the mock that you’ve created and save only the responses that have Price > 0 
> - Sort the result by accessibility parameter, ascending.
---

## Description
#### PyTest was chosen as the working framework.
#### A complete list of installed packages can be found in 'requirements.txt'
~~~
 './requirements.txt'
~~~
> #### *The project is divided into two modules:*
> - API_task
> - FE_mobile_task
> ~~~
> |_API_task
> | |_src
> |   |_tests
> |     | sort_api_response_test.py
> |   |_utils
> |     | helper.py
> |     | request_data_from_service.py
> |
> |_FE_mobile_task
>   |_
>   |_
>   |_
> ~~~
> 
> #### *To install all the necessary dependencies, run the console command before starting the project:* 
> ~~~
> pip install -r requirements.txt
> ~~~
---
## Run tests:
### Go to the folder with the test class: 
~~~
cd API_task/src/tests
~~~
### To run the tests, please use the console command below:
~~~
pytest --alluredir=../../../allure_results
~~~
#### If you want to change the storage location of the Allure report data - change the value of the key *"--alluredir"* by specifying the path to the new location of the report folder
####
### To generate a report, run the console command.
###### _(If the path to the report folder has been changed - specify a new path to the report data storage folder)_
~~~
allure serve ../../../allure_results
~~~
