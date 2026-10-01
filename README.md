# Yatin Kumar Singh — Senior Data Engineer Portfolio
> **"Engineering data systems that scale."**

The official personal engineering portfolio of **Yatin Kumar Singh**, Senior Data Engineer. Designed as a living, intelligent enterprise data infrastructure featuring real-time stream ingestion, lakehouse transformations, multi-warehouse compute isolation, and downstream AI integration.

**Live Deployment:** [https://yatin536.github.io/portfolio/](https://yatin536.github.io/portfolio/)  
**Printable Resume:** [https://yatin536.github.io/portfolio/resume.html](https://yatin536.github.io/portfolio/resume.html)

---

## 🌟 Key Architectural Features

- **Living 3D Data Infrastructure (Three.js WebGL):** Interactive spatial node network representing `Sources → AWS Kinesis → Amazon S3 Lake → Databricks & PySpark → Snowflake → Agentic AI`. Responds to cursor physics with spring damping.
- **System Boot Sequence:** Full-screen terminal boot loader counting `000%` &rarr; `100%` with live pipeline telemetry.
- **Adaptive Rem Grid (Lumora-Inspired):** Proportional viewport scaling across 4K, desktop, tablet, and mobile displays.
- **Interactive Data Pipeline ("From Event &rarr; Insight"):** 6-stage architecture walkthrough with isometric visual mesh and metric inspector.
- **Verified Career Graph:** Chronological systems engineering records across **Accenture** (Client: GE Vernova), **Syven Global Services** (Clients: Lazard Inc. & Student Housing), and **Acidaes Solutions**.
- **Selected Systems Case Studies:** 3D tilt cards with hover-reveal micro-diagrams (query execution plan tuning, real-time streaming, and SCD Type I/II MERGE).
- **Technical Deep-Dive ("Inside the System"):** Interactive tabbed modules with production-grade PySpark and SQL scripts.
- **Verified Metrics Panel:** Scroll-driven count-up statistics (25–30% latency reduction, 90% manual maintenance reduction, 100% reconciliation accuracy).
- **Printable Resume:** Dedicated `/resume.html` and clean `/resume` URL with one-click print styling.
- **Interactive Contact Modal:** Glassmorphism dialog with form validation, keyboard navigation (`Escape` closes), and simulated submission.

---

## 🚀 Running Locally

### Option 1: 1-Click Desktop Launcher
Double-click `run_portfolio.bat` in this folder or `Launch-Portfolio.bat` on your Desktop. It starts the local server and automatically launches `http://localhost:8080`.

### Option 2: Zero-Dependency Python Server
```bash
python server.py 8080
```
Open [http://localhost:8080](http://localhost:8080) in your browser.

### Option 3: Dynamic Flask Web Server
```bash
pip install -r requirements.txt
python app.py
```
Open [http://localhost:5000](http://localhost:5000) in your browser.

### Option 4: Direct Browser View
Double-click `index.html` to open directly in any modern browser without running a server.

---

## 📦 Building for Production

Compile the standalone distribution into `./dist/`:
```bash
python build_static.py
```
The `./dist/` directory is ready to deploy to GitHub Pages, AWS S3, Vercel, or Netlify.

---

## 🔄 CI/CD & Deployment

Every push to the `main` branch automatically triggers the GitHub Actions workflow (`.github/workflows/deploy.yml`), which compiles the static site and deploys it to **GitHub Pages**.

Full migration and architecture documentation is available in **[`docs/PORTFOLIO_MIGRATION.md`](file:///c:/Users/yatin/Desktop/Workspace1/portfolio/docs/PORTFOLIO_MIGRATION.md)**.

---

## 📄 License & Copyright
© 2026 Yatin Kumar Singh. All rights reserved.
