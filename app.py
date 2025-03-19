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
            "Rainfall (mm)": [rainfall],
        }
        df = pd.DataFrame(weather_data)

        # Generate recommendation
        def generate_recommendation(df):
            temperature = df["Temperature (°C)"].iloc[0]
            humidity = df["Humidity (%)"].iloc[0]
            rainfall = df["Rainfall (mm)"].iloc[0]
            recommendations = []

            # Temperature-based recommendations
            if temperature < 15:
                recommendations.append(
                    "🌡️ Temperature is too low. Consider using protective covers or greenhouses.\n"
                )
            elif temperature > 30:
                recommendations.append(
                    "🔥 High temperature detected. Ensure adequate irrigation and consider shade techniques.\n"
                )
            else:
                recommendations.append("✅ Temperature is within the optimal range.\n")

            # Humidity-based recommendations
            if humidity < 40:
                recommendations.append(
                    "💧 Low humidity detected. Consider irrigation or misting to maintain moisture levels.\n"
                )
            elif humidity > 80:
                recommendations.append(
                    "⚠️ High humidity detected. Monitor for fungal diseases and improve ventilation.\n"
                )
            else:
                recommendations.append("✅ Humidity is within the optimal range.\n")

            # Rainfall-based recommendations
            if rainfall < 5:
                recommendations.append(
                    "🚰 Low rainfall detected. Consider irrigation to maintain soil moisture.\n"
                )
            elif rainfall > 50:
                recommendations.append(
                    "🌧️ Heavy rainfall detected. Ensure proper drainage to prevent waterlogging.\n"
                )
            else:
                recommendations.append("✅ Rainfall is within the optimal range.\n")

            return "\n".join(recommendations)

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
