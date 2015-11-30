#############################从普通文本中读取、清理单词
ipath=input()#文本路径
import re
record=[re.sub('[\W\d_]',' ',x) for x in open(ipath)]
clean=[x.lower() for list in record for x in list.split()]

#############################计算单词的频率，并将计算结果储存
opath=input()#储存路径
from collections import Counter
import pickle
pickle.dump(Counter(clean),open(opath,'wb'))

#############################从储存数据的文件重新读取数据
data=pickle.load(open(opath,'rb'))

#############################将不同频率的单词，分别归类		
dd={}
for (voca,times) in data.items():
	if times in dd.keys():
		dd[times].append(voca)
	else:
		dd[times]=[voca]

#############################更新数据
#使用+-&|运算符
#交集并集只能取两个Counter的最大与最小，独有元素当成0次。加和减也只是对次数加减
#如果是要对元素进行加减，先转换为dict用for循环进行del语句，再转换为Counter

#############################删除重复副本
import os
os.chdir(r'文件夹路径')
import glob
for x in glob.glob('*(1).txt'):
	os.remove(x)

#############################合并文件夹，同名文件会被删除是个问题
path1=r'c:\users\pmhgms\python-2.7.9-docs-text'
path2=r'c:\users\pmhgms\a'
import shutil

def walkcopy(dir,targdir):
	a=os.listdir(dir)
	for x in a:
		if os.path.isdir(os.path.join(dir,x)):#千万不要忘记join
			walkcopy(os.path.join(dir,x),targdir)
		else:
			shutil.copy2(os.path.join(dir,x),os.path.join(targdir,x))

walkcopy(path1,path2)

#############################合并文件
txtlist=[]
a=os.listdir(path2)
for x in a:
	txtlist.append(open(os.path.join(path2,x)).read())

open('total2.txt','w').writelines(txtlist)

#############################加工英汉字典
pathd=r'C:\Users\pmhgms\Downloads\ci\c.txt'
recordc=[x for x in open(pathd)]
print recordc[:3]
a=[x.split('\t',1) for x in recordc]
dic=dict(tuple(a))
pickle.dump(dic,open('dict.pickle','wb'))

#############################将一个列表内的内容合并（词组）
gao=[' '.join(x) for x in gao]

#############################妹子图爬虫
import urllib2
import re
import time
import pickle

a='http://jandan.net/ooxx/page-'
c='#comments'
pattern=re.compile('<div.*?class="author">.*?<strong.*?>(.*?)</strong>.*?<div.*?class="text">.*?<img.*?src="(.*?)".*?>.*?<a.*?/a>.*?<span.*?>(.*?)</span>.*?<span.*?>(.*?)</span>',re.S)
data=[]

for b in range(900,1346):
    url=a+str(b)+c
    time.sleep(2)
    try:
        response=urllib2.urlopen(url)
    except urllib2.URLError,e:
        print e.code,e.reason
    else:
        print '!',
    content=response.read().decode('utf-8')
    items=re.findall(pattern,content)
    data.extend(items)

print data[0]
pickle.dump(data,open(r'c:\users\pmhgms\ooxx.pickle','wb'))

#############################储存数据
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
path1=r'c:\users\pmhgms\test.txt'
path2=r'c:\users\pmhgms\ooxx.pickle'
import pickle
data=pickle.load(open(path2,'rb'))
fil=open(path1,'a')
for x in data:
        print >>fil,x[0],',',x[2],',',x[3],',',x[1]
		
#############################去除文件名中空格
path1=r'C:\Users\pmhgms\Desktop\machine_leaning\Machine_Learning_Final_Projects_Autumn_2011'
path2=r'C:\Users\pmhgms\Desktop\machine_leaning\txts'
a=os.listdir(path1)
for x in a:
    xl=x.split()
    xo=''.join(xl)
    shutil.copy2(os.path.join(path1,x),os.path.join(path2,xo))
	
#############################pdf2txt
path1=r'C:\Users\pmhgms\Desktop\machine_leaning\txts'
fnames=os.listdir(path1)
for fname in fnames:
    fname=os.path.join(path1,fname)
    a,b=os.path.splitext(fname)
    out=a+'.txt'
    os.system('pdf2txt.py -o '+out+' '+fname)
	
#############################将文本替换为html
def test4(block):
    block=re.sub(r'(.+)',r'<em>\1</em>',block)
    return block

def sub(file):
	b=open('x.html','w')
	b.write(r'<html><body>')
	title=True
	for x in a:
		x=test4(x)
		if title:
			x=re.sub(r'(.+)',r'<h1>\1</h1>',x)
			title=False
		else:
			x=re.sub(r'(.+)',r'<li>\1</li>',x)
		b.write(x)
	b.write('</body></html>')
	b.close()

#############################验证随机游走
from pylab import *
def test(time):
    b=[]
    a,ini=0,10
    c=range(time)
    for t in c:
        a=random()*20-10
        ini=ini*a*0.01+ini
        b.append(ini)
    plot(c,b)
	
#############################凯利公式
 def kaili(p,a,b):
     b=a/float(b)
     return (p*(1+b)-1)/b