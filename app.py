import streamlit as st
import requests
import pandas as pd
from streamlit_geolocation import streamlit_geolocation

# Get user location
st.title("Sustainable Agriculture DSS 🌱")
st.write("Fetching your location automatically...")

location = streamlit_geolocation()

if location and "latitude" in location and "longitude" in location:
    latitude = location["latitude"]
    longitude = location["longitude"]

    st.write(f"📍 Detected Location: **Lat:** {latitude}, **Lon:** {longitude}")

    # Fetch weather data from Open-Meteo
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,precipitation"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        
        # Extract relevant data
        current_weather = data["current_weather"]
        temperature = current_weather["temperature"]
        humidity = data["hourly"]["relativehumidity_2m"][0]  # Current humidity
        rainfall = data["hourly"]["precipitation"][0]  # Current precipitation
        
        # Store weather data in a DataFrame
        weather_data = {
            "Temperature (°C)": [temperature],
            "Humidity (%)": [humidity],
            "Rainfall (mm)": [rainfall]
        }
        df = pd.DataFrame(weather_data)

        # Generate recommendation
        def generate_recommendation(df):
            if df["Rainfall (mm)"].iloc[0] < 5 and df["Temperature (°C)"].iloc[0] > 30:
                return "🚰 Recommend irrigation: Low rainfall and high temperature detected."
            elif df["Humidity (%)"].iloc[0] > 80:
                return "⚠️ High humidity detected. Monitor for fungal diseases."
            else:
                return "✅ Conditions are optimal. No action needed."

        recommendation = generate_recommendation(df)

        # Display results
        st.write("### Weather Data")
        st.write(df)
        st.write("### Recommendation")
        st.success(recommendation)

    else:
        st.error("Failed to fetch weather data. Please try again.")
else:
    st.warning("⚠️ Please allow location access to fetch weather data.")
