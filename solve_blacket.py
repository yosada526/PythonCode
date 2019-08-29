#!/usr/bin/python3
import re

#get brackets size
def getSize(s):
    m=0
    count=0
    for i in range(len(s)):
        if s[i]=='(':
            count+=1
        elif s[i]==')':
            m=max(m,count)
            count-=1
    return m

def solve(arr,s1):
    for i in range(len(arr)-1):
        s2 = arr[i+1]
        if getSize(s1) > getSize(s2):
            s1=s1[:-1]+s2+')'
        elif getSize(s1) == getSize(s2):
            s1=s1+s2
        else:
            s1='('+s1+s2[1:]
    return s1

def parseQue(s):
    arr=s.split('+')
    return arr

def getAnswer(m):
    m = re.sub('[^()+]','',m)
    arr = parseQue(m)
    s1 = arr[0]
    s1 = solve(arr,s1)
    print('solve')
    print(m)
    print(s1)

getAnswer('(()) + ()')
getAnswer('() + (()) + ((()))')
