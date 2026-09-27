# 🚀 Deployment Guide: Yatin Kumar Singh's Portfolio
### Minimum Cost, Maximum Performance & Deployment Strategies

This guide breaks down the best, fastest, and least expensive ways to deploy your portfolio website over the internet, including a comparison between **Static CDN Hosting**, **AWS Serverless**, and **Docker Containerization**.

---

## 🏆 The Verdict: Which is the Best & Least Expensive?

| Method | Monthly Cost | Speed & Uptime | Cold Starts? | Maintenance | Best For |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. GitHub Pages** *(Recommended)* | **$0.00 / mo** (Free Forever) | ⚡ Sub-50ms Global CDN | ❌ None (Instant) | Zero | **#1 Best & Easiest** |
| **2. Vercel / Netlify** | **$0.00 / mo** (Free Tier) | ⚡ Sub-50ms Global CDN | ❌ None (Instant) | Zero | Fast Drag-and-Drop |
| **3. AWS S3 + CloudFront** | **~$0.10 - $0.50 / mo** | ⚡ Enterprise AWS CDN | ❌ None (Instant) | Low | **The AWS Data Engineer Flex** |
| **4. Docker Container (Render.com)** | **$0.00 / mo** (Free Tier) | 🐢 Good after wakeup | ⚠️ 30-50s sleep delay | Moderate | If you want live Python backend |
| **5. AWS App Runner / ECS** | **~$5 - $15 / mo** | ⚡ Always On | ❌ None | Moderate | Dedicated container instances |

---

## 💡 Should You Containerize (Docker)?

### The Honest Truth:
- **For a Portfolio Website**: Containerization is **overkill and unnecessarily expensive** if you keep a VM or container running 24/7 on AWS/GCP ($5–$20/mo). Free container platforms (like Render.com free tier) put the container to sleep after 15 minutes of inactivity, meaning a recruiter might wait **30 to 50 seconds** for the container to wake up.
- **Why we still created the Dockerfile**: Having a production-grade `Dockerfile` in your GitHub repository proves to recruiters and engineering managers that you know how to build secure, non-root, production-ready containers.
- **The Ideal Strategy**:
  1. **Deploy the live website for $0 on GitHub Pages or Vercel** (instant loading, zero cold starts, 100% free forever).
  2. **Keep the `Dockerfile` and `docker-compose.yml` in your public GitHub repository** so visitors and recruiters can see your containerization skills.

---

## 🛠️ Step-by-Step Deployment Options

---

### Option 1: GitHub Pages (Recommended: $0.00 Forever, Automated CI/CD)

We have already configured a complete GitHub Actions workflow for you in [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml).

#### Steps:
1. **Initialize Git & Push to GitHub**:
   Open PowerShell in your portfolio folder:
   ```powershell
   cd c:\Users\yatin\Desktop\Workspace1\portfolio
   git init
   git add .
   git commit -m "Initial commit of Data Engineer portfolio"
   ```
2. **Create a Repository on GitHub**:
   - Go to [github.com/new](https://github.com/new).
   - Name it `portfolio` (or `<your-username>.github.io` for a root domain).
   - Keep it Public.
3. **Push your code**:
   ```powershell
   git remote add origin https://github.com/<your-username>/portfolio.git
   git branch -M main
   git push -u origin main
   ```
4. **Enable GitHub Pages**:
   - In your GitHub repository, click **Settings** → **Pages** (in the left sidebar).
   - Under **Build and deployment** → **Source**, select **GitHub Actions**.
5. **Done!**
   GitHub will run `python build_static.py` automatically and publish your site at:
   `https://<your-username>.github.io/portfolio/`

---

### Option 2: Vercel / Netlify (100% Free, Drag-and-Drop in 60 Seconds)

If you don't even want to touch Git right now:

1. Run the static site builder locally:
   ```powershell
   cd c:\Users\yatin\Desktop\Workspace1\portfolio
   python build_static.py
   ```
   This generates the complete website in the `dist/` folder.
2. Go to [app.netlify.com/drop](https://app.netlify.com/drop) or [vercel.com](https://vercel.com).
3. Drag and drop the `dist/` folder into the browser window.
4. Your website is instantly live with a free SSL certificate!

---

### Option 3: AWS S3 + CloudFront (The "AWS Data Engineer" Showcase)

As an AWS Data Engineer, hosting your portfolio on AWS S3 and CloudFront is a great conversation starter in interviews.

**Monthly Cost**: Less than $0.50 (Pennies for S3 storage + CloudFront free tier 1TB transfer).

#### Steps:
1. **Build the static site**:
   ```powershell
   python build_static.py
   ```
2. **Create an S3 Bucket**:
   - Bucket name: e.g. `yatin-singh-portfolio`
   - Enable "Static website hosting" with Index document: `index.html`.
3. **Upload the contents of `dist/` to the S3 bucket**:
   ```bash
   aws s3 sync dist/ s3://yatin-singh-portfolio/ --delete
   ```
4. **Set up AWS CloudFront (CDN)**:
   - Create a CloudFront Distribution pointing to the S3 website endpoint.
   - Enables global edge caching and free HTTPS via AWS Certificate Manager (ACM).

---

### Option 4: Deploying with Docker (Containerization)

If you want to run the full Flask dynamic app inside a Docker container:

#### 1. Test Locally with Docker:
Make sure Docker Desktop is running:
```powershell
cd c:\Users\yatin\Desktop\Workspace1\portfolio

# Build the Docker image
docker build -t yatin-portfolio .

# Run the container
docker run -d -p 5000:5000 --name yatin_site yatin-portfolio
```
Visit `http://localhost:5000` to see your containerized app running with Gunicorn.

Or using Docker Compose:
```powershell
docker-compose up -d
```

#### 2. Deploy Docker Container to Render.com (Free Tier):
1. Push your repository (with `Dockerfile`) to GitHub.
2. Sign up at [Render.com](https://render.com).
3. Click **New +** → **Web Service**.
4. Connect your GitHub repository.
5. Select **Docker** as the Environment.
6. Choose the **Free** instance type.
7. Click **Create Web Service**. Render builds your Dockerfile and deploys it live.

---

## 📬 What About the Contact Form on Free Static Hosting?

When hosting statically on GitHub Pages or Vercel, there is no Python backend running 24/7 to process POST requests.

You have two solutions:
1. **Direct Mailto (Already Built-In)**: If someone clicks "Send Message", `main.js` automatically creates an email draft addressed directly to `yatin536@gmail.com`.
2. **Free Form Backend (Formspree or Web3Forms - 2 min setup)**:
   - Sign up for free at [Web3Forms.com](https://web3forms.com) (no credit card needed).
   - Get your free access key.
   - In `templates/index.html`, add `<input type="hidden" name="access_key" value="YOUR_KEY">` and point the form action to `https://api.web3forms.com/submit`.
   - Every time a recruiter submits the form, you receive an instant email in your inbox!

---

## 🎯 Summary Recommendation

1. **Host Live on GitHub Pages ($0.00 / month)**: Fastest, never goes to sleep, 100% free forever.
2. **Keep the `Dockerfile` in the repo**: Shows hiring managers that you have production containerization and DevSecOps fundamentals.
