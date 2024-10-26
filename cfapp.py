import streamlit as st
from streamlit_option_menu import option_menu

# Temperature conversion functions
def c_to_f(c):
    return (9/5 * c) + 32

def f_to_c(f):
    return (5/9) * (f - 32)

def k_to_c(k):
    return k - 273.15

def c_to_k(c):
    return c + 273.15

def f_to_k(f):
    return c_to_k(f_to_c(f))

def k_to_f(k):
    return c_to_f(k_to_c(k))

# Convert temperature based on units
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return c_to_f(value)
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return f_to_c(value)
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return c_to_k(value)
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return k_to_c(value)
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return f_to_k(value)
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return k_to_f(value)
    return None

# Streamlit app title and styling
st.title("🌡️ Fancy Temperature Converter")
st.markdown(
    """
    <style>
        .stTextInput, .stSelectbox {width: 100%;}
        div[role="button"] {width: 150px; height: 40px; font-size: 16px; color: #ffffff; background-color: #4CAF50; border-radius: 5px;}
        h1, h2, h3, h4, h5, h6 {color: #4CAF50;}
    </style>
    """,
    unsafe_allow_html=True
)

# UI layout
col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

# Temperature input field
with col1:
    temperature_value = st.number_input("Enter Temperature:", format="%.2f")

# From unit dropdown
with col2:
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])

# To unit dropdown
with col3:
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])

# Display converted temperature
with col4:
    converted_value = st.text_input("Converted Value", value="", disabled=True)

# Convert button with Enter key trigger
if st.button("Convert") or temperature_value:
    result = convert_temperature(temperature_value, from_unit, to_unit)
    if result is not None:
        st.text_input("Converted Value", f"{result:.2f}", disabled=True)
    else:
        st.write("Conversion not supported")