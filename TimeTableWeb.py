import streamlit as st
import random

def inputSub():
    a = st.number_input("Enter the number of subjects: ",step = 1)
    sub = []
    for x in range(a):
        subject = st.text_input(f"Enter the subject{x+1}: ", key = x)
        subject = subject.upper()
        sub.append(subject)
    return sub

def inputNumber(sub):
    period = []
    for x in sub:
        a = st.number_input(f"Enter the number of periods for '{x}': ",step = 1,key = x)
        period.append(a)

    if sum(period) > 48:
        st.write("Too many periods alloted for a week.")
        return None

    return period

def choose(sub,period):
    peri = []
    for a in range(48):
        peri.append(None)
    p = []

    for x in range(len(sub)):
        for y in range(period[x]):
            k = random.randint(0,47)
            while k in p:
                k = random.randint(0,47)
            else:
                peri[k] = sub[x]
                p.append(k)
    return peri

def show(day):
    c = [None,None,None,None,None,None,None,None,None,None]
    st.write("YOUR TIMETABLE IS READY!!")
    c[0],c[1],c[2],c[3],c[4],c[5],c[6],c[7],c[8],c[9] = st.columns(10)
    days = ["DAYS","MON","TUE","WED","THU","FRI","SAT"]
    a = 0
    for x in days:
        if x == "DAYS":
            for n in range(0,9):
                if n == 0:
                    n = "DAYS"
                c[0].write(n)
        else:
            c[a+1].write(x)
            for y in day[a]:
                c[a+1].write(y)
            a += 1
            st.write()

st.title("Welcome to Time-Table Generator!")
sub = inputSub()
print(sub)
period = inputNumber(sub)
print(period)

if period == None:
    st.write("Please change the number of periods.")
    st.write("NOTE: A total of 48 periods is requested.")
else:
    peri = choose(sub,period)
    day1 = []
    day2 = []
    day3 = []
    day4 = []
    day5 = []
    day6 = []

    print(peri)
    for x in range(48):
        if x<8:
            day1.append(peri[x])
        elif x < 16:
            day2.append(peri[x])
        elif x < 24:
            day3.append(peri[x])
        elif x < 32:
            day4.append(peri[x])
        elif x < 40:
            day5.append(peri[x])
        elif x < 48:
            day6.append(peri[x])
        else:
            print("ERROR!")
            break
    day = [day1,day2,day3,day4,day5,day6]
    print(day)
    show(day)
    


