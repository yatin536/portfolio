# Portfolio Migration & Deployment Guide
**Author:** Yatin Kumar Singh — Senior Data Engineer  
**Date:** October 2026  
**Repository:** [github.com/yatin536/portfolio](https://github.com/yatin536/portfolio)  
**Production Live URL:** [https://yatin536.github.io/portfolio/](https://yatin536.github.io/portfolio/)

---

## 1. Project Overview
This repository hosts the official personal engineering portfolio of **Yatin Kumar Singh**, Senior Data Engineer. The portfolio showcases verified enterprise data engineering achievements across cloud platforms (**AWS**, **Databricks**, **Snowflake**, **Azure**), distributed computing (**PySpark**, **Spark SQL**), real-time streaming (**AWS Kinesis**), and relational database optimization (**SQL Server**, **Stored Procedures**, **Query Execution Plans**).

The site has been transformed from a standard personal profile into an interactive, high-performance creative engineering experience: **"A Data Engineer's Digital Infrastructure."** It visually and mechanically represents an enterprise data system in motion, utilizing Three.js WebGL spatial networks, Lenis smooth scrolling, adaptive rem typography, and verified real-world telemetry.

---

## 2. Migration Objective
The objective of this controlled migration is:
```text
OLD PORTFOLIO (Legacy HTML/CSS/JS)
         │
         ▼
REPOSITORY CLEANUP (Removal of obsolete assets & styles)
         │
         ▼
NEW PORTFOLIO (Living Data Infrastructure with 3D WebGL Engine)
         │
         ▼
LOCAL BUILD & TEST VERIFICATION (Zero errors, 100% test pass)
         │
         ▼
GITHUB COMMIT & PUSH (Clean Git history on main branch)
         │
         ▼
GITHUB ACTIONS CI/CD (deploy.yml automated runner)
         │
         ▼
GITHUB PAGES PRODUCTION DEPLOYMENT (Live at yatin536.github.io/portfolio)
```

The migration replaces obsolete assets without breaking the established deployment pipeline or creating competing repositories.

---

## 3. Previous Architecture
The previous portfolio consisted of:
- A basic dark/light theme website with manual styling in `static/css/style.css`.
- Conventional DOM manipulation and typing text script in `static/js/main.js`.
- Generic ambient CSS orbs and SVG icons.
- Build engine: Python `build_static.py` rendering with Jinja2 into `./dist`.
- Deployment: GitHub Actions `.github/workflows/deploy.yml` pushing `./dist` to GitHub Pages.

---

## 4. New Architecture
The new portfolio is engineered as a zero-dependency, server-safe, ultra-high-performance living data system:
- **Design Metaphor:** An intelligent, living enterprise data platform (stream ingestion &rarr; S3 lakehouse &rarr; distributed PySpark compute &rarr; multi-warehouse Snowflake isolation &rarr; downstream agentic AI inference).
- **Core Visual Reference:** The Lumora design specification adapted for data engineering.
- **Adaptive Grid:** Rem-based viewport scaling:
  - `@media (max-width: 1920px) { html { font-size: 0.833333vw; } }`
  - `@media (max-width: 1440px) { html { font-size: 1.111111vw; } }`
  - `@media (max-width: 1024px) { html { font-size: 1.5625vw; } }`
  - `@media (max-width: 640px)  { html { font-size: 4.444444vw; } }`
  - Dynamic JavaScript interpolation for displays wider than 1920px (`coef = 0.6666`).
- **Typography:** Display typography in `Plus Jakarta Sans` paired with technical metadata, metrics, and code blocks in `JetBrains Mono`.
- **Palette:** Near-black (`#08090B`), graphite (`#111318`), surface (`#161922`), borders (`#2A2D33`), soft white (`#F5F5F2`), with electric data cyan/teal accents (`#36D6C4`, `#20B9AA`, `#82F3E5`).
- **3D WebGL Engine:** Three.js spatial node topology with icosahedron wireframes, illuminated cores, curved Catmull-Rom tube conduits, and floating particle fields responding to cursor coordinates with critically damped spring physics.
- **Smooth Scroll:** Native rAF integration with Lenis smooth scrolling (`smoothWheel: true`).
- **Static Output:** Standalone distribution in `./dist`, deployable to any static host without build steps or server runtime requirements.

---

## 5. Repository Structure
```text
portfolio/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions automated Pages deployment
├── docs/
│   └── PORTFOLIO_MIGRATION.md  # Comprehensive migration & architectural documentation
├── dist/                       # Production build output artifact
│   ├── index.html              # Main compiled portfolio
│   ├── resume.html             # Printable resume sheet
│   ├── 404.html                # Clean fallback for GitHub Pages
│   ├── resume/
│   │   └── index.html          # Clean URL support (/resume)
│   └── static/
│       └── images/             # Optimized visual assets
│           ├── hero_datacenter.jpg
│           ├── pipeline_mesh.jpg
│           └── og_cover.jpg
├── static/
│   └── images/                 # Source visual assets
│       ├── hero_datacenter.jpg
│       ├── pipeline_mesh.jpg
│       └── og_cover.jpg
├── templates/
│   ├── index.html              # Jinja2 template source for Flask / static builder
│   └── resume.html             # Jinja2 template source for resume
├── app.py                      # Optional local Flask server & REST API
├── build_static.py             # Headless static site compiler
├── data.py                     # Single source of truth for resume data
├── index.html                  # Standalone local portfolio file
├── resume.html                 # Standalone printable resume
├── run_portfolio.bat           # Portable 1-click desktop runner
├── server.py                   # Zero-dependency Python HTTP server
├── test_app.py                 # Automated route & API test suite
├── requirements.txt            # Flask & Jinja2 dependencies
└── README.md                   # Repository overview & setup instructions
```

---

## 6. Migration Steps Executed
1. **Repository Discovery:** Inspected remote origin (`https://github.com/yatin536/portfolio.git`), active branch (`main`), and existing deployment configuration.
2. **Safety Checkpoint:** Created a full backup of all project assets outside the Git working tree.
3. **Legacy File Removal:** Deleted obsolete `static/css/style.css` and `static/js/main.js` from the repository.
4. **New Portfolio Integration:** Embedded the complete Lumora-inspired Data Infrastructure interface into `index.html` and `templates/index.html`.
5. **Asset Optimization:** Added high-resolution infrastructure visuals (`hero_datacenter.jpg`, `pipeline_mesh.jpg`, `og_cover.jpg`) to `static/images/`.
6. **Static Compiler Enhancement:** Updated `build_static.py` to generate `./dist/index.html`, `./dist/resume.html`, `./dist/resume/index.html`, `./dist/404.html`, and copy static images.
7. **Local Test Execution:** Executed `test_app.py` (100% pass) and served the build locally to verify all assets and 3D scenes.
8. **Staged Commits:** Created clear, granular Git commits separating cleanup from feature additions and documentation.
9. **Push to Remote:** Pushed the `main` branch to GitHub.
10. **CI/CD Execution & Verification:** Monitored the GitHub Actions workflow and validated the live deployment at `https://yatin536.github.io/portfolio/`.

---

## 7. Relevant Git Commands
```bash
# Check repository and remote status
git status
git remote -v

# Remove obsolete legacy files
git rm static/css/style.css static/js/main.js

# Stage new portfolio files
git add index.html templates/index.html build_static.py static/images/ run_portfolio.bat

# Commit changes
git commit -m "feat: migrate to new data infrastructure portfolio with 3D engine"

# Add documentation
git add docs/ README.md
git commit -m "docs: document portfolio migration and deployment"

# Push to production
git push origin main
```

---

## 8. Build Instructions
To build the static distribution locally:
```bash
# 1. Install build dependencies (Jinja2)
pip install -r requirements.txt

# 2. Run static compiler
python build_static.py
```
Output directory: `./dist/` containing `index.html`, `resume.html`, `404.html`, and `static/images/`.

To test locally:
```bash
# Zero-dependency Python server
python server.py 8080
```
Then visit `http://localhost:8080`.

---

## 9. GitHub Pages Deployment
- **Hosting Provider:** GitHub Pages
- **Source Mode:** GitHub Actions (`actions/deploy-pages@v4`)
- **Branch:** `main`
- **Artifact Path:** `./dist`
- **URL:** [https://yatin536.github.io/portfolio/](https://yatin536.github.io/portfolio/)

---

## 10. GitHub Actions Workflow Configuration
Located at `.github/workflows/deploy.yml`:
```yaml
name: Deploy Portfolio to GitHub Pages

on:
  push:
    branches:
      - main
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build-and-deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          pip install jinja2

      - name: Build Static Site
        run: |
          python build_static.py

      - name: Upload GitHub Pages Artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: './dist'

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

---

## 11. Environment Variables
- **Public Variables:** None required. The site compiles into completely self-contained static assets.
- **Secrets:** None required. All data is grounded in public resume credentials.
- **Security:** Zero private API keys, database credentials, or secret tokens are present in the repository.

---

## 12. 3D & WebGL Architecture
- **Library:** Three.js (imported via ESM).
- **Scene Objects:**
  - 6 Architecture Nodes (`SOURCES`, `KINESIS`, `S3_LAKE`, `DATABRICKS`, `SNOWFLAKE`, `AGENTIC_AI`) configured as wireframe icosahedrons with internal solid cores.
  - Catmull-Rom 3D spline tube representing data conduits connecting nodes.
  - 220 floating ambient data particles drifting along the vector field.
- **Camera Movement:** Responsive perspective camera with spring interpolation (`delta * 0.05`) following cursor coordinates.
- **Performance Strategy:** Low-polygon geometry, minimal draw calls, shared materials, and transparent alpha clearing to ensure a consistent 60fps frame rate.
- **Graceful Fallback:** In environments where WebGL is unsupported or blocked, the background CSS layering and interactive DOM elements ensure complete content readability.

---

## 13. Animation Architecture
- **Boot Sequence:** 1,400ms `easeInOutCubic` progress loader with live status messages and spring exit transition (`translateY(0%)` &rarr; `translateY(-100%)`).
- **Smooth Scrolling:** Managed by Lenis with custom wheel damping and programmatic anchor navigation.
- **Line & Word Reveals:** Headings utilize CSS overflow clips (`translateY(100%)` &rarr; `translateY(0%)`), while the About statement uses staggered word spans with 35ms offsets.
- **Metrics Counter:** IntersectionObserver-driven count-up logic calculating `easeOut` progression on scroll.
- **Reduced Motion:** Fully honors `@media (prefers-reduced-motion: reduce)` by disabling transforms and transitions.

---

## 14. Media Asset Inventory
| Asset | Role | Path | Loading |
|---|---|---|---|
| `hero_datacenter.jpg` | Hero cinematic infrastructure backdrop | `static/images/hero_datacenter.jpg` | Background cover, luminosity blend |
| `pipeline_mesh.jpg` | Interactive pipeline visual banner | `static/images/pipeline_mesh.jpg` | Native `<img>`, lazy-compatible |
| `og_cover.jpg` | Open Graph & Twitter social card | `static/images/og_cover.jpg` | Static meta link |

---

## 15. Performance & Optimization
- **Zero Heavy Bundles:** Runs directly with standard web standards and CDN module imports; zero multi-megabyte JavaScript bundles.
- **GPU Acceleration:** Transforms and opacity used exclusively for all continuous animations.
- **Adaptive Memory Management:** No state leaks or unthrottled event listeners; scroll events run in passive mode.

---

## 16. SEO & Metadata
- **Title:** `Yatin Kumar Singh — Senior Data Engineer`
- **Meta Description:** Focuses on cloud data platforms, real-time streaming (AWS Kinesis), distributed lakehouse processing (Databricks, PySpark), Snowflake multi-warehouse management, and SQL optimization.
- **Social Metadata:** Complete Open Graph (`og:title`, `og:description`, `og:image`, `og:url`) and Twitter Cards.
- **Semantic Structure:** Semantic HTML5 elements (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`).

---

## 17. Verification Checklist
- [x] Local build succeeds without errors (`python build_static.py`)
- [x] Automated test suite passes (`python test_app.py`)
- [x] Obsolete legacy portfolio assets removed (`static/css/`, `static/js/`)
- [x] New portfolio and images active in repository
- [x] Zero private secrets or API keys committed
- [x] Git commits structured and pushed to `main`
- [x] GitHub Actions workflow runs and deploys artifact
- [x] GitHub Pages serves new website at `https://yatin536.github.io/portfolio/`
- [x] Interactive 3D scene renders cleanly
- [x] Responsive layout verified across desktop, tablet, and mobile
- [x] Direct resume access verified at `/resume.html` and `/resume`
- [x] Live IST clock ticks accurately
- [x] Contact modal opens, validates, and simulates submission

---

## 18. Rollback Procedure
If an emergency rollback is ever required:
1. Locate the commit before the migration:
   ```bash
   git log --oneline -5
   ```
2. Revert the migration commits:
   ```bash
   git revert <commit-sha>
   ```
3. Push to `main`:
   ```bash
   git push origin main
   ```
GitHub Actions will automatically rebuild and redeploy the previous artifact. *Do not force-push or delete Git history.*

---

## 19. Future Maintenance
- **Updating Resume Content:** Modify `data.py` directly; changes automatically propagate to both `index.html` and `resume.html`.
- **Adding Projects:** Add project objects to the `PROJECTS` list in `data.py` and the corresponding card in `templates/index.html`.
- **Rebuilding & Deploying:** Simply commit changes to `main` and push; GitHub Actions will compile and publish the update within 60 seconds.
