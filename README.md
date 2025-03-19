# Sustainable Agriculture Decision Support System (DSS)

## 🌱 Overview

The **Sustainable Agriculture DSS** is a web-based **Decision Support System** that helps farmers make **data-driven agricultural decisions** by providing **real-time weather-based recommendations**. The system fetches **live weather data** from Open-Meteo API and generates **actionable insights** to help optimize irrigation and crop management, thereby maximizing crop yield while minimizing environmental impact.

## 🚀 Live Demo

[Access the deployed application here](https://sustainableagridss.streamlit.app/)

## 🎯 Features

- **Automatic Location Detection** 📍 – The system automatically detects the user's location and retrieves weather data accordingly.
- **Real-time Weather Data Retrieval** 📊 – Fetches **temperature, humidity, and rainfall** based on user-inputted location.
- **Automated Decision Support** 🤖 – Provides **irrigation and disease control recommendations** based on weather conditions.
- **User-Friendly Interface** 🖥️ – Built using **Streamlit**, making it **easy to use for non-technical users**.
- **Fast & Scalable** ⚡ – Processes data in real-time with **minimal latency**.
- **Secure & Efficient** 🔒 – Ensures **data privacy** and optimized API usage.

## 🛠️ Tech Stack

- **Frontend:** [Streamlit](https://streamlit.io/)
- **Backend:** Python (Flask for API integration)
- **Geolocation:** [`streamlit-geolocation`](https://pypi.org/project/streamlit-geolocation/)
- **Data Handling:** Pandas, Requests
- **Weather Data Source:** [Open-Meteo API](https://open-meteo.com/)
- **Deployment:** Streamlit Cloud

## 🏗️ Installation & Running Locally

To run the Sustainable Agriculture DSS locally, follow these steps:

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/d3vluqman/sustainable-agri-dss.git
cd sustainable-agri-dss
```

### 2️⃣ Install Dependencies

```sh
pip install streamlit requests pandas numpy
```

### 3️⃣ Run the Application

```sh
streamlit run app.py
```

### 4️⃣ Open in Browser

The app will launch automatically, or you can access it at:
```
http://localhost:8501/
```

## 📌 Usage

1. The system **automatically detects your location** (latitude & longitude) using GPS (you may need to grant location permissions).
2. Click **"Get Weather Data"** if the location isn't detected automatically.
3. View **real-time weather information**.
4. Get **automated recommendations** (e.g., irrigation advice, disease risk alerts).

## 🧑‍💻 System Architecture

The system follows a **modular architecture** consisting of:

- **User Interface (UI)** → Streamlit-based frontend.
- **Geolocation Module** → Retrieves the user's location automatically.
- **Weather Data Retrieval Module** → Fetches live data from Open-Meteo API.
- **Decision Support Engine** → Applies predefined rules to generate recommendations.
- **Recommendation Output Module** → Displays actionable insights for farmers.

## 🔬 Performance Evaluation

The system is continuously evaluated based on:

- **Accuracy** – Comparison with expert agricultural advice.
- **Response Time** – Ensuring recommendations are generated in **<2 seconds**.
- **User Satisfaction** – Feedback-driven UI/UX improvements.

## 🏆 Contributors

- **Abdulwasii Luqman**
- *Oluwatobiloba Famiwaye*

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-xyz`)
3. Commit changes (`git commit -m 'Added feature xyz'`)
4. Push to the branch (`git push origin feature-xyz`)
5. Submit a Pull Request

## 📜 License

## License

MIT
