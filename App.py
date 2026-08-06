import streamlit as st
import pandas as pd
import joblib

model = joblib.load('Random_Forest_MentalScore.pkl')
Scaler = joblib.load('Scaler.pkl')
Columns = joblib.load('columns.pkl')

st.title('Check Your Mental_Score')
st.subheader('Provide The Following Details')


age = st.slider("Age",18,70,25)

Sex = st.selectbox("GENDER",['MALE','FEMALE'])

col1,col2 = st.columns(2)
with col1:
    Countries = ['Other','India','USA','Canada','Australia','UK','Germany','Mexico','Turkey','France']
    selected_countries = st.selectbox("Select Your Country:",
                                    options=Countries,
                                    index=5)
    st.write("You selected :", selected_countries)

with col2:
    Academic_Level = ['Undergraduate', 'Graduate', 'High School']
    selected_Academic = st.selectbox("Select Your Academic Level :",options=Academic_Level)
    st.write("Your Current Academic Level :",selected_Academic)

col3,col4 = st.columns(2)
with col3:
    Most_Used_Platform = ['Facebook', 'LinkedIn', 'Instagram', 'Snapchat', 'Twitter',
            'YouTube', 'TikTok', 'LINE', 'KakaoTalk', 'VKontakte', 'WhatsApp','WeChat']
    selected_Platform = st.selectbox("Select Your Fav Platform :",options=Most_Used_Platform)
    st.write("Your Most Used & Fav Platform :",selected_Platform)

with col4:
    Purpose_Of_Use = ['Networking', 'Education', 'Entertainment', 'News']
    Select_Usage = st.selectbox("Your Purpose of Using:",options= Purpose_Of_Use)
    st.write("Your Main Purpose of Using :",Select_Usage)


Avg_Usage = st.number_input("Enter Average Usage of Screen Hrs:",min_value=1,max_value=24)
st.write(f"You Avg Screen Time: {Avg_Usage}")

Daily_Unlocks = st.number_input("Avg Unlocks Of Phone : ",min_value=20,max_value=300)
st.write(f"Your Daily Unlocks : {Daily_Unlocks}")

study_hour = st.slider("Study Hour's",0.3,10.0,4.0)
st.write(f"Study Hours : {study_hour}")

physical_Activity = st.slider("The Physical Activity You Had Done:",0.0,5.0,2.0)
st.write(f"The Phyical Activity You Had: {physical_Activity}")

Sleep = st.slider("The Amount Of Quality Sleep you Had per Day:",3.0,24.0,8.0)
st.write(f"You Slept in a Day: {Sleep}")

stress = st.selectbox("Your Stress Level :",['Medium', 'Low', 'Very High', 'High'])
st.write(f"Your Stress Level: {stress}")

Group_countries = st.selectbox("The Group of Counrtys:",['Other', 'Canada', 'USA', 'India', 'Australia', 'UK', 'Germany',
       'France', 'Mexico', 'Turkey'])

                              
if st.button("Predict"):
    raw_input = pd.DataFrame([{
        'Age': age,
        'Gender': Sex,
        'Country': selected_countries,
        'Academic_Level': selected_Academic,
        'Most_Used_Platform': selected_Platform,
        'Purpose_Of_Use': Select_Usage,
        'Avg_Daily_Usage_Hours': Avg_Usage,
        'Daily_Unlocks': Daily_Unlocks,
        'Study_Hours': study_hour,
        'Physical_Activity_Hours': physical_Activity,
        'Sleep_Hours_Per_Night': Sleep,
        'Stress_Level': stress,
        'Group_countries': Group_countries
    }])
   
    prediction = model.predict(raw_input)

    st.success(f"Predicted Mental Health Score: {prediction[0]:.2f}")

