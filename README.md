# Exoplanet AI Analytics Dashboard

> An interactive astrophysical analytics pipeline that interfaces with the NASA Exoplanet Archive API to process structured astronomical datasets and generate dynamic scientific hypotheses using an LLM reasoning engine.

### **[Live Application](https://exoplanet-pipeline.streamlit.app/)**

---

## Architecture & Mission

Built to programmatically ingest, clean, and visualize structured JSON payloads from the **NASA Exoplanet Archive API**. The application processes confirmed exoplanetary data to construct interactive logarithmic distributions comparing planetary mass against orbital periods.

**LLM Reasoning Engine:** The dashboard integrates a dynamic reasoning agent via the OpenAI API. When a user isolates a specific exoplanet, the application programmatically extracts its unique telemetry (e.g., mass, orbital flux) and utilizes structured prompt engineering to generate context-aware scientific hypotheses regarding the planet's atmospheric composition and environmental habitability.

## Technical Stack

* **Data Ingestion & Backend Pipeline:** Python, `requests`, `pandas` (multi-indexing & data cleansing)
* **Logarithmic Visualization:** `plotly.express` *(with `matplotlib` implemented for standalone statistical analysis)*
* **Automated Reasoning Engine:** `openai` (OpenAI API with custom prompt construction)
* **Cloud Deployment:** `streamlit` (Distributed runtime)