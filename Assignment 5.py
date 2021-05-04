#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Detect Floating Point Number

import re

for x in range(int(input())):

    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))


# In[6]:


#Group(), Groups() & Groupdict()

import re 
m = re.search(r'([A-Za-z0-9])\1',input())
if m:
    print(m.group(1))
    
else:
    print -1


# In[7]:


#Re.findall() & Re.finditer()

import re

consonants = 'qwrtypsdfghjklzxcvbmn'
vowels = 'aeiou'

match = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])',input(),flags = re.I)
if match:
    for i in match:
        print (i)
else:
    print(-1)


# In[8]:


# Re.start() & Re.end()

string = input()
k = input()
import re
pattern = re.compile(k)
r = pattern.search(string)
if not r: print ("(-1, -1)")
while r:
    print( "({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(string,r.start() + 1)


# In[3]:


#Regex Substitution

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

t=[]
def change(match):
    if match.group(0) == '&&' :
        return 'and'
    elif match.group(0) == '||' :
        return 'or'
    
n = int(input())
for i in range(n):
    t.append(input())
    
    
t = '\n'.join(t)

print(re.sub(r"(?<= )(&&|\|\|)(?= )", change, t))
    


# In[1]:


# Validating Roman Numerals

thousandnum = 'M{0,3}'
hundrednum = '(C[MD]|D?C{0,3})'
tensnum = '(X[CL]|L?X{0,3})'
digitnum = '(I[VX]|V?I{0,3})'



regex_pattern = r"%s%s%s%s$" % (thousandnum, hundrednum, tensnum, digitnum)	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))


# In[2]:


#Validating phone numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for i in range(n):
    number = input()
    if(len(number) == 10 and number.isdigit()):
        op = re.findall(r"^[789]\d{9}$", number)
        if(len(op)==1):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')        


# In[1]:


#Validating and Parsing Email Addresses


import re

from email.utils import *

n = int(input())
for i in range(n):
    email = parseaddr(input())
    if bool(re.search(r'^[a-zA-Z][\w\-\.]*@[A-Za-z]+\.[a-zA-Z]{1,3}$', email[1])):
        print(formataddr(email))


# In[11]:


#Hex Color Code

import re

n = int(input())
inCss = False
for _ in range (n):
    string = input()
    if '{' in string :
        inCss = True
        
    elif '}' in string :
        inCss = False
        
    elif inCss:
        for color in re.findall(r'^#[0-9a-fA-F]{3,6}', string):
            print(color)


# In[12]:


#HTML Parser - Part 1

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ('Start :',tag)
        for attr in attrs:
                print( '->',' > '.join(map(str,attr)))
    def handle_endtag(self, tag):
        print ('End   :',tag)
    def handle_startendtag(self, tag, attrs):
        print ('Empty :',tag)
        for attr in attrs:
                print ('->',' > '.join(map(str,attr)))

html = ""
for i in range(int(input())):
    html += input()
                    
                
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# In[13]:


#HTML Parser - Part 2

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if '\n' not in data:
            print('>>> Single-line Comment')
            print(data)
        elif '\n' in data:
            print('>>> Multi-line Comment')
            print(data)
    def handle_data(self, data):
        if data != '\n':
            print('>>> Data')
            print(data)
  
  
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()


# In[6]:


# Detect HTML Tags, Attributes and Attribute Values

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print (tag)
        for attr in attrs:
            print("->"," > ".join(attr))

parser = MyHTMLParser()

html = ""
for i in range(int(input())):
    html += input()
    html += '\n'

    
    


# In[7]:


#Validating UID

import re

for i in range(int(input())):
    n = input().strip()
    if n.isalnum() and len(n) == 10:
        if(bool(re.search(r'(.*[A-Z]){2,}',n)) and bool(re.search(r'(.*[0-9]){3,}',n))):
             if re.search(r'.*(.).*\1+.*',n):
                print("Invalid")
             else:
                print("Valid")
        else:
             print("Invalid")
    else:
             print("Invalid")            


# In[8]:


#Validating Credit Card Numbers  

import re

for i in range(int(input())):
    string = input().strip()
    match1 = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$',string)
    if match1:
        match2 = "".join(match1.group(0).split("-"))
        match3 = re.search(r'(\d)\1{3,}',match2)
        print('Invalid') if match3 else print('Valid')
    else:
        print("Invalid")


# In[9]:


#Validating Postal Codes

regex_integer_in_range = r"^[1-9][\d]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


# In[10]:


#Matrix Script

import re
  
(n,m) = map(int, input().strip().split())
  
matrix = []
  
for i in range(n):
    matrix.append(input())
  
phrase = ""
  
for j in range(m):
    for i in range(n):
        phrase += str(matrix[i][j])
  
# # phrase = "q"+str(phrase)+"q"
# print phrase
print (re.sub(r'\b[^a-zA-Z0-9]+\b', r' ', phrase))


# In[ ]:




