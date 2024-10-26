import streamlit as st
from streamlit_option_menu import option_menu

# Define temperature conversion functions
def convert_temperature(value, from_unit, to_unit):
    conversions = {
        ("Celsius", "Fahrenheit"): lambda c: (9/5 * c) + 32,
        ("Fahrenheit", "Celsius"): lambda f: (5/9) * (f - 32),
        ("Celsius", "Kelvin"): lambda c: c + 273.15,
        ("Kelvin", "Celsius"): lambda k: k - 273.15,
        ("Fahrenheit", "Kelvin"): lambda f: (5/9) * (f - 32) + 273.15,
        ("Kelvin", "Fahrenheit"): lambda k: (9/5 * (k - 273.15)) + 32
    }
    if from_unit == to_unit:
        return value
    return conversions.get((from_unit, to_unit), lambda x: x)(value)

# Set up the Streamlit app with a stylish title and subtitle
st.set_page_config(page_title="Temperature Converter", page_icon="🌡️")
st.title("🌡️ Temperature Converter")
st.markdown("### Convert temperatures between various units easily and stylishly!")

# UI setup for user input and conversion
st.markdown("---")
col1, col2 = st.columns([2, 2])

# Temperature input and units dropdown
with col1:
    st.markdown("#### Enter Temperature")
    temp_value = st.number_input("", min_value=-273.15, format="%.2f", help="Input temperature to convert")
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"], index=0)

# Converted temperature display and units dropdown
with col2:
    st.markdown("#### Converted Temperature")
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"], index=1)
    if st.button("Convert 🌡️"):
        converted_value = convert_temperature(temp_value, from_unit, to_unit)
        st.markdown(f"### {converted_value:.2f} °{to_unit[0]}")

# Adding some fancy sidebar options for style
with st.sidebar:
    st.markdown("## Customize the look")
    option_menu(
        menu_title="Choose Theme", 
        options=["Light Mode", "Dark Mode"],
        icons=["sun", "moon-stars"],
        menu_icon="paint-brush"
    )

st.markdown(
    """
    <style>
    div.stButton > button {
        font-size: 18px;
        color: white;
        background-color: #4CAF50;
        border-radius: 8px;
        padding: 10px;
    }
    input[type="number"] {
        border: 2px solid #4CAF50;
        border-radius: 4px;
    }
    </style>
    """, unsafe_allow_html=True
)