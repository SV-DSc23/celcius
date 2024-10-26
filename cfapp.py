import streamlit as st

# Temperature conversion functions
def c_to_f(c):
    return (9/5 * c) + 32

def f_to_c(f):
    return (5/9) * (f - 32)

# Streamlit app title
st.title("Temperature Converter")

# Input field and dropdown for original temperature value and unit
input_temp = st.number_input("Enter temperature:", format="%.2f")
input_unit = st.selectbox("Unit", ("Celsius", "Fahrenheit"), key="input_unit")

# Output field and dropdown for converted temperature value and unit
converted_temp = st.empty()
output_unit = st.selectbox("Convert to", ("Fahrenheit", "Celsius"), key="output_unit")

# Function to perform the temperature conversion based on selected units
def convert_temperature():
    if input_unit == "Celsius" and output_unit == "Fahrenheit":
        result = c_to_f(input_temp)
    elif input_unit == "Fahrenheit" and output_unit == "Celsius":
        result = f_to_c(input_temp)
    else:
        result = input_temp  # No conversion needed if input and output units are the same
    converted_temp.write(f"Converted Temperature: {result:.2f} °{output_unit[0]}")

# Convert button to trigger the conversion
if st.button("Convert") or st.session_state.get("input_enter_pressed", False):
    convert_temperature()

# Allow conversion on hitting 'Enter' in the input field
st.session_state["input_enter_pressed"] = st.number_input