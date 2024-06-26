<h1>How to make a Quiz Game with python</h1>


<h2>Description</h2>
With this lab, we gain a better understanding of the Python language through the use of lists, objects, looping, and functions to create a quiz game.
This program will provide the user with a series of questions and give you some answers for you to answer. The program will give you feedback on whether you provided the correct answer or not and then explain the correct answer. While the program is running it will keep track of your score. When the quiz is finished the program will print your results. <br/>
<br/>
In this example, we are making a sneakerhead quiz game but feel free to take the information shown and modify it to a topic that quizzes you on a subject of your liking.  <br />
<br/>
Let's walk through it!<br/>
<br/>
Heads up:
- Coding indentation follows the PEP8 style guide for Python throughout the project.<br/>
- \n: tells the program to print an empty line.
- f: Used in front of a string allowing variable to be used. 

<h2>Languages and Utilities Used</h2>

- <b>Python3</b>
- <b>Terminal on Kali Linux</b> 
- <b>Nano Text Editor</b> 7.2

<h2>Environments Used </h2>

- <b>Linux</b>

<h2>Writing the code:</h2>

<p>
First, create a list: <br/>
- This list contains objects with different properties.<br/>
  - Here we have the prompt which is the question.<br/>
  - The options which are the answers to choose from.<br/>
  - The answer which is the correct answer is define by the letter.<br/>
  - The explanation which will explain the correct answer if the user made the wrong choice.<br/>
<br/>
A quick tip: Write out the questions, answers, and explanations on a separate text document. This allowed us to paste in the information and focus more on the formatting of the objects in the list.<br/>
<br />
<br />

Loop object:  <br/>
By putting the object in the curly brackets this will allow us to display each question one by one.<br/>
<br />
<img src="images/1-qgame.png" height="80%" width="80%">
<br />
<br />
Define the function:  <br/>
<br />
Once the list of questions is in place, define a function. In the example below the function is run_quiz and will take the parameters of questions that will run at the end. <br/>
- Next, initialize a score variable at zero to keep track of the user score <br />
<br />
<img src="images/2-qgame.png" height="80%" width="80%">
<br />
- Create a for loop for these questions. This loops through all of the individual objects (prompt, option, answer, and explanation) where the question variable refers to each object in the array respectively.<br/>
  - Inside the loop, print the question in the terminal. Print out the question by accessing the prompt attribute of the questions objects.<br/>
    Coding indentation follows the PEP8 style guide for Python throughout the project.<br/>
    <br />
    <img src="images/3-qgame.png" height="80%" width="80%">
    <br />
  - Create another for loop inside our question loop. The variable is option and we are accessing the options attribute of the questions objects.  <br />
    This will print out the answer choices line by line.  <br />
    <img src="images/4-qgame.png" height="80%" width="80%">
    <br />
  - Let's check on our code to make sure nothing is broken. <br />
    Use the run_quiz(questions) command outside and below of defined run_quiz function.<br />
    <img src="images/5-qgame.png" height="80%" width="80%"><br />
    <br />
    It should look like this if everything is up and running. <br />
    <br />
    <img src="images/6-qgame.png" height="80%" width="80%">
    <br />
  - Now we have to ask the user for the answer. Back in the text editor inside our defined run_quiz(questions) function, define a variable called answer and set it equal to input. Inside the input is the prompt or the question printed to the user.<br />
    This allows for the program to run the initial loop and stop to wait for the user's input before moving on to the next question object. <br />
    Append this function with .upper to 
    <img src="images/7-qgame.png" height="80%" width="80%">
    <br />
  - Create an if and else statement comparing to what the user input was. <br />
    When setting the if statement variable equal to, as a comparison operator, the object definition "answer" the program prints out a string notifying that the user is correct. <br />
    When correct we also want to increment the score variable. The score += 1 takes the value of the score and increments 1 to it and sets the new variable with that plus one compared to the previous one. <br />
    <img src="images/8-qgame.png" height="80%" width="80%">
    <br />
  - The else statement is for any other input that does not match the object definition "answer" inside the questions objects.<br />
    In this example, the print function prints out a string that notifies the user that they made the wrong choice and also an explanation of the right answer in the next line. <br />
   <img src="images/9-qgame.png" height="80%" width="80%">
    <br />
  - These lines will run for every question inside the loop until there are no more object questions to go through.<br />
    <br />
    <br />
  
Print the quiz grade:  <br/>
  - Print the score of the ending results with the variables of score and length (number of questions) inside the curly brackets.<br />
    f: Used in front of a string allowing variables to be used. <br />
    <img src="images/10-qgame.png" height="80%" width="80%">
    <br />
    <br />
Run the quiz:  <br/>
  Use the run_quiz(questions) command outside and below of defined run_quiz function again, if it's not already there. Save the program and run it back in the terminal. It should look like this if everything is up and running. <br />
    <img src="images/11-qgame.png" height="80%" width="80%">
    <br />
    <br />
  There we have it! Our very own Quiz Game made of the Python code. Go through and take the quiz to make sure everything works.
<img src="images/12-qgame.png" height="80%" width="80%">

</p>


<h2>Lessons Learned</h2>

- <b>Create an array of objects with definitions.</b><br />
- <b>Use for loops and the print function to show objects on the terminal intended.</b><br />
- <b>Input function stops the program from continuing the for loop waiting for user input.</b><br />
- <b>If and Else Statements to compare user input to right and wrong answers returning feedback to the user after each question.</b><br />



<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
