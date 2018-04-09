from tkinter import *
from PIL import Image, ImageTk
import random as rd
import lxml
import bs4 as bs
import urllib.request
url = 'https://www.codechef.com/problems/'
sauce = urllib.request.urlopen('https://www.codechef.com/problems/school/').read()
soup = bs.BeautifulSoup(sauce,'lxml')
beggi=['CNDLOVE', 'SINS', 'SPAMCLAS', 'ORDTEAMS', 'ZUBTRCNT', 'FRK', 'ZUBREACH', 'CHEFCHR', 'BIGSALE', 'CHEGLOVE', 'COUPSYS', 'L56GAME', 'CODERLIF', 'SURVIVE', 'HILLS', 'CO92JUDG', 'SMRSTR', 'KFIB', 'RGAME', 'VILTRIBE', 'CHRL4', 'GIT01', 'STRLBP', 'GOODBAD', 'CCOOK', 'RNDPAIR', 'NW1', 'FBMT', 'RECTANGL', 'ALEXTASK', 'TWEED', 'KOL16B', 'SEBIHWY', 'LISDIGIT', 'LIKECS01', 'C00K0FF', 'LTM40AB', 'SNELECT', 'ENTEXAM', 'KOL16J', 'PERFCONT', 'CHEFAPAR', 'MATPAN', 'CK87MEDI', 'CHNGOR', 'CHEFROUT', 'SNAKPROC', 'XENTASK', 'TEMPLELA', 'SEGM01', 'ADACRA', 'CHEFDETE', 'NOTINCOM', 'LADDU', 'COOMILK', 'BUGCAL', 'CHEFSUM', 'NITIKA', 'BRLADDER', 'ACBALL', 'LOSTMAX', 'LCOLLIS', 'GOODSET', 'EGRANDR', 'ELEVSTRS', 'DEVARRAY', 'RAINBOWA', 'ICPC16B', 'SIMDISH', 'OMWG', 'ANKTRAIN', 'UTMOPR', 'CHCHCL', 'CHEFSTUD', 'STICKS', 'CATSDOGS', 'WDTBAM', 'TTENIS', 'TWONMS', 'DWNLD', 'TALAZY', 'TICKETS5', 'SIMPSTAT', 'ALTARAY', 'CANDY123', 'FLOW015', 'ALPHABET', 'CHRL2', 'SUBINC', 'BRACKETS', 'STRPALIN', 'CFRTEST', 'LONGSEQ', 'COLOR', 'DEVUGRAP', 'ICPC16A', 'MOVIEWKN', 'FRGTNLNG', 'CHEFARRP', 'KTTABLE', 'CHEFSQ', 'RRJOKE', 'VCS', 'CHN09', 'RECTSQ', 'TRICOIN', 'COPS', 'MISSP', 'MNMX', 'LCH15JAB', 'TWOSTR', 'FRUITS', 'PPSUM', 'CHEFSTLT', 'FLOW014', 'FLOW011', 'GDOG', 'FLOW016', 'FLOW009', 'HEADBOB', 'AMR15A', 'TRISQ', 'CHOPRT', 'FLOW010', 'SMPAIR', 'PRB01', 'PALL01', 'COMM3', 'FLOW013', 'FLOW005', 'FLOW008', 'FLOW018', 'ONP', 'RECIPE', 'FLOW017', 'REMISS', 'FSQRT', 'PERMUT2', 'FLOW007', 'SUMTRIAN', 'FLOW004', 'LUCKFOUR', 'START01', 'CIELRCPT', 'FLOW002', 'FLOW006', 'MUFFINS3', 'TLG', 'FLOW001', 'TSORT']
'''url+=beggi[rd.randrange(len(beggi))]
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
s = s[ind1+30:ind-8]'''



class Window(Frame):

    def __init__(self,master = None):
        Frame.__init__(self,master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Virual Competitive Judge")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)
        Questions = Menu(menu)
        Questions.add_command(label='Question 1',command = self.showTxt)
        Questions.add_command(label='Question 2',command = self.showTxt)
        Questions.add_command(label='Question 3')
        Questions.add_command(label='Question 4')
        Questions.add_command(label='Question 5')
        menu.add_cascade(label='Questions',menu=Questions)

        #quitButton = Button(self, text = "Exit", command = self.client_exit)
        #quitButton.place(x=400,y=0)


    def showTxt(self):
        global url,sauce,soup,beggi
        url+=beggi[rd.randrange(len(beggi))]
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
        text = Label(self,text = s)
        text.pack()

    def client_exit(self):
        exit()

root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()


        
        
