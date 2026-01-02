import streamlit as st
import random

def classes():
    cls = st.number_input("Enter the number of classes: ",step = 1)
    if cls <= 0:
        st.write("Invalid Input")
        return None
    else:
        return cls

def subjects(cls):
    subject = st.number_input("Enter the number of subjects: ",step = 1)
    if subject <= cls:
        print("Invalid Input")
        return None
    
    sub = []
    for n in range(subject):
        sub.append((st.text_input(f"Enter the subject no. {n+1}: ")).upper())
        
    return sub

def number(sub,cls):
    num = []
    for n in sub:
        num.append(st.number_input(f"Enter the number of periods for '{n}': ",step = 1))
    if sum(num) != 48:
        st.write("48 periods is necessary")
        return None
    return num

def create(sub,cls,num):
    table = []
    for a in range(cls):
        table.append([])
        for b in range(6):
            table[a].append([])
            for c in range(8):
                table[a][b].append(0)
    

    for x in range(len(table)):
        period = [0]*len(sub)
        for y in range(6):
            for z in range(8):
                ver = False
                att = 0
                while not ver and att < 1000:
                    n = random.randint(1,len(sub))
                    att += 1
                #print(n)
                    if period[n-1] < num[n-1]:
                        clash = False
                        for ch in range(x):
                            if table[ch][y][z] == n:
                                clash = True
                                break
                        if not clash:
                            table[x][y][z] = n
                            period[n-1] += 1
                            ver = True
                    
    return table

def show(table,cls,sub):
    c = [None,None,None,None,None,None,None,None,None,None]
    st.write("TIME TABLE FOR CLASS NO.",cls)
    c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9] = st.columns(10)
    days = ["MON|","TUE|","WED|","THU|","FRI|","SAT|"]
    a = 0
    for x in days:
        if a == 0:
            c[0].write("DAYS")
        c[a+1].write(x)
        for y in table[cls-1][a]:
            if y == None:
                c[a+1].write(None)
            else:
                c[a+1].write(sub[y-1])
        a += 1
    for z in range(8):
        c[0].write(z+1)

st.title("Welcome to Time-Table Generator!")
cls = classes()
sub = subjects(cls)
num = number(sub,cls)
table = create(sub,cls,num)

for y in range(1,len(table)+1):
    print()
    show(table,y,sub)
    y+=1
