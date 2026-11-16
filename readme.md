# Weatherly – Live Weather Dashboard

A Python-based live weather dashboard built with **Streamlit** and the **Open-Meteo API**. Search for any city to explore current weather conditions, essential weather metrics, and a 7-day forecast through an interactive interface.

## Features

- **City Search:** Find weather information by entering a city name.
- **Current Weather:** View real-time temperature and weather conditions.
- **Feels-Like Temperature:** Check how the temperature actually feels.
- **Weather Metrics:** View humidity and wind speed.
- **Sunrise & Sunset:** Get daily sunrise and sunset timings.
- **7-Day Forecast:** Explore upcoming daily weather conditions.
- **Interactive Visualization:** Analyze temperature trends through interactive charts.
- **Error Handling:** Handles unsuccessful API requests and invalid city searches.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Open-Meteo API | Weather data |
| Requests | API communication |
| Pandas | Data handling |
| Plotly | Interactive visualizations |

## Project Structure

```text
weatherly/
├── app.py
├── weather.py
├── requirements.txt
├── readme.md
├── .gitignore
└── LICENSE
```

## Getting Started

Follow these instructions to run Weatherly locally.

### 1. Clone the repository

```bash
git clone https://github.com/bruce-01/weatherly.git
```

### 2. Navigate to the project directory

```bash
cd weatherly
```

### 3. Create a virtual environment

```bash
python3 -m venv venv
```

### 4. Activate the virtual environment

**macOS / Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your default browser.

## API Documentation

Weatherly uses the free Open-Meteo APIs:

- [Open-Meteo Weather API](https://open-meteo.com/en/docs)
- [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api)

## Author

**Sumit Bhandari**

[GitHub](https://github.com/bruce-01)

---

If you find this project useful, consider giving the repository a ⭐.