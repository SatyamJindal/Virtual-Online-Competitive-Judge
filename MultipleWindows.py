from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random as rd
import lxml
import bs4 as bs
import urllib.request
url = 'https://www.codechef.com/problems/'
LARGE_FONT = ("Verdana", 12)
#beggi=['CNDLOVE', 'SINS', 'SPAMCLAS', 'ORDTEAMS', 'ZUBTRCNT', 'FRK', 'ZUBREACH', 'CHEFCHR', 'BIGSALE', 'CHEGLOVE', 'COUPSYS', 'L56GAME', 'CODERLIF', 'SURVIVE', 'HILLS', 'CO92JUDG', 'SMRSTR', 'KFIB', 'RGAME', 'VILTRIBE', 'CHRL4', 'GIT01', 'STRLBP', 'GOODBAD', 'CCOOK', 'RNDPAIR', 'NW1', 'FBMT', 'RECTANGL', 'ALEXTASK', 'TWEED', 'KOL16B', 'SEBIHWY', 'LISDIGIT', 'LIKECS01', 'C00K0FF', 'LTM40AB', 'SNELECT', 'ENTEXAM', 'KOL16J', 'PERFCONT', 'CHEFAPAR', 'MATPAN', 'CK87MEDI', 'CHNGOR', 'CHEFROUT', 'SNAKPROC', 'XENTASK', 'TEMPLELA', 'SEGM01', 'ADACRA', 'CHEFDETE', 'NOTINCOM', 'LADDU', 'COOMILK', 'BUGCAL', 'CHEFSUM', 'NITIKA', 'BRLADDER', 'ACBALL', 'LOSTMAX', 'LCOLLIS', 'GOODSET', 'EGRANDR', 'ELEVSTRS', 'DEVARRAY', 'RAINBOWA', 'ICPC16B', 'SIMDISH', 'OMWG', 'ANKTRAIN', 'UTMOPR', 'CHCHCL', 'CHEFSTUD', 'STICKS', 'CATSDOGS', 'WDTBAM', 'TTENIS', 'TWONMS', 'DWNLD', 'TALAZY', 'TICKETS5', 'SIMPSTAT', 'ALTARAY', 'CANDY123', 'FLOW015', 'ALPHABET', 'CHRL2', 'SUBINC', 'BRACKETS', 'STRPALIN', 'CFRTEST', 'LONGSEQ', 'COLOR', 'DEVUGRAP', 'ICPC16A', 'MOVIEWKN', 'FRGTNLNG', 'CHEFARRP', 'KTTABLE', 'CHEFSQ', 'RRJOKE', 'VCS', 'CHN09', 'RECTSQ', 'TRICOIN', 'COPS', 'MISSP', 'MNMX', 'LCH15JAB', 'TWOSTR', 'FRUITS', 'PPSUM', 'CHEFSTLT', 'FLOW014', 'FLOW011', 'GDOG', 'FLOW016', 'FLOW009', 'HEADBOB', 'AMR15A', 'TRISQ', 'CHOPRT', 'FLOW010', 'SMPAIR', 'PRB01', 'PALL01', 'COMM3', 'FLOW013', 'FLOW005', 'FLOW008', 'FLOW018', 'ONP', 'RECIPE', 'FLOW017', 'REMISS', 'FSQRT', 'PERMUT2', 'FLOW007', 'SUMTRIAN', 'FLOW004', 'LUCKFOUR', 'START01', 'CIELRCPT', 'FLOW002', 'FLOW006', 'MUFFINS3', 'TLG', 'FLOW001', 'TSORT']
beggi=[]
easy=[]
medi=[]
hard=[]
final_ques=[]
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
def str1(i):
    s=''
    global url,beggi,final_ques
    url = 'https://www.codechef.com/problems/'
    if(i==0):
        url+=beggi[rd.randrange(len(beggi))]
    elif(i==1 or i==2):
        url+=easy[rd.randrange(len(beggi))]
    elif(i==3):
        url+=medi[rd.randrange(len(beggi))]
    elif(i==4):
        url+=hard[rd.randrange(len(beggi))]
    sauce = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(sauce,'lxml')
    ind=0
    ind1=0
    count=0
    s = soup.get_text()
    for i in range(len(s)-20):
        if(s[i]=='S' and s[i+1]=='u' and s[i+2]=='b' and s[i+3]=='m' and s[i+4]=='i' and s[i+5]=='t'):
            count+=1
            if(count==1):
                ind1=i
                break
            #if(count==2):
                #ind=i
    for i in range(len(s)-1,7,-1):
        if(s[i]=='t' and s[i-1]=='i' and s[i-2]=='m' and s[i-3]=='b' and s[i-4]=='u' and s[i-5]=='S'):
            ind=i
            break
    s = s[ind1+30:ind-8]
    final_ques.append(s)
for i in range(5):
    str1(i)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive):
            

            frame = F(container, self)

            self.frames[F]= frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def qf(param):
    print(param)


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        global final_ques
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
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
        label = ttk.Label(self, text="Page 1", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
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
        button6 = ttk.Button(self, text="Show Problem",
                            command=self.showTxt)
        button6.pack()

    def showTxt(self):
        global final_ques,root
        root = Tk()
        T = Text(root, height=100, width=100)
        T.pack()
        T.insert(END,final_ques[0])
        

class PageTwo(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
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
        button6 = ttk.Button(self, text="Show Problem",
                            command=self.showTxt)
        button6.pack()

    def showTxt(self):
        global final_ques,root
        root = Tk()
        T = Text(root, height=100, width=100)
        T.pack()
        T.insert(END,final_ques[1])

class PageThree(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page three!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
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
        button5 = ttk.Button(self, text="VSee Problem 5",
                            command=lambda: controller.show_frame(PageFive))
        button5.pack()
        button6 = ttk.Button(self, text="Show Problem",
                            command=self.showTxt)
        button6.pack()

    def showTxt(self):
        global final_ques,root
        root = Tk()
        T = Text(root, height=100, width=100)
        T.pack()
        T.insert(END,final_ques[2])

class PageFour(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page four!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
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
        button5 = ttk.Button(self, text="VSee Problem 5",
                            command=lambda: controller.show_frame(PageFive))
        button5.pack()

        button6 = ttk.Button(self, text="Show Problem",
                            command=self.showTxt)
        button6.pack()

    def showTxt(self):
        global final_ques,root
        root = Tk()
        T = Text(root, height=100, width=100)
        T.pack()
        T.insert(END,final_ques[3])

class PageFive(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Page five!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
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
        button6 = ttk.Button(self, text="Show Problem",
                            command=self.showTxt)
        button6.pack()

    def showTxt(self):
        global final_ques,root
        root = Tk()
        T = Text(root, height=100, width=100)
        T.pack()
        T.insert(END,final_ques[4])


#root = tk.Tk()
#root.geometry("400x300")
app = SeaofBTCapp()
app.mainloop()
file1.close()
file2.close()
file3.close()
file4.close()



