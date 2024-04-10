<h1>How to make a Quiz Game with python</h1>


<h2>Description</h2>
With this lab we gain a better understanding of the Python language through use of lists, objects, looping, and functions to create a quiz game.
This program will provide the user with a series of questions and give you some answers for you to answer. The program will give you a feedback whether you provided the correct answer or not then give an explaination of the correct answer. While the program is running it will keep track of your score. when the quiz is finish the program will print your results. <br/>
<br/>
In this example we are making a sneakerhead quiz game but feel free to take the information shown and modify it to a topic that quizes you on a subject of your liking.  
<br />
Lets walk through it!


<h2>Languages and Utilities Used</h2>

- <b>Python3</b>
- <b>Terminal on Kali Linux</b> 
- <b>Nano Text Editior</b> 

<h2>Environments Used </h2>

- <b>Kali Linux</b> (2024.1-amd64)

<h2>Writing the code:</h2>

<p>
First we create a list: <br/>
- This list contains objects with different properties.</b> 
  - Here we have the prompt which is the question.</b> 
  - The option which are the answers to choose from.</b> 
  - The answer which is the correct answer define by the letter.</b> 
  - The explaination which will explain the correct answer if user made the wrong choice.</b> 
<img src="https://i.imgur.com/TuUqRo5.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Loop object:  <br/>
By putting the object with in the curly brackets this will allow us to display each question one by one<br/>
<img src="https://i.imgur.com/qNa1AR0.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Define the function:  <br/>
Once the list of questions are in place, we want to define a function. In the example below the function is run_quiz and will take the parameters of questions which will run at the end. <br/>
- We then want to initialize a score variable at zero to keep track of the user score</b> 
*
- Create a for loop for these questions. This loops though all of the individual objects (prompt, option, answer, and explanation) where the question variable refers to each object in the array respectively.
  - Inside the loop, we first need to print the question in the terminal.
    Here we print out the question by accessing the prompt attribute of the questions object.
  - We then need to print the choices.
    
<img src="https://i.imgur.com/qNa1AR0.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
</p>

<h2>Lessons Learned</h2>

-</b>

<h2>Brush Up</h2>

- <b></b>

<h2>Shortcuts Learned</h2>

- <b></b>


<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
