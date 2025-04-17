# Rzecin Peatland Monitoring Platform

## Description

This project develops a cloud-based platform for real-time monitoring of the Rzecin peatland study area. The platform integrates data from various sensor types, providing a comprehensive view of the peatland's ecological status and dynamics.

## Peatland Area

Rzecin is a valuable peatland ecosystem, characterized by its unique hydrological regime and vegetation composition. Peatlands play a crucial role in carbon storage, water regulation, and biodiversity conservation. Monitoring the peatland is essential to understand its response to environmental changes and to ensure its long-term preservation.

## System Components

The platform consists of three main components:

1. **Edge Simulator**: Simulates sensor data collection from the peatland environment.

2. **Cloud Handler**: Processes and stores the incoming sensor data.

3. **Real-time Dashboard**: Visualizes the sensor data in real-time, providing insights into the peatland's environmental conditions.

## Sensors

The platform manages data from the following sensors:

* **Eddy Covariance System:** Measures the fluxes of carbon dioxide, water vapor, and energy between the peatland and the atmosphere.
* **Spectrometers:** Capture spectral reflectance data, which can be used to monitor vegetation health and species composition.
* **Pheno Cams:** Provide visual information about the phenological development of vegetation.
* **Other IoT Sensors:** These can include a range of sensors, such as soil moisture sensors, water level sensors, temperature sensors, and more, providing additional data on the peatland's biophysical state.

## Dashboard Features

The real-time dashboard provides visualization of key environmental parameters including:

* Air Temperature (°C)
* Wind Speed (m/s)
* CO₂ Flux (μmol/m²/s)
* H₂O Flux (mmol/m²/s)

The dashboard displays both current readings and historical data through interactive charts.

## Installation and Setup

1. Clone the repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To start the entire system, run:

```
python -m src.app.main
```

This will start:
- The data handler process
- The dashboard server
- The API server

Access the dashboard at: http://localhost:5001/
