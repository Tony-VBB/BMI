import streamlit as st

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

st.title("⚖️ Body Mass Index (BMI) Calculator")

weight = st.number_input("Enter your weight (kg):", min_value=1.0, format="%.2f")
height = st.number_input("Enter your height (cm):", min_value=30.0, format="%.2f")

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    st.success(f"Your BMI is: **{bmi}**")
    st.info(f"Category: **{category}**")
