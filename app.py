import streamlit as st
import pandas as pd
from skops.io import load, get_untrusted_types

model_file = "car_price_model.skops"
trusted = get_untrusted_types(file=model_file)
model = load(model_file, trusted=trusted)

df = pd.read_csv("car_data.csv")

brands = df["Brand"].unique()
models_by_brand = {b: df[df["Brand"] == b]["model"].unique() for b in brands}

st.title("🚗 Car Price Prediction App")
st.sidebar.header("Car Details")

selected_brand = st.sidebar.selectbox("Brand", brands)
selected_model = st.sidebar.selectbox("Model", models_by_brand[selected_brand])
year = st.sidebar.number_input("Year", min_value=1990, max_value=2026, step=1)
km_driven = st.sidebar.number_input("Kilometers Driven", min_value=0)
fuel_type = st.sidebar.selectbox("Fuel Type", df["FuelType"].unique())
transmission = st.sidebar.selectbox("Transmission", df["Transmission"].unique())
owner = st.sidebar.selectbox("Owner", df["Owner"].unique())

if st.sidebar.button("Predict"):
    input_data = pd.DataFrame([{
        "Brand": selected_brand,
        "model": selected_model,
        "Year": year,
        "Age": 2026 - year,
        "kmDriven": km_driven,
        "FuelType": fuel_type,
        "Transmission": transmission,
        "Owner": owner
    }])
    prediction = model.predict(input_data)
    st.success(f"Predicted Price: ₹{prediction[0]:,.2f}")
