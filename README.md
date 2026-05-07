# NASA Exoplanet Interactive Dashboard

> A Python-based interactive web application that fetches, processes, and visualizes live astronomical data.

### **[Live Demo](https://exoplanet-pipeline.streamlit.app/)**

---

## The Mission

Built to programmatically interface with the **NASA Exoplanet Archive API**, extracting JSON data on confirmed exoplanets and rendering a logarithmic distribution of planetary mass versus orbital periods.

## Tech Stack

* **Backend / API Framework:** Python, `requests`
* **Data Processing:** `pandas`
* **Interactive Visualization:** `plotly.express` *(with `matplotlib` utilized in standalone `exoplanet.py`)*
* **Web Deployment:** `streamlit`