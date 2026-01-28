import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu

df=pd.read_csv("Daily_Water_Intake.csv")


with st.sidebar:
    selected=option_menu("Daily_Water_Intake_Analysis",["Home","About US","Dataset","Individual Analysis","GroupBy Analysis",],icons=["house","people","table","bar-chart","link"],menu_icon=["cast"],orientation="vertical",default_index=0)


if selected == "Home":
        st.title("Daily Water Intake Analysis Dashboard")
        st.write("""
        This project analyzes daily water intake patterns based on 
        age, gender, weight, physical activity, weather, and hydration level.
        """)

        st.metric("Total Records", df.shape[0])
        st.metric("Average Water Intake (liters)", round(df["Daily Water Intake (liters)"].mean(), 2))

        st.subheader("Developed by Shiva keerth")

if selected == "About US":
    st.write("This is About Us")
    st.title("ℹ️ About This Project")

    st.write("""
    This project is a data analytics dashboard built using Streamlit to analyze 
    daily water intake patterns of individuals based on demographic and lifestyle factors.

    The dataset includes information such as age, gender, body weight, physical activity level,
    weather conditions, hydration level, and daily water consumption.
    """)

    st.subheader("🎯 Project Objective")
    st.write("""
    The main objective of this project is to identify patterns and relationships
    that influence daily water intake and hydration levels, and to present
    these insights through an interactive and user-friendly dashboard.
    """)

    st.subheader("🛠️ Tools & Technologies")
    st.write("""
    - Python
    - Pandas & NumPy
    - Matplotlib
    - Streamlit
    """)

    st.subheader("📊 Key Skills Demonstrated")
    st.write("""
    - Data cleaning and preprocessing
    - Exploratory Data Analysis (EDA)
    - GroupBy and aggregation analysis
    - Data visualization
    - Interactive dashboard development
    """)
    st.info("This project was created for learning and demonstrating practical data analytics skills.")

if selected== "Dataset":

    st.header("Dataset Overview")
    st.write("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Column Information")
    st.write(df.dtypes)

    st.subheader("Missing Values")
    st.write(df.isnull().sum())

if selected == "Individual Analysis":

    analysis_type = st.sidebar.selectbox(
        "Select Individual Analysis",
        [
            "1.Age Analysis",
            "2.Gender Analysis",
            "3.Weight Analysis",
            "4.Water Intake Analysis",
            "5.Physical Activity Analysis",
            "6.Weather Analysis",
            "7.Hydration Level Analysis"
        ]
    )
    if analysis_type == "1.Age Analysis":
     st.subheader("Age Distribution")
     age_counts = df["Age"].value_counts().sort_index()
     st.write(age_counts)

     fig, ax = plt.subplots()
     ax.bar(age_counts.index, age_counts.values,color="Purple")
     ax.set_xlabel("Age")
     ax.set_ylabel("Count")
     st.pyplot(fig)

     st.subheader("Age Statistics")
     st.write("Minimum Age:", df["Age"].min())
     st.write("Maximum Age:", df["Age"].max())
     st.write("Most Frequent Age:", df["Age"].mode()[0])

    if analysis_type == "2.Gender Analysis":
        st.subheader("Gender Distribution")
        gender_counts = df["Gender"].value_counts()
        st.write(gender_counts)

        fig, ax = plt.subplots()
        ax.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%")
        st.pyplot(fig)
    if analysis_type == "3.Weight Analysis":
        st.subheader("Weight Distribution")
        fig, ax = plt.subplots()
        ax.hist(df["Weight (kg)"], bins=20,edgecolor="White",color="black")
        ax.set_xlabel("Weight (kg)")
        ax.set_ylabel("Count")
        st.pyplot(fig)

        st.subheader("Weight Statistics")
        st.write("Minimum Weight:", df["Weight (kg)"].min())
        st.write("Maximum Weight:", df["Weight (kg)"].max())
        st.write("Most Common Weight:", df["Weight (kg)"].mode()[0])

    if analysis_type =="4.Water Intake Analysis":
        st.subheader("Daily Water Intake Distribution")
        fig, ax = plt.subplots()
        ax.hist(df["Daily Water Intake (liters)"], bins=20,edgecolor="White",color="green")
        ax.set_xlabel("Liters")
        ax.set_ylabel("Count")
        st.pyplot(fig)

        st.subheader("Low Water Intake")
        low_intake = df[df["Daily Water Intake (liters)"] < 2].shape[0]
        st.metric("People drinking < 2 liters", low_intake)

    if analysis_type =="5.Physical Activity Analysis":
        st.subheader("Physical Activity Levels")
        activity_counts = df["Physical Activity Level"].value_counts()
        st.write(activity_counts)

        fig, ax = plt.subplots()
        ax.bar(activity_counts.index, activity_counts.values,color=["red","yellow","black"])
        st.pyplot(fig)

    if analysis_type =="6.Weather Analysis":
        st.subheader("Weather Distribution")
        weather_counts = df["Weather"].value_counts()
        st.write(weather_counts)

        fig, ax = plt.subplots()
        ax.bar(weather_counts.index, weather_counts.values,color=["red","blue","black"])
        st.pyplot(fig)
    if analysis_type =="7.Hydration Level Analysis":
        st.subheader("Hydration Level Distribution")
        hydration_counts = df["Hydration Level"].value_counts()
        st.write(hydration_counts)

        fig, ax = plt.subplots()
        ax.bar(hydration_counts.index, hydration_counts.values,color=["orange","blue"])
        st.pyplot(fig)

        st.subheader("Most Common Hydration Level")
        st.write(df["Hydration Level"].mode()[0])
if selected == "GroupBy Analysis":

    groupby_type = st.sidebar.selectbox(
        "Select GroupBy Analysis",
        [
            "1.Age vs Avg Water Intake",
            "2.Gender vs Avg Water Intake",
            "3.Weight vs Avg Water Intake",
            "4.Activity Level vs Avg Water Intake",
            "5.Weather vs Avg Water Intake",
            "6.Hydration Level vs Avg Water Intake",
            "7.Weather & Activity vs Water Intake",
            "8.Age × Hydration Level",
            "9.Gender × Hydration Level",
            "10.Activity Level × Hydration Level",
            "11.Weather × Hydration Level",
            "12.Gender × Activity Level",
            "13.Age × Activity Level",
            "14.Weather × Activity Level"
        ]
    )
    if groupby_type == "1.Age vs Avg Water Intake":
        st.subheader("Age vs Average Water Intake")
        age_water = df.groupby("Age")["Daily Water Intake (liters)"].mean()
        st.write(age_water)

        fig, ax = plt.subplots()
        ax.plot(age_water.index, age_water.values,color="green")
        st.pyplot(fig)
    if groupby_type == "2.Gender vs Avg Water Intake":
        st.subheader("Gender vs Average Water Intake")
        gender_water = df.groupby("Gender")["Daily Water Intake (liters)"].mean()
        st.write(gender_water)

        fig, ax = plt.subplots()
        ax.bar(gender_water.index, gender_water.values,color=["pink","black"])
        st.pyplot(fig)
    if groupby_type == "3.Weight vs Avg Water Intake":
        st.subheader("Weight vs Average Water Intake")
        weight_water = df.groupby("Weight (kg)")["Daily Water Intake (liters)"].mean()
        st.write(weight_water)

        fig, ax = plt.subplots()
        ax.scatter(weight_water.index, weight_water.values,color="black")
        st.pyplot(fig)
    if groupby_type == "4.Activity Level vs Avg Water Intake":
        st.subheader("Activity Level vs Water Intake")
        activity_water = df.groupby("Physical Activity Level")["Daily Water Intake (liters)"].mean()
        st.write(activity_water)

        fig, ax = plt.subplots()
        ax.bar(activity_water.index, activity_water.values,color=["red","yellow","black"])
        st.pyplot(fig)
    if groupby_type == "5.Weather vs Avg Water Intake":
        st.subheader("Weather vs Water Intake")
        weather_water = df.groupby("Weather")["Daily Water Intake (liters)"].mean()
        st.write(weather_water)

        fig, ax = plt.subplots()
        ax.bar(weather_water.index, weather_water.values,color=["red","blue","black"])
        st.pyplot(fig)
    if groupby_type == "6.Hydration Level vs Avg Water Intake":
        st.subheader("Hydration Level vs Water Intake")
        hydration_water = df.groupby("Hydration Level")["Daily Water Intake (liters)"].mean()
        st.write(hydration_water)
        fig, ax = plt.subplots()
        ax.bar(hydration_water.index, hydration_water.values,color=["orange","blue"])
        st.pyplot(fig)
    if groupby_type == "7.Weather & Activity vs Water Intake":
        combo = df.groupby(
            ["Weather", "Physical Activity Level"]
        )["Daily Water Intake (liters)"].mean()
        st.dataframe(combo)
    if groupby_type == "8.Age × Hydration Level":
        st.subheader("Age vs Hydration Level")
        age_hydration = df.groupby(["Age", "Hydration Level"]).size().unstack()
        st.dataframe(age_hydration)
        fig, ax = plt.subplots()
        ax.plot(age_hydration.index, age_hydration.values,)
        ax.legend(age_hydration)
        st.pyplot(fig)

    if groupby_type == "9.Gender × Hydration Level":
        st.subheader("Gender vs Hydration Level")
        gender_hydration = df.groupby(["Gender", "Hydration Level"]).size()
        st.dataframe(gender_hydration)

    if groupby_type == "10.Activity Level × Hydration Level":
        st.subheader("Activity Level vs Hydration Level")
        activity_hydration = df.groupby(["Physical Activity Level", "Hydration Level"]).size()

        st.dataframe(activity_hydration)

    if groupby_type == "11.Weather × Hydration Level":
        st.subheader("Weather vs Hydration Level")
        weather_hydration = df.groupby(["Weather", "Hydration Level"]).size()

        st.dataframe(weather_hydration)

    if groupby_type == "12.Gender × Activity Level":
        st.subheader("Gender vs Physical Activity Level")
        gender_activity = df.groupby(["Gender", "Physical Activity Level"]).size()

        st.dataframe(gender_activity)

    if groupby_type == "13.Age × Activity Level":
        st.subheader("Age vs Physical Activity Level")
        age_activity = df.groupby(["Age", "Physical Activity Level"]).size()

        st.dataframe(age_activity)

    if groupby_type == "14.Weather × Activity Level":
        st.subheader("Weather vs Physical Activity Level")
        weather_activity = df.groupby(["Weather", "Physical Activity Level"]).size()

        st.dataframe(weather_activity)

