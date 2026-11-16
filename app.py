
import streamlit as st
import pandas as pd
import plotly.express as px
import requests

from weather import (
    get_coordinates,
    get_weather,
    get_weather_description,
    get_weather_icon
)


# 1. Page configuration

st.set_page_config(
    page_title="Weatherly | Live Weather",
    page_icon="🌤️",
    layout="wide"
)


# 2. Application heading

st.title("🌤️ Weatherly")
st.caption("Your live weather dashboard")


# 3. City search

with st.form("weather_search"):

    city = st.text_input(
        "Search for a city",
        placeholder="Enter city name (e.g. Delhi, London, Tokyo)"
    )

    search_button = st.form_submit_button(
        "Get Weather",
        use_container_width=True
    )


# 4. Fetch weather when the user searches

if search_button:

    if not city.strip():

        st.warning("Please enter a city name.")

    else:

        try:

            with st.spinner("Fetching live weather data..."):

                location = get_coordinates(city.strip())

                if location is None:

                    st.error("City not found. Please try another city.")

                    st.session_state.pop("weather_data", None)
                    st.session_state.pop("location_data", None)

                else:

                    weather = get_weather(
                        location["latitude"],
                        location["longitude"]
                    )

                    st.session_state["weather_data"] = weather
                    st.session_state["location_data"] = location

        except requests.exceptions.RequestException as e:

            st.error(f"Unable to fetch weather data: {e}")

        except (KeyError, TypeError, ValueError) as e:

            st.error(f"Unable to process weather data: {e}")


# 5. Display weather information

if "weather_data" in st.session_state:

    weather = st.session_state["weather_data"]
    location = st.session_state["location_data"]

    current = weather["current"]
    daily = weather["daily"]

    st.divider()

    # Location information

    st.subheader(
        f'{location["name"]}, {location["country"]}'
    )

    # Current weather condition

    weather_code = current["weather_code"]

    description = get_weather_description(weather_code)

    icon = get_weather_icon(weather_code)

    col1, col2 = st.columns([1, 3])

    with col1:

        st.markdown(f"# {icon}")

        st.caption(description)

    with col2:

        st.metric(
            "Current Temperature",
            f'{current["temperature_2m"]} °C'
        )

    # Weather metrics

    st.subheader("Current Weather Details")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Feels Like",
        f'{current["apparent_temperature"]} °C'
    )

    col2.metric(
        "Humidity",
        f'{current["relative_humidity_2m"]}%'
    )

    col3.metric(
        "Wind Speed",
        f'{current["wind_speed_10m"]} km/h'
    )

    col4.metric(
        "Precipitation",
        f'{current["precipitation"]} mm'
    )

    st.caption(
        f'Wind direction: {current["wind_direction_10m"]}°'
    )

    # Sunrise and sunset

    st.subheader("Sunrise & Sunset")

    sunrise_col, sunset_col = st.columns(2)

    sunrise_col.metric(
        "Sunrise",
        daily["sunrise"][0].split("T")[1]
    )

    sunset_col.metric(
        "Sunset",
        daily["sunset"][0].split("T")[1]
    )

    # Seven-day forecast

    st.divider()

    st.subheader("7-Day Weather Forecast")

    forecast_data = pd.DataFrame({

        "Date": daily["time"],

        "Weather": [
            get_weather_description(code)
            for code in daily["weather_code"]
        ],

        "Maximum Temperature": daily["temperature_2m_max"],

        "Minimum Temperature": daily["temperature_2m_min"],

        "Rain Probability": daily["precipitation_probability_max"]

    })

    st.dataframe(
        forecast_data,
        use_container_width=True,
        hide_index=True
    )

    # Temperature visualization

    st.subheader("Temperature Forecast")

    chart_data = pd.DataFrame({

        "Date": daily["time"],

        "Maximum Temperature": daily["temperature_2m_max"],

        "Minimum Temperature": daily["temperature_2m_min"]

    })

    chart_data = chart_data.melt(
        id_vars="Date",
        var_name="Temperature Type",
        value_name="Temperature"
    )

    figure = px.line(
        chart_data,
        x="Date",
        y="Temperature",
        color="Temperature Type",
        markers=True,
        title="7-Day Temperature Trends"
    )

    figure.update_layout(
        xaxis_title="Date",
        yaxis_title="Temperature (°C)",
        hovermode="x unified"
    )

    st.plotly_chart(
        figure,
        use_container_width=True
    )

    st.caption(
        "Weather data provided by Open-Meteo."
    )
