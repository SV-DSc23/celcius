import streamlit as st

# Temperature conversion functions
def c_to_f(c):
    return (9/5 * c) + 32

def f_to_c(f):
    return (5/9) * (f - 32)

# Streamlit app title
st.title("Temperature Converter")

# Input fields for Celsius and Fahrenheit
st.subheader("Convert Celsius to Fahrenheit")
celsius_input = st.number_input("Enter temperature in Celsius:", format="%.2f")
if st.button("Convert to Fahrenheit"):
    fahrenheit_result = c_to_f(celsius_input)
    st.write(f"Temperature in Fahrenheit: {fahrenheit_result:.2f} °F")

st.subheader("Convert Fahrenheit to Celsius")
fahrenheit_input = st.number_input("Enter temperature in Fahrenheit:", format="%.2f")
if st.button("Convert to Celsius"):
    celsius_result = f_to_c(fahrenheit_input)
    st.write(f"Temperature in Celsius: {celsius_result:.2f} °C")