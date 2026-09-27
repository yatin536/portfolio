# Yatin Kumar Singh - Senior Data Engineer Portfolio Website

A personal portfolio website and resume platform engineered for **Yatin Kumar Singh**, Senior Data Engineer, built using **Python**, **Flask**, **Jinja2**, and modern responsive web standards.

---

## 🌟 Key Highlights & Features

- **Data-Centric Developer Aesthetic**: Sleek obsidian and electric cyan dark mode with subtle particle grid, glowing ambient orbs, and glassmorphism cards.
- **Dynamic Typing Effect**: Cycles through core engineering identities (*Senior Data Engineer, AWS Athena & Glue ETL Specialist, AWS Kinesis Real-Time Streaming, Databricks & PySpark Architect, Snowflake & High-Performance SQL*).
- **Interactive Data Pipeline Anatomy Simulator**: Clickable 5-stage interactive flow (`Ingest (Kinesis/S3) -> Catalog & Validate (Glue/Python) -> Transform (Databricks/Glue/PySpark) -> Orchestrate (Airflow) -> Serve (Athena/Snowflake)`) that dynamically showcases modern data engineering patterns.
- **Impact Metrics Counter**: Showcases 3.5+ years experience, 50+ optimized SQL objects, 90% manual effort reduction via SCD I/II, 30% Databricks & PySpark speedup, and 95-99% reporting accuracy.
- **Experience Timeline**: Career milestones at **Accenture**, **Syven Global Services**, and **Acidaes Solutions** with company chips, tags, and quantified bullet points.
- **Featured Architectural Case Studies**: Real-Time AWS Kinesis Streaming Lakehouse, High-Performance Databricks & PySpark Engine (connecting Azure Storage & S3), Serverless AWS Glue ETL & Snowflake Warehouse, and SQL Optimization.
- **Categorized Technical Arsenal**: Interactive skill bars across AWS Big Data (Athena, Glue, Kinesis, S3), Databricks & PySpark, Snowflake Data Warehousing, SQL Tuning, and foundational Azure Storage Accounts.
- **Printable Resume View (`/resume`)**: Clean, standardized resume page matching your exact CV layout with one-click **"Print / Save as PDF"** support.
- **One-Click Clipboard**: Instant copy buttons for Email (`yatin536@gmail.com`) and Phone (`+91 9068630131`) with toast notifications.
- **Working Contact System**: Flask POST API `/api/contact` that logs messages to `inquiries.json` with seamless client fallback.
- **Dark / Light Theme Toggle**: Persistent mode preference saved in local storage.

---

## 🚀 How to Run (Multiple Options)

### Option 1: Live Flask Web Server (Recommended)
This runs the full dynamic application with all API endpoints and contact message logging:

```bash
# 1. Navigate to the portfolio folder
cd c:\Users\yatin\Desktop\Workspace1\portfolio

# 2. (Optional) Install requirements
pip install -r requirements.txt

# 3. Launch Flask
python app.py
```
Open your browser and navigate to: **`http://localhost:5000`**

---

### Option 2: Zero-Dependency Python Server (No `pip install` needed!)
Uses Python's built-in `http.server` standard library:

```bash
cd c:\Users\yatin\Desktop\Workspace1\portfolio
python server.py
```
Open your browser and navigate to: **`http://localhost:8000`**

---

### Option 3: Static Site Build (Deploy to GitHub Pages / Vercel / Netlify)
If you wish to host your portfolio on GitHub Pages or any static CDN for free:

```bash
cd c:\Users\yatin\Desktop\Workspace1\portfolio
python build_static.py
```
This renders the entire website into the **`dist/`** folder containing:
- `dist/index.html`
- `dist/resume.html`
- `dist/static/css/style.css`
- `dist/static/js/main.js`

You can drag and drop the `dist/` folder directly to **Netlify**, **Vercel**, or push to GitHub Pages!

---

## 📁 Project Structure

```
portfolio/
├── app.py                  # Flask web server & REST API
├── data.py                 # Central data source (all resume info, skills, projects)
├── build_static.py         # Static site compiler (renders templates into dist/)
├── server.py               # Pure Python built-in HTTP server runner
├── test_app.py             # Automated route verification test suite
├── requirements.txt        # Flask & Jinja2 dependencies
├── inquiries.json          # Stores incoming messages from the contact form
├── dist/                   # Compiled static website ready for free hosting
│   ├── index.html
│   ├── resume.html
│   └── static/
├── static/
│   ├── css/
│   │   └── style.css       # Custom styling, dark mode, animations & responsive design
│   └── js/
│       └── main.js         # Interactivity (typing, pipeline flow, filter, clipboard)
└── templates/
    ├── index.html          # Main portfolio Jinja2 template
    └── resume.html         # Printable PDF-ready resume template
```

---

## ✏️ How to Update Your Resume or Portfolio

All information (experience, job titles, metrics, skills, projects, contact info) is stored cleanly in a single Python file: **[`data.py`](file:///c:/Users/yatin/Desktop/Workspace1/portfolio/data.py)**.

To update anything:
1. Open `data.py`
2. Edit or add new entries to `PROFILE`, `EXPERIENCE`, `SKILLS`, or `PROJECTS`
3. Restart `python app.py` (or run `python build_static.py` if using static mode).
