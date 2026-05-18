import streamlit as st
import random

st.title("Industrial Monitoring Dashboard")

temperature = random.randint(20, 40)
humidity = random.randint(40, 90)
gas_level = random.randint(100, 500)

st.metric("Temperature", f"{temperature} °C")
st.metric("Humidity", f"{humidity} %")
st.metric("Gas Level", gas_level)

if gas_level > 400:
    st.error("Warning! High Gas Level Detected")
else:
    st.success("System Operating Normally")
