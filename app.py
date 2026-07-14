import streamlit as st
import pandas as pd
import numpy as np

def checker(stats,our_num,low_lim, high_lim):
        if (our_num >= low_lim and our_num <= high_lim):
            st.success(stats + "                  Normal")
        else:
            st.warning(stats + "                Abnormal")
def bpChecker(stats,num1,num2,low_lim1,high_lim1,low_lim2,high_lim2):
        if ((num1 >= low_lim1 and num1 <= high_lim1) and (num2 >= low_lim2 and num2 <= high_lim2)):
            st.success(stats + "                  Normal")
        else:
            st.warning(stats + "                Abnormal") 
def converter (age,temperature,heart_rate,systolic,diastolic,Respiratory_rate ,SpO2,Go):
    try:
        age = int(age)
        temperature = float(temperature)
        heart_rate = float(heart_rate)
        systolic = float(systolic)
        diastolic = float(diastolic)
        Respiratory_rate = float(Respiratory_rate )
        SpO2 = float(SpO2)
        vitalis = [age,temperature,heart_rate,systolic,diastolic,Respiratory_rate,SpO2]
        if any(item < 0 for item in vitalis):
            st.error("You have to enter numbers equal or greater than 0")
            Go = False
        return age,temperature,heart_rate,systolic,diastolic,Respiratory_rate,SpO2,Go
        
    except ValueError:
        st.error("Enter numbers that are equal to or greater than 0")
        Go = False
        return age,temperature,heart_rate,systolic,diastolic,Respiratory_rate,SpO2,Go
def Allchecker(a,vitals,temp,heart,sys,dia,breathe,SpO2,checker,bpChecker):
        if (a > 17):
            i = 0
        else:
            i = 2
        checker("Temperature",temp,vitals["Temperature"][i],vitals["Temperature"][i+1])
        checker("Heart rate",heart,vitals["Heart rate"][i],vitals["Heart rate"][i+1])
        bpChecker("Blood Pressure",sys,dia,vitals["Sys"][i],vitals["Sys"][i+1],vitals["Dia"][i],vitals["Dia"][i+1])
        checker("Respiratory rate",breathe,vitals["Respiratory rate"][i],vitals["Respiratory rate"][i+1])
        checker("SpO2",SpO2,vitals["SpO2"][i],vitals["SpO2"][i+1])
class vitals_app:   
    with st.container():
        st.title("Vitals App")
        st.caption("Enter your vitals to check if you are in the normal range")
     
        vitals = {
            "Temperature": [36.1,37.2,36.1,37.5],
            "Heart rate": [60,100,80,140],
            "Sys": [90,120,80,110],
            "Dia":[60,80,50,75],
            "Respiratory rate":[12,18,20,30],
            "SpO2" :[95,100,95,100]
        }
        Go = True
        col1,col2= st.columns(2)
        age = col1.text_input("Age")
        sex = col2.selectbox("Sex",("Female", "Male"),)
        col3,col4 = st.columns(2)
        temp = col3.text_input("Temperature(°C)")
        heart = col4.text_input("Heart rate(bpm)")
        col5, slash, col6 = st.columns([6, 1, 6])

        sys = col5.text_input("Blood pressure (mmHg)")

        with slash:
            st.markdown("", unsafe_allow_html=True)
            st.markdown(
                "<h3 style='text-align:center;'>/</h3>",
                unsafe_allow_html=True
            )
        dia = col6.text_input("")
        col7,col8 = st.columns(2)
        breathe = col7.text_input("Respiratory rate")
        SpO2 = col8.text_input("SpO2(%)")

        if st.button("Check Results ✓"):
            st.caption("Results")
            
            age,temp,heart,sys,dia,breathe,SpO2,Go = converter (age,temp,heart,sys,dia,breathe,SpO2,Go)
            if Go:
                Allchecker(age,vitals,temp,heart,sys,dia,breathe,SpO2,checker,bpChecker)