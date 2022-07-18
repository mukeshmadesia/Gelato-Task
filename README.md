# Gelato-Task

Task 1 - Application testing
  Part 1- "Test Cases.xlsx" - for test cases
  Part 3- Python code to generate mock data randomly.

Task 3 - API Testing

    Gelato-Task.postman_collection.json - Is the exported collection of POSTMAN 
    
    Created collection of all the APIs and Test Scripts using Javascript for Test result validation 
            1. Used Global Variables to store BaseURL.
            2. Stored access code in Global Variable.
                
       "API-Test-Cases.xlsx"    - Refer the excelsheet for TestCases
    
    
Task 4 - Selenium with Python This Project is to test the following functionlity of Book Store Application Registration, https://demoqa.com/register authentication(login) https://demoqa.com/login Search https://demoqa.com/books

**Approach Deatils:

Sprint 1 : -

1. First, I explore the application manually and understand the functionalites of website

2. Login page requires - username and password, 

3. Registration Page - reuires firstname, lastname username and password
    a. An Alert is pop-up, on Successfull registration.
    b. "Passwords must have at least one non alphanumeric character, one digit ('0'-'9'), one uppercase ('A'-'Z'), one lowercase ('a'-'z'), one special                     character and Password must be eight characters or longer."
    
3. Search page - can filter on basis of  a. Book Title, b.Author and C. Publisher
**Sprint 2: **

1. Created a data driven framework based on Page Object Model using Selenium and Python
/NEP 
    /demoqaConfig 
        /Config.json  - Contains url and other static data required
        
   /demoqaPages 
        /BasePage.py      - Contains common functionalties required by other pages (like findElement, click, Send_keys etc)
        /Registration.py  - Contains actions to Enter details of user and click on Register and Then check for Alert Pop up -
                          - **Not Able to handle captcha - in QA - Captcha should be disabled**
                          - if Alert pop up - Returns the Alert message
                          - if Alert pop up doesn't comes - retuens  errormessage
        /LoginPage.py     - Contains Actions on Login Page (i.e. Login with valid/invalid credentials)
                          - Enter Username and Password, then click on login button
                          - Returns - uservalue of nextpage
        /Search.py        - Enters the searchtext in textbox and then retrieves the BooksTitle, Authorname and Publisher
                          - Checks if the searchtext is present in either title , Authorname or Publisher
                          - Returns flag
 /demoqaTests
      /BaseTest.py        - Create to include common methods required in TestScript
      /conftest.py        - fixture of Pytest - to used by all testscripts
      
 /demoqaTestScript       - Contains Scripts of Each page
      /Test_Login.py      - 1. test login page title
                          - 2. test login with valid credentials
                          - 3. test login with invalid credentails
      /Test_Register.py   - 1. Test Registration with new data
                          - 2. Test Registration with existing user
      /Test_Search.py     - 1. Test Search functionality with input data
 
 /demoqaTestData          
      /testData.csv       - conatins testdata in csv format
      
 /demoqaUtilis            - For common utlities to Read test data and can be enhanced to other functionalities
      
                              
      @data - used to make test datadriven - data read by csv file
