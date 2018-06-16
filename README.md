# Virtual-Online-Competitive-Judge :sunglasses:


**Virtual Online Judge** generates a random set of questions from various Online Websites for competitive programming  such as Codechef, Codeforces etc.It creates a contest containing five problems sorted by difficulty and a user may submit solutions to these problems in any order. Questions from these websites are scraped and can be viewed by the user on a basic GUI crated on python using Tkinter.


Every competitive programmer wants a good mix of questions from different judges and to have a script which would create a completely random contest any number of times would be a delight for a competitive programmer. :computer:


## Set-Up Instructions :exclamation:


**Technologies needed –**
+ Python

**Python Modules needed –**
+ Tkinter
+ PIL
+ lxml
+ bs4
+ webbrowser
+ requests
+ urllib

**_Tip:_** - The simplest way to get the above modules is to use pip. :thumbsup:

**_Note:_**- Before you begin attempting the questions make sure you have logged in to your respective judges with your respective account details.

**Setup on your PC**
+ After you are done with downloading the above modules you have to download the contents of this repository.
+ Unzip it and run the python file named “Virtual_Online_Judge.py”

**A Tkinter GUI window will pop up which will something like this: -**

![alt text](https://github.com/SatyamJindal/Virtual-Online-Competitive-Judge/blob/master/GUI_Window.gif "Logo Title Text 1")



After you see the above window, you are all set to attempt all the questions. A basic display would be something like: - 

![alt text](https://github.com/SatyamJindal/Virtual-Online-Competitive-Judge/blob/master/Problem_demo.gif "Logo Title Text 1")


## How it works :question:

Codechef and Codeforces have a standard template of contest information of their own. The script initially randomly selects from either of the two judges and then randomly generates the URL of the question based on the difficulty of the problem. 

Once the URL is generated, the respective website is parsed and the entire question is scraped using the beautiful soup library using the lxml parser and printed as it in in the GUI after removing all the HTML tags and string formatting.

The URL for the Submit button also follows a similar standard template approach and is obtained in a similar way.

















