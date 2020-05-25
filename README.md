# bookmovie_app
## LINKS
Risk Assessment : https://onedrive.live.com/edit.aspx?resid=67C6B66CC3D9FFE8!105&cid=11e27e3c-647a-48fc-92a2-dde06427a580&ithint=file%2cxlsx&wdOrigin=OFFICECOM-WEB.MAIN.MRU

Trello : https://trello.com/b/jzxsxgkl/movie-and-book-app

## Content
* [Brief](#brief)
* [Methods](#methods)
* [Architecture](#architecture)
* [CI Pipeline](#ci-pipeline)
* [Tracking my Project](#tracking-my-project)
* [Risk Assessment ](#risk-assessment)
* [Testing](#testing)
* [Web application display of the app](#web-application-display-of-the-app)
* [Issues with Application](#issues-with-application)
* [Improvements](#improvements)
* [Author](#author)




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

## Architecture
#### Database Structure

##### Before
![erd2](https://user-images.githubusercontent.com/64255340/82837018-d3592b80-9ebf-11ea-9271-0b79c1780bd6.png)

I had initially planned to use the image above as my ERD however, I wanted to insure I had implemented what would allow me to achieve my MVP, and after which I could then build upon it. 

##### Current
![erd1](https://user-images.githubusercontent.com/64255340/82837033-e1a74780-9ebf-11ea-8881-831d231daeee.png)

This image is currently what the structure of the database is built on as as shown, we have the foreign key of in the Movies table implemented from the primary key of the Books table, hence allowing for a relationship to occur between the tables.

#### User Case
![usercase](https://user-images.githubusercontent.com/64255340/82837084-000d4300-9ec0-11ea-8376-a00455007ada.png)

This is an outline description of what is possible for the user to be able to do and also how the computer will respond to their request. Within the app, the users request will be recognised by the server through either the POST Method or the GET method.

## CI Pipeline
![CIpipeline](https://user-images.githubusercontent.com/64255340/82837352-aa856600-9ec0-11ea-9422-c6cfc59ed580.png)
The continous integration pipeline begins at the  python level in which the source code is constructed in VS code and tested using python3 app.py. After the code successfully worked in the development server, the code is then pushed up to github under the repository name bookmovie_app. Currently there are 3 branches being used and the most updated one being the testing branch. This branch has a connection through webHook with hence any changes made here will be picked up by the CI tool Jenkins and automatically configured and built. 

In my CI pipeline, I planned to have Jenkins run my automatic test as shown however, in reality, all code was tested using unit testing in pytest before the code was pushed up to git hub and integrated into the app. Jenkins will install the flask and import all the necessary modules. 

Code is checked by Jenkins and if it is sufficient, it will then be built without an error message being sent. 
At the very beginning of the process, all the required work are put on Trello and the required work is recieved from Trello and once is it completed, it is then updated in Trello and another piece of work is taken.

## Tracking my Project
the link for my Trello can be found at : https://trello.com/b/jzxsxgkl/movie-and-book-app

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

## Risk Assessment 
The link for the risk assessment can be found - https://onedrive.live.com/edit.aspx?resid=67C6B66CC3D9FFE8!105&cid=1371f661-24ed-4557-b5e7-a18b1901bf6b&ithint=file%2cxlsx&wdOrigin=OFFICECOM-WEB.MAIN.MRU 

It is also shown below: -
![riskassessment1](https://user-images.githubusercontent.com/64255340/82815927-1c928680-9e92-11ea-8e1f-a8543b0e1a17.png)

![riskassessment2](https://user-images.githubusercontent.com/64255340/82815949-25835800-9e92-11ea-9f84-97ec6a79898e.png)

## Testing
![coveragereport](https://user-images.githubusercontent.com/64255340/82816159-8b6fdf80-9e92-11ea-9dca-739e752fadd9.png)

Pytest is a powerful tool used to test the functionality of code. There is a saying “an untested code is a broken code”. Although this may not necessarily be true, it does cause the belief that without tested code, there is no guarantee that the application created will continue to work when it is transferred from development environment to the production environment. Hence it is important that a high-test coverage is achieved. 

Reason for this is that, it will first expose any errors in the code immediately and will also provide confidence that would allow developers to continue adding features without having to waste time and revisit previous written code that was perceived to be working. 

In my own code, I achieved 99% coverage although my initial aim was to achieve 100% aim however, I was unable to trigger the code which would cause an automatic error to display upon the user pressing the delete button on the app without entering information. 

For my own app, I wrote 23 different tests. 

## Web application display of the app 
![DeleteMovie](https://user-images.githubusercontent.com/64255340/82816985-0c7ba680-9e94-11ea-8d98-2fe7bfa7ef66.png)

This is the Delete Page of the side allowing an individual to enter a Book name into the form and if the book placed is within the database, they are given the ability to delete the book from the list. Upon pressing that button, they would be directed to the Book page where they would be able to see that indeed the Book has been removed from the database.  

![Bookpage](https://user-images.githubusercontent.com/64255340/82817031-25845780-9e94-11ea-8761-fa01e9adaff1.png)

This page host all the books that have been added to the database. In this, only the book ID, Book name, authors  name and the Genre will be displayed here. 

![moviepage](https://user-images.githubusercontent.com/64255340/82817063-3634cd80-9e94-11ea-9e06-c51c68520e74.png)
This is the same format for the movie page also where all the movies added will be displayed upon this page.  

![addbook](https://user-images.githubusercontent.com/64255340/82817109-49e03400-9e94-11ea-8e24-6a8d2b79850f.png)
In this page, an individual is able to add books and can only do so by filling in all the given forms which upon completion, they would then be redirected to the Book Page, where they can see their input data has successfully been added to the database.  

![addmovie](https://user-images.githubusercontent.com/64255340/82817140-5b294080-9e94-11ea-9a3f-87f5ff11a67c.png)

This page allows the user to enter a movie and its details which will be saved unto the database. If the movie is made based upon a movie, they can go to the book section and add it according to the books ID and upon submission, there would be a relationship created between the book and the movie. Deletion of this book or movie would cause the complete removal of the added information.

![deletemovie2](https://user-images.githubusercontent.com/64255340/82817203-785e0f00-9e94-11ea-9417-5899e625406a.png)
This page is similar to the delete Book page however it differs in that It will allow the user to delete the movie. 

![update](https://user-images.githubusercontent.com/64255340/82817251-90359300-9e94-11ea-9644-4254313e29eb.png)
This page allows the user to update items in the database. Hence when they enter the Book name, the system will search the database for the book name entered. If the Book can be found within the database, then all the other entered items in the remaining forms will be updated for the book name in question. 


## Issues with Application 

* An issue with the app at the moment is that, you can add the same movie or Books more than once. 

* Another issue is that when you go to update a book, if the book name is not known in the database, the application simply reloads but does not necessarily provide a reason why the page has not redirected to the book page. 

 

## Improvements 

* The Design of the site is the first thing I want to improve. Given that this is an app for Books and Movies, there should be pictures of books and movies to encourage the user to use the site. 

* Furthermore, upon someone adding a movie or book, they should also have the option of attaching a picture alongside or in fact, an algorithm which fetches the picture based upon the name of the book or movie. 

* Another improvement is allowing users to have a personalised account on the app. 

* Another improvement is the incorporate either a selling or a renting function whereby users can sell movies or books to other users within the page.  

* Another improvement is allowing a voting system on the books or movies that individuals will add to the page. 

## Author
Emmanuel Agyapong



 
 
 
 
 
 
 
