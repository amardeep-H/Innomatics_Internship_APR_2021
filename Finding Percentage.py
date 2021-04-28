#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Finding the percentage

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    total_sum_of_marks=0
    average = float()
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks[query_name]:
        total_sum_of_marks=total_sum_of_marks+i
    average = total_sum_of_marks/len(student_marks[query_name])
    print("%.2f" %average)

