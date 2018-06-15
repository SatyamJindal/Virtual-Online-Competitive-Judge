from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random as rd
import lxml                                                                                 #Importing Libraries
import bs4 as bs
import urllib.request
from urllib.request import Request, urlopen
import webbrowser as wb
from bs4 import BeautifulSoup
import sys
from lxml import html
import requests


def codeforces(raw_html):
    raw_html = raw_html.replace('<span class="tex-font-style-bf">', ' ')
    raw_html = raw_html.replace("\le","<=")
    raw_html = raw_html.replace("\lt","<")
    raw_html = raw_html.replace("&lt;", '<')
    raw_html = raw_html.replace("\ge",">=")
    raw_html = raw_html.replace("\gt",">")
    raw_html = raw_html.replace("\\times","x")
    raw_html = raw_html.replace("\dots","...")
    raw_html = raw_html.replace("\ldots","...")
    raw_html = raw_html.replace("$$$","")
    raw_html = raw_html.replace("~"," ")
    raw_html = raw_html.replace("\sqrt","sqrt")
    raw_html = raw_html.replace("\sum_","sum")                                              #Cleaning Codeforces Questions
    raw_html = raw_html.replace("<p>","\n")
    raw_html = raw_html.replace("<i>","")
    raw_html = raw_html.replace("</i>","")
    raw_html = raw_html.replace('<div class="sample-tests">', '\n')
    raw_html = raw_html.replace('<span class="tex-font-style-underline">','')
    raw_html = raw_html.replace("</p>","")
    raw_html = raw_html.replace("<div>","\n")
    raw_html = raw_html.replace("</div>","\n")
    raw_html = raw_html.replace("</span>","")
    raw_html = raw_html.replace('<span class="tex-span">',"")
    raw_html = raw_html.replace('<div class="input-specification">', '')
    raw_html = raw_html.replace('<div class="section-title">', '\n')
    raw_html = raw_html.replace('<div class="problem-statement">', '')
    raw_html = raw_html.replace('<div class="header">','')
    raw_html = raw_html.replace('<div class="title">', '\n')
    raw_html = raw_html.replace('<div class="time-limit">','')
    raw_html = raw_html.replace('<div class="property-title">', '\n')
    raw_html = raw_html.replace('<div class="memory-limit">','')
    raw_html = raw_html.replace('<div class="property-title">', '\n')
    raw_html = raw_html.replace('<div class="input-file">','')
    raw_html = raw_html.replace('<div class="property-title">', '\n')
    raw_html = raw_html.replace('<div class="output-file">','')
    raw_html = raw_html.replace('<div class="property-title">', '\n')
    raw_html = raw_html.replace('<div class="output-specification">','')
    raw_html = raw_html.replace('<div class="section-title">', '\n')
    raw_html = raw_html.replace('<sup class="upper-index">', '^')
    raw_html = raw_html.replace('<span class="tex-font-style-tt">','')
    raw_html = raw_html.replace('</sup>','')
    raw_html = raw_html.replace('</sub>','')
    raw_html = raw_html.replace('<br/>','\n')
    raw_html = raw_html.replace('<pre>','')
    raw_html = raw_html.replace('<ol>','\n')
    raw_html = raw_html.replace('<ul>','\n')
    raw_html = raw_html.replace('</ol>','\n')
    raw_html = raw_html.replace('</ul>','\n')
    raw_html = raw_html.replace('<li>','\t')
    raw_html = raw_html.replace('</li>','\n')
    raw_html = raw_html.replace('</pre>' ,'')
    raw_html = raw_html.replace('<div class="sample-test">','')
    raw_html = raw_html.replace('<div class="input">','\n')
    raw_html = raw_html.replace('<div class="title">', '\n')
    raw_html = raw_html.replace('<div class="note">','')
    raw_html = raw_html.replace('<div class="output">', '\n')
    raw_html = raw_html.replace('<div class="section-title">', '')
    raw_html = raw_html.replace('<sub class="lower-index">' ,'')
    raw_html = raw_html.replace('\cdot' ,'.')
    
    if '\n\n' in raw_html or '\n \n ':
        raw_html = raw_html.replace('\n\n','\n')
        raw_html = raw_html.replace('\n \n ','\n')
    return raw_html


def codechef(raw_html):
    raw_html = raw_html.replace("\\t",'')
    raw_html = raw_html.replace("\\n",'\n')
    raw_html = raw_html.replace("\'",'\'')                                              #Cleaning Codechef Questions
    raw_html = raw_html.replace("      ",'')    
    raw_html = raw_html.replace("       ",'')
    return raw_html


url = 'https://www.codechef.com/problems/'
LARGE_FONT = ("Verdana", 12)
forces=['A','B','C','D','E']
beggi=[]
easy=[]
medi=[]
hard=[]
final_ques=[]
links=[]
file1 = open('beggi.txt','r')
file2 = open('easy.txt','r')
file3 = open('medi.txt','r')
file4 = open('hard.txt','r')                                                           
for i in file1:
    beggi.append(i)
for i in file2:
    easy.append(i)
for i in file3:
    medi.append(i)
for i in file4:
    hard.append(i)
def str_codechef(i):
    s=''
    global url,beggi,final_ques
    url = 'https://www.codechef.com/problems/'
    url1 = 'https://www.codechef.com/submit/'
    if(i==0):
        code = beggi[rd.randrange(len(beggi))]
        url+=code
        url1+=code
        links.append(url1)
    elif(i==1 or i==2):                                                         #Scraping Random Codechef Question based on difficulty   
        code = easy[rd.randrange(len(beggi))]
        url+=code
        url1+=code
        links.append(url1)
    elif(i==3):
        code = medi[rd.randrange(len(beggi))]
        url+=code
        url1+=code
        links.append(url1)
    elif(i==4):
        code = hard[rd.randrange(len(beggi))]
        url+=code
        url1+=code
        links.append(url1)
    page = requests.get(url[:-1])                                               #Getting source code
    #print(page.content)
    tree = html.fromstring(page.content)
    s = str(html.tostring(tree))
    soup = BeautifulSoup(s,'lxml')
    ques = soup.find_all("div",class_="primary-colum-width-left")               #Picking up the class containing the question
    #print(ques)
    soup1 = BeautifulSoup(str(ques),'lxml')
    final = str(soup1.get_text())
    final = str(codechef(str(final)))
    final = final[15:-90]                                                       
    final_ques.append(final)



def str_codeforces(i):
    global forces
    link = "http://codeforces.com/contest/" + str(rd.randrange(5,486))+'/problem/'
    if(i==0):
        link+='A'
        sauce = urllib.request.urlopen(link).read()
        soup = BeautifulSoup(sauce,'lxml')
        ques = soup.find_all("div",class_ = "problem-statement")                #Picking up the class containing the question
        ques[0] = codeforces(str(ques[0]))
        final_ques.append(ques[0])
        
    elif(i==1 or i==2):
        link+=forces[rd.randrange(1,3)]
        sauce = urllib.request.urlopen(link).read()
        soup = BeautifulSoup(sauce,'lxml')
        ques = soup.find_all("div",class_ = "problem-statement")
        ques[0] = codeforces(str(ques[0]))
        final_ques.append(ques[0])
    elif(i==3):                                                                 #Scraping Random Codeforces Question based on difficulty
        link+='D'
        sauce = urllib.request.urlopen(link).read()
        soup = BeautifulSoup(sauce,'lxml')
        ques = soup.find_all("div",class_ = "problem-statement")
        ques[0] = codeforces(str(ques[0]))
        final_ques.append(ques[0])
    elif(i==4):
        link+='E'
        sauce = urllib.request.urlopen(link).read()
        soup = BeautifulSoup(sauce,'lxml')
        ques = soup.find_all("div",class_ = "problem-statement")
        ques[0] = codeforces(str(ques[0]))
        final_ques.append(ques[0])
    links.append(link)
        
    
    
    

for i in range(5):
    which = rd.randrange(2)
    if(which==0):                                                                  #Random choice between codechef and codeforces
        str_codechef(i)
    else:
        str_codeforces(i)

class Virtual_Online_Judge(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self,'Virtual_Online_Judge')
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage,StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive):
            

            frame = F(container, self)

            self.frames[F]= frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def qf(param):
    print(param)

class MainPage(tk.Frame):

    def __init__(self, parent, controller):                                                     #Main Page
        global final_ques
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Main Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Start Contest",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        global final_ques
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="PROBLEM SET", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="See Problem 1",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

        button2 = ttk.Button(self, text="See Problem 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        button3 = ttk.Button(self, text="See Problem 3",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()
        button4 = ttk.Button(self, text="See Problem 4",
                            command=lambda: controller.show_frame(PageFour))
        button4.pack()
        button5 = ttk.Button(self, text="See Problem 5",
                            command=lambda: controller.show_frame(PageFive))
        button5.pack()


class PageOne(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="PROBLEM 1", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to PROBLEM SET",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="See Problem 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        button3 = ttk.Button(self, text="See Problem 3",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()
        button4 = ttk.Button(self, text="See Problem 4",
                            command=lambda: controller.show_frame(PageFour))
        button4.pack()
        button5 = ttk.Button(self, text="See Problem 5",
                            command=lambda: controller.show_frame(PageFive))
        button5.pack()
        button6 = ttk.Button(self, text="SHOW PROBLEM",
                            command=self.showTxt)
        button6.pack()
        button7 = ttk.Button(self, text="SUBMIT",
                            command=self.open_url)
        button7.pack()

    def showTxt(self):
        global final_ques,root
        root = Tk()
        T = Text(root, height=100, width=100)
        T.pack()
        T.insert(END,final_ques[0])

    def open_url(self):
        global links
        wb.open(links[0])
        
        

class PageTwo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="PROBLEM 2", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to PROBLEM SET",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="See Problem 1",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        button3 = ttk.Button(self, text="See Problem 3",
                            command=lambda: controller.show_frame(PageThree))
        button3.pack()
        button4 = ttk.Button(self, text="See Problem 4",
                            command=lambda: controller.show_frame(PageFour))
        button4.pack()
        button5 = ttk.Button(self, text="See Problem 5",
                            command=lambda: controller.show_frame(PageFive))
        button5.pack()
        button6 = ttk.Button(self, text="SHOW PROBLEM",
                            command=self.showTxt)
        button6.pack()
        button7 = ttk.Button(self, text="SUBMIT",
                            command=self.open_url)
        button7.pack()

    def showTxt(self):
        global final_ques,root
        root = Tk()
        T = Text(root, height=100, width=100)
        T.pack()
        T.insert(END,final_ques[1])

    def open_url(self):
        global links
        wb.open(links[1])

class PageThree(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="PROBLEM 3", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to PROBLEM SET",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="See Problem 1",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

        button3 = ttk.Button(self, text="See Problem 2",
                            command=lambda: controller.show_frame(PageTwo))
        button3.pack()
        button4 = ttk.Button(self, text="See Problem 4",
                            command=lambda: controller.show_frame(PageFour))
        button4.pack()
        button5 = ttk.Button(self, text="See Problem 5",
                            command=lambda: controller.show_frame(PageFive))
        button5.pack()
        button6 = ttk.Button(self, text="SHOW PROBLEM",
                            command=self.showTxt)
        button6.pack()

        button7 = ttk.Button(self, text="SUBMIT",
                            command=self.open_url)
        button7.pack()

    def showTxt(self):
        global final_ques,root
        root = Tk()
        T = Text(root, height=100, width=100)
        T.pack()
        T.insert(END,final_ques[2])

    def open_url(self):
        global links
        wb.open(links[2])

    

class PageFour(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="PROBLEM 4", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to PROBLEM SET",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="See Problem 1",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

        button3 = ttk.Button(self, text="See Problem 2",
                            command=lambda: controller.show_frame(PageTwo))
        button3.pack()
        button4 = ttk.Button(self, text="See Problem 3",
                            command=lambda: controller.show_frame(PageThree))
        button4.pack()
        button5 = ttk.Button(self, text="See Problem 5",
                            command=lambda: controller.show_frame(PageFive))
        button5.pack()

        button6 = ttk.Button(self, text="SHOW PROBLEM",
                            command=self.showTxt)
        button6.pack()

        button7 = ttk.Button(self, text="SUBMIT",
                            command=self.open_url)
        button7.pack()

    def showTxt(self):
        global final_ques,root
        root = Tk()
        T = Text(root, height=100, width=100)
        T.pack()
        T.insert(END,final_ques[3])

    def open_url(self):
        global links
        wb.open(links[3])

class PageFive(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="PROBLEM 5", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to PROBLEM SET",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="See Problem 1",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()

        button3 = ttk.Button(self, text="See Problem 2",
                            command=lambda: controller.show_frame(PageTwo))
        button3.pack()
        button4 = ttk.Button(self, text="See Problem 3",
                            command=lambda: controller.show_frame(PageThree))
        button4.pack()
        button5 = ttk.Button(self, text="See Problem 4",
                            command=lambda: controller.show_frame(PageFour))
        button5.pack()
        button6 = ttk.Button(self, text="SHOW PROBLEM",
                            command=self.showTxt)
        button6.pack()

        button7 = ttk.Button(self, text="SUBMIT",
                            command=self.open_url)
        button7.pack()

    def showTxt(self):
        global final_ques,root
        root = Tk()
        T = Text(root, height=100, width=100)
        T.pack()
        T.insert(END,final_ques[4])

    def open_url(self):
        global links
        wb.open(links[4])

    



app = Virtual_Online_Judge()
app.geometry("1000x600")
app.mainloop()
file1.close()
file2.close()
file3.close()
file4.close()



