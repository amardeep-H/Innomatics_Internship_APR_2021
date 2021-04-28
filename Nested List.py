#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Nested Lists
if __name__ == '__main__':
    name_score = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_score.append([name,score])
    sorted_score = sorted(list(set([x[1]for x in name_score])))
    second_low = sorted_score[1]
    low1 = []   
    for student in name_score:
        if second_low == student[1]:
            low1.append(student[0])
        
    for student in sorted(low1):
        print(student)

