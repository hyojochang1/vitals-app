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

with st.container():
    st.title("Vitals App")
    st.caption("Enter your vitals to check if you are in the normal range")
    a_low = [36.1,60,90,60,12,95]
    a_hi = [37.2,100,120,80,18,100]
    p_low = [36.1,80,80,50,20,95]
    p_hi = [37.5,140,110,75,30,100]

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
        age = int(age)
        temp = float(temp)
        heart = float(heart)
        sys = float(sys)
        dia = float(dia)
        breathe = float(breathe)
        SpO2 = float(SpO2)
    
        if (age > 17):
            checker("Temperature",temp,a_low[0],a_hi[0])
            checker("Heart rate",heart,a_low[1],a_hi[1])
            bpChecker("Blood Pressure",sys,dia,a_low[2],a_hi[2],a_low[3],a_hi[3])
            checker("Respiratory rate",breathe,a_low[4],a_hi[4])
            checker("SpO2",SpO2,a_low[5],a_hi[5])
        else:
            checker("Temperature",temp,p_low[0],p_hi[0])
            checker("Heart rate",heart,p_low[1],p_hi[1])
            bpChecker("Blood Pressure",sys,dia,p_low[2],p_hi[2],p_low[3],p_hi[3])
            checker("Respiratory rate",breathe,p_low[4],p_hi[4])
            checker("SpO2",SpO2,p_low[5],p_hi[5])
        