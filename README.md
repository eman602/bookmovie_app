# bookmovie_app

## Brief
The aim of this project as specified in the brief is to create a CRUD application with utilisation of supporting tools. It must have methodologies and technologies that encapsulates all core modules covered during the training. It is then to be assessed by the trainers who will assess the capabilities and concepts that were taught and assess the project against S.F.I.A. 
 In order to meet the requirements of the project I must display the following:
 * A Trello board displaying tasks in category of Completed, In progress, and etc. 

 * A relational database to store data persistently for the project. The database must contain at least 2 tables excluding a table displaying Users. 

 * A detailed risk assessment and a clear documentation from a design phase describing the architecture.  

 * A functional CRUD application created in Python which meets the requirements set in the Trello board. 

 * A high-test coverage in the backend providing a consistent report and evidence to support a TDD approach. 

 * A fully designed test suites for the project as well as a well automated tests for validation of the application.   

 * A functioning front-end website with integrated API’s using Flask. 

 * Code being fully integrated into a version control system using the feature-branch model which will subsequently be built through a CI server and deployed to a cloud-based virtual machine. 
 
 ## Methods
 My attempt at achieving the requirements is through a movie and book app project that will allow the user to first: - 
 * Add books to sell 
   (Title, genre, year of release, Author, price).
 * Add movies to sell 
    (Title, genre, year of release, Director, price).
 * Search  and read about books to buy 

 * Search and read about movies to buy 

 * Update information about a movie or book 

 * Delete movie or book 

## Tracking my Project
![trello picture](https://user-images.githubusercontent.com/64255340/82814253-b0faea00-9e8e-11ea-9559-fe6f8b70f04e.png)

This Trello is designed to be read and interpreted from left to right with different categorising relating to different parts of the projects as explained below. 

#### Things to do (Beck-end) 
 

This reflects the tasks relating to the logical parts of the app and the code required to complete it. Namely, I would need to construct code allowing users to add a movie or a book as well as code to allow users to update or delete items as they see fit. 

#### Things to do (Front-end) 

This refers to the websites and perhaps the design of it which will need to be completed in Flask. 

#### Things to do (UCD & Database & Planning) 

This category refers to tasks which are non-coding related are ideally based on analysis on risks, documentation of the process, creation of user stories and etc.  

#### Things to do(Testing) 

This category refers to testing of both the front-end and back-end of the project. The beck-end specifically will be tested using pytest. Altogether, there will need to be a high-test coverage and evidence of this shown. 

#### Doing 
This signifies the tasks which I am currently doing. 
#### Done 
This refers to tasks which are completed. 

#### Risk Assessment 
The link for the risk assessment can be found - https://onedrive.live.com/edit.aspx?resid=67C6B66CC3D9FFE8!105&cid=1371f661-24ed-4557-b5e7-a18b1901bf6b&ithint=file%2cxlsx&wdOrigin=OFFICECOM-WEB.MAIN.MRU 

It is also shown below: -
![riskassessment1](https://user-images.githubusercontent.com/64255340/82815927-1c928680-9e92-11ea-8e1f-a8543b0e1a17.png)

![riskassessment2](https://user-images.githubusercontent.com/64255340/82815949-25835800-9e92-11ea-9f84-97ec6a79898e.png)

#### Testing
![coveragereport](https://user-images.githubusercontent.com/64255340/82816159-8b6fdf80-9e92-11ea-9dca-739e752fadd9.png)

Pytest is a powerful tool used to test the functionality of code. There is a saying “an untested code is a broken code”. Although this may not necessarily be true, it does cause the belief that without tested code, there is no guarantee that the application created will continue to work when it is transferred from development environment to the production environment. Hence it is important that a high-test coverage is achieved. 

Reason for this is that, it will first expose any errors in the code immediately and will also provide confidence that would allow developers to continue adding features without having to waste time and revisit previous written code that was perceived to be working. 

In my own code, I achieved 99% coverage although my initial aim was to achieve 100% aim however, I was unable to trigger the code which would cause an automatic error to display upon the user pressing the delete button on the app without entering information. 

For my own app, I wrote 23 different tests. 

 
 
 
 
 
 
 
 
