# Coding Dojo Python (Flask)
### Using python in a micro-framework

#### In this section we covered how python can be used to create full-scale web applications with the help of the Flask.
#### Main concepts were:
* ##### Rendering Templates
* ##### Redirecting Routes
* ##### Form Data
* ##### GET & POST requests
* ##### Session

# Projects

* ##### UnderStanding Routing
  > Create a server file that generates 5 different http responses
  >- Practice building a server with Flask from Scratch  
  >- Get Comfortable with routes and passing information to the routes  

* ##### Playground
  >Level 1: When a user visits localhost:5000/play, have it render three beautiful looking blue boxes  
  >Level 2: When a user visits localhost:5000/play/(x), have it display the beautiful looking blue boxes x times  
  >level 3: When a user visits localhost:5000/play/(x)/(color), have it display beautiful looking boxes x times, but this time where the boxes appear in (color). 
  
  >- Get comfortable passing information from the route to the template  
  >- Understand how to display information passed from the route in the template file  
  >- Get comfortable with using for loops in the template file  
  >- Get comfortable with using if statements in the template file  

* #### Checkerboard
  >- Continue to learn how to pass information from the url to the route  
  >- Get comfortable passing information from the route to the template
  >- Understand how to use for loop properly in the template
  >- Recognize the value of creating a html/css first and then adding logic/code
  
* #### HTML Table
  >- Get comfortable passing information from the route to the template
  >- Get very comfortable iterating through a list of dictionaries to generate a html output.  

* #### Dojo Survey 
  > Build a flask application that accepts a form submission and presents the submitted data on a results page
  
  >- Practice creating a server with Flask from scratch
  >- Practice adding routes to a Flask app  
  >- Practice having the client send data to the server with a form
  >- Practice having the server render a template using data provided by the client
  >- Practice how to redirect a http request to another url
  
* #### Dojo Fruit Store
  > Build a small web app of a fruit store where a student can select fruit and input their name and student Id  
  Have a check out page give the time and date the order was placed as well as a summary of fruit ordered and   
  student information
  
  >- Get more comfortable with POST and passing information via a form  
  >- Understand how to reference static css or images
  >- Practice using Git (especially git clone)
  >- Learn the importance of making your key assignments/projects look better
  >- Understand how your workflow may be like if you first worked on the HTML/CSS and how it's better
  >- Understand why rendering HTML on a URL that received a POST is a bad idea  
  
* #### Counter
  > Build a flask application that counts the number of times the root route ('/') has been viewed  
  > Level 1: localhost:5000- print in the terminal what's stored in session as well as have it render a template  
  > Level 1: localhost:5000/destroy_session - clear session (e.g. session.clear()).  Once the session is cleared, redirect to the root  
  > Level 1: Add a +2 button underneath the counter that reloads the page and increments counter by 2. Add another route to handle this functionality 
  > Level 2: Add a reset button that resets the counter back to 1. Add another route to handle this functionality
  
  >- Practice using session to store data about a particular client's history with the app
  >- Be able to check whether a session exists  
  >- Be able to initialize a session  
  >- Be able to modify a session  
  
* #### Number Game
  > Create a site that when a user loads it creates a random number between 1-100 and stores the number in session. Allow the user to guess at the number and tell them when they are too high or too low. If they guess the correct number tell them and offer to play again.

  >- Practice using session to store data about a client's history with the web app  
  >- Practice clearing a session  
  >- Practice having the server use data submitted by a client with a form  

* #### Ninja Gold
  > Create a simple game to test your understanding of flask, and implement the functionality below.  
  > For this assignment, you're going to create a mini-game that helps a ninja make some money!  
  > When you start the game, your ninja should have 0 gold. The ninja can go to different places (farm, cave, house, casino)   
  > and earn different amounts of gold. In the case of a casino, your ninja can earn or LOSE up to 50 golds.   
  > Your job is to create a web app that allows this ninja to earn gold and to display past activities of this ninja.  

  >- Practice using session
  >- Practice having the server use data sent by the client in a form
  >- Practice using hidden inputs 

* #### Dojo Survey with validations
  > Take the Dojo Survey assignment that you completed previously and add validations! The Name and Comment fields should be validated so that they are not blank. Also, validate that the comment field is no longer than 120 characters

  >- Practice validating user input
  >- Practice using flash messages

* #### Registration Form
  > Create a simple registration page with the following fields  
  >- Email  
  >- First Name  
  >- Last Name  
  >- Password  
  >- Confirm Password  
  
  > Validations must include  
  >- All fields are required and must not be blank
  >- First and Last Name cannot contain any numbers
  >- Password should be more than 8 characters
  >- Email should be a valid email
  >- Password and Password Confirmation should match
  
  > When the form is submitted, make sure the user submits appropriate information. If the user did not submit appropriate information, return the error(s) above the form that asks the user to correct the information
  
  >- Practice validating user input
  >- Practice using flash messages

* #### C+R Friends 
  > Create an application that allows users to view all friends and add new ones
  
  >- Create a Flask application that displays data from a MySQL database
  >- Take user input and add it to the database
  >- Practice redirecting after going to a POST route 

* #### Leads and Clients 
  > create a simple report dashboard using jQuery charts and graphs
  
  >- At a deeper level, understand how the server generates a http response which the browser can use to render the html/css or to give to the Javascript interpreter.
  >- Have you get exposure to generating beautiful graphs/plots using jQuery and know how to insert information from the database to Javascript.

* #### Email Validation with DB
  > Create an application that asks a user to enter an email address and validates whether that email is valid and whether it exists in the database  
  > Once a valid email address is entered, save to the database the email address the user entered. On the success page, display all the email addresses entered along with the date and the time when the email addresses were entered  
  
  >- Practice fetching data from a database connected to a Flask application
  >- Validate user input before adding it to the database
  >- Practice using flash messages
  >- Practice redirecting after going to a POST route
  
* #### Login and Registration
  > Build a Flask application that allows login and registration  
  > The user inputs their information, we verify that the information is correct, insert it into the database and return back with a success message. If the information is not valid, redirect to the registration page  
  >- First Name - letters only, at least 2 characters and that it was submitted
  >- Last Name - letters only, at least 2 characters and that it was submitted
  >- Email - valid Email format, does not already exist in the database, and that it was submitted
  >- Password - at least 8 characters, and that it was submitted
  >- Password Confirmation - matches password  
  
  > When the user initially registers we would log them in automatically, but the process of "logging in" is simply just verifying that the email and password the user is providing matches up with one of the records that we have in our database table for users  
  > Once we have already identified the places on our site that we wish to be dynamic for users that are logged in, then we just need to check to see if that session variable has been set and display the content accordingly

  >- Build an application that requires login and registration
  >- Practice connecting a Flask application to a MySQL database
  >- Become familiar with the logic that is required to validate a user's registration to a website
  >- Become familiar with the logic that is required to validate a user logging in to a website
  >- Practice using session

* #### Simple Wall
  > Build a Message wall Using Flask. User should be able to register and log in. Once a user logs in, allow the logged in user to send a message to other users as well as read all the messages sent to the logged in user. 
  > Users should be able to delete a message that has only been sent to that individual user.
  
  >- Practice connecting a Flask application to a MySQL database
  >- Include login and registration
  >- Include one-to-many relationships
  >- Continue to think about web security and how others could potentially hack your site


