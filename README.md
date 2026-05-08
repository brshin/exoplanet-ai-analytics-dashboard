# NASA Exoplanet AI Dashboard

> A Python-based interactive web application that fetches live astronomical data and utilizes an LLM reasoning engine to generate dynamic astrophysical insights.

### **[Live Demo](https://exoplanet-pipeline.streamlit.app/)**

---

## The Mission

Built to programmatically interface with the **NASA Exoplanet Archive API**, extracting JSON data on confirmed exoplanets and rendering a logarithmic distribution of planetary mass versus orbital periods.

**AI Integration:** The dashboard features a dynamic Large Language Model (LLM) integration. When a user queries a specific exoplanet, the application captures its unique orbital parameters and injects them into the OpenAI API, generating real-time, context-aware scientific hypotheses about the planet's potential climate and environment based on its telemetry.

## Tech Stack

* **Backend & Data Pipeline:** Python, `requests`, `pandas`
* **Interactive Visualization:** `plotly.express` *(with `matplotlib` utilized in standalone script)*
* **AI / Reasoning Engine:** `openai` (OpenAI API)
* **Web Deployment:** `streamlit`