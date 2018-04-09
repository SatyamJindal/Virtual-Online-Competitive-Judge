import random as rd
import lxml
import bs4 as bs
import urllib.request
url = 'https://www.codechef.com/problems/'
sauce = urllib.request.urlopen('https://www.codechef.com/problems/school/').read()
soup = bs.BeautifulSoup(sauce,'lxml')
#url1=[]
beggi=['CNDLOVE', 'SINS', 'SPAMCLAS', 'ORDTEAMS', 'ZUBTRCNT', 'FRK', 'ZUBREACH', 'CHEFCHR', 'BIGSALE', 'CHEGLOVE', 'COUPSYS', 'L56GAME', 'CODERLIF', 'SURVIVE', 'HILLS', 'CO92JUDG', 'SMRSTR', 'KFIB', 'RGAME', 'VILTRIBE', 'CHRL4', 'GIT01', 'STRLBP', 'GOODBAD', 'CCOOK', 'RNDPAIR', 'NW1', 'FBMT', 'RECTANGL', 'ALEXTASK', 'TWEED', 'KOL16B', 'SEBIHWY', 'LISDIGIT', 'LIKECS01', 'C00K0FF', 'LTM40AB', 'SNELECT', 'ENTEXAM', 'KOL16J', 'PERFCONT', 'CHEFAPAR', 'MATPAN', 'CK87MEDI', 'CHNGOR', 'CHEFROUT', 'SNAKPROC', 'XENTASK', 'TEMPLELA', 'SEGM01', 'ADACRA', 'CHEFDETE', 'NOTINCOM', 'LADDU', 'COOMILK', 'BUGCAL', 'CHEFSUM', 'NITIKA', 'BRLADDER', 'ACBALL', 'LOSTMAX', 'LCOLLIS', 'GOODSET', 'EGRANDR', 'ELEVSTRS', 'DEVARRAY', 'RAINBOWA', 'ICPC16B', 'SIMDISH', 'OMWG', 'ANKTRAIN', 'UTMOPR', 'CHCHCL', 'CHEFSTUD', 'STICKS', 'CATSDOGS', 'WDTBAM', 'TTENIS', 'TWONMS', 'DWNLD', 'TALAZY', 'TICKETS5', 'SIMPSTAT', 'ALTARAY', 'CANDY123', 'FLOW015', 'ALPHABET', 'CHRL2', 'SUBINC', 'BRACKETS', 'STRPALIN', 'CFRTEST', 'LONGSEQ', 'COLOR', 'DEVUGRAP', 'ICPC16A', 'MOVIEWKN', 'FRGTNLNG', 'CHEFARRP', 'KTTABLE', 'CHEFSQ', 'RRJOKE', 'VCS', 'CHN09', 'RECTSQ', 'TRICOIN', 'COPS', 'MISSP', 'MNMX', 'LCH15JAB', 'TWOSTR', 'FRUITS', 'PPSUM', 'CHEFSTLT', 'FLOW014', 'FLOW011', 'GDOG', 'FLOW016', 'FLOW009', 'HEADBOB', 'AMR15A', 'TRISQ', 'CHOPRT', 'FLOW010', 'SMPAIR', 'PRB01', 'PALL01', 'COMM3', 'FLOW013', 'FLOW005', 'FLOW008', 'FLOW018', 'ONP', 'RECIPE', 'FLOW017', 'REMISS', 'FSQRT', 'PERMUT2', 'FLOW007', 'SUMTRIAN', 'FLOW004', 'LUCKFOUR', 'START01', 'CIELRCPT', 'FLOW002', 'FLOW006', 'MUFFINS3', 'TLG', 'FLOW001', 'TSORT']
#for p in soup.find_all('a'):
#    url1.append(p.text)
#url_ind1 = url1.index('Accuracy')
#url1 = url1[64:-34]
#for i in range(1,len(url1)-9,3):
#    fin1.append(url1[i])
url+=beggi[rd.randrange(len(beggi))]
#print('url',url)
sauce = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(sauce,'lxml')


    
'''p_tags=[]
h3_tags=['Input','Output']
u_tags=[]

p_tags.append(soup.title.text)
for p in soup.find_all('p'):
    p_tags.append(p.text)
p_tags[0]=p_tags[0][:-11]
p_tags = list(filter(lambda x: x!='' and x!='\xa0',p_tags))

for p in soup.find_all('ul'):
    u_tags.append(p.text)'''
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
print(s)





