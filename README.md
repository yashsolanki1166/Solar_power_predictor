A Solar_power_predictor
# ☀️ AI-Powered Solar Irradiance Prediction System

Demo Video coming soon here 


A brief Project Overview : 
A machine learning-powered web application that predicts solar irradiance levels using real-time weather data and Edge Impulse.
Development Process

Phase 1: Dataset Preparation
 Data Sources: 
- Historical solar irradiance data from [NASA POWER](https://power.larc.nasa.gov/)
- Weather data from OpenMeteo API
- 10,000+ data points across multiple geographic locations

Features Collected:
- Temperature (°C)
- Relative Humidity (%)
- Wind Speed (m/s) 
- Atmospheric Pressure (hPa)
- Cloud Cover (%)
- Hour of Day
- Geographic Coordinates

Data Preprocessing:
- Normalization and scaling
- Handling missing values
- Time-series feature engineering
- Train/validation/test split (70/15/15)

 Phase 2: Model Training with Edge Impulse
Impulse Design:
- Input: 4 weather parameters + time features
- Processing: Normalization and feature scaling
- Neural Network: Dense layers with dropout

Training Results:
- Model Accuracy: 94.2%
- Validation Loss: 0.023
- Inference Time: <50ms

Phase 3: Application Development
**Frontend Technologies:**
- HTML5, CSS3, JavaScript
- Chart.js for data visualization
- Responsive design principles

Backend Integration:
- OpenMeteo API for real-time weather data
- Edge Impulse WebAssembly for model inference
- Client-side processing (no server required)
