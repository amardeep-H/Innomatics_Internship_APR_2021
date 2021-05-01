#!/usr/bin/env python
# coding: utf-8

# In[3]:


#sWAP cASE

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# In[4]:


#What's Your Name?

def print_full_name(first, last):
    # Write your code here
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


# In[5]:


#Mutations

def mutate_string(string, position, character):
    l=list(string)
    l[position] = character
    string = ''.join(l)
    return string
    
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


# In[6]:


#Find a string

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# In[8]:


#String Validators

if __name__ == '__main__':
    s = input()
    print(any([char.isalnum() for char in s]))
    print(any([char.isalpha() for char in s]))
    print(any([char.isdigit() for char in s]))
    print(any([char.islower() for char in s]))
    print(any([char.isupper() for char in s]))


# In[9]:


#Text Alignment

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# In[13]:


#Text Wrap
import textwrap

def wrap(string, max_width):
   return textwrap.fill(string, max_width)
        

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# In[14]:


#Designer Door Mat

n, m = map(int, input().split())
for i in range(1, n, 2):
    print((str('.|.')*i).center(m,'-'))
print('WELCOME'.center(m,'-'))
for i in range(n-2, -1, -2):
    print((str('.|.')*i).center(m, '-'))


# In[15]:


#String Formatting

def print_formatted(number):
    # your code goes here
    width = len("{0:b}".format(number))
    
    for i in range(1, number+1):
        print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i,w=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


# In[17]:


#Alphabet Rangoli

def print_rangoli(size):
    # your code goes here
    
    for i in range(size):
        s = "-".join(chr(ord('a')+size-j-1) for j in range(i+1))
        print((s+s[::-1][1:]).center(size*4-3, '-'))

    for i in range(n-1):
        s = "-".join(chr(ord('a')+size-j-1) for j in range(size-i-1))
        print((s+s[::-1][1:]).center(size*4-3, '-'))
    
        
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
    



# In[21]:


#Capitalize!
def solve(s):
    for i in s.split():
        s=s.replace(i,i.capitalize())
    return s

if __name__ == '__main__':
    s=input()
    ss = solve(s)
    print(ss)


# In[22]:


#The Minion Game

def minion_game(string):
    
    # your code goes here
    SS = string.strip()
    S_length = len(SS)
    player1, player2 = 0,0

    for i in range(S_length):
        if SS[i] in "AEIOU":
            player1 += S_length - i
        else:
            player2 += S_length - i        
            
    if player1 > player2:
        print ("Kevin", player1)
    elif player1 < player2:
        print("Stuart", player2)
    else:
        print("Draw")



if __name__ == '__main__':
    s = input()
    minion_game(s)


# In[23]:


#Merge the Tools!

def merge_the_tools(string, k):
    # your code goes here
   
    num_subsegments = int(len(string) / k)

    for index in range(num_subsegments):
        
        t = string[index * k : (index + 1) * k]
        
        u = ""
        
        for c in t:
            if c not in u:
                u += c

        # Print final converted string
        print(u)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# In[ ]:




