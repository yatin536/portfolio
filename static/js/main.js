/**
 * Yatin Kumar Singh - Senior Data Engineer Portfolio
 * Interactive client-side controller
 */

document.addEventListener('DOMContentLoaded', () => {
  initTypingEffect();
  initPipelineSimulator();
  initProjectFiltering();
  initArchitectureExplorer();
  initClipboardButtons();
  initContactForm();
  initScrollNav();
  initThemeToggle();
  initMobileMenu();
});

/* --------------------------------------------------------------------------
   1. Dynamic Typing Effect
   -------------------------------------------------------------------------- */
function initTypingEffect() {
  const typedEl = document.getElementById('typed-text');
  if (!typedEl) return;

  const phrases = [
    "Senior Data Engineer",
    "GE Vernova • Agentic AI Cash Flow",
    "AWS Data Engg (Kinesis, S3, Athena, Glue)",
    "Databricks & PySpark Pipelines",
    "Lazard Inc. • Multi-Warehouse Ingestion",
    "SQL Optimization & Execution Plans",
    "Snowflake • Automated SCD I & II"
  ];

  let phraseIdx = 0;
  let charIdx = 0;
  let isDeleting = false;
  let typingSpeed = 100;

  function type() {
    const currentPhrase = phrases[phraseIdx];

    if (isDeleting) {
      typedEl.textContent = currentPhrase.substring(0, charIdx - 1);
      charIdx--;
      typingSpeed = 50;
    } else {
      typedEl.textContent = currentPhrase.substring(0, charIdx + 1);
      charIdx++;
      typingSpeed = 110;
    }

    if (!isDeleting && charIdx === currentPhrase.length) {
      typingSpeed = 1800; // Pause at end
      isDeleting = true;
    } else if (isDeleting && charIdx === 0) {
      isDeleting = false;
      phraseIdx = (phraseIdx + 1) % phrases.length;
      typingSpeed = 400; // Pause before new word
    }

    setTimeout(type, typingSpeed);
  }

  type();
}

/* --------------------------------------------------------------------------
   2. Interactive Data Pipeline Simulator
   -------------------------------------------------------------------------- */
function initPipelineSimulator() {
  const stepNodes = document.querySelectorAll('.pipeline-step-node');
  const detailTitle = document.getElementById('pipeline-stage-title');
  const detailDesc = document.getElementById('pipeline-stage-desc');
  const detailTech = document.getElementById('pipeline-stage-tech');
  const detailMetric = document.getElementById('pipeline-stage-metric');

  if (!stepNodes.length || !detailTitle) return;

  const stageData = [
    {
      title: "01. Real-Time & Multi-Source Ingestion",
      desc: "Capturing real-time financial and event streams via AWS Kinesis Data Streams and ingesting multi-source data feeds into Amazon S3 centralized data lakes.",
      tech: "AWS Kinesis, Amazon S3, Python Ingestion Scripts, REST APIs",
      metric: "Sub-second event ingestion & near-zero error rate"
    },
    {
      title: "02. Schema Catalog & Quality Gate",
      desc: "Automated schema inference using AWS Glue Data Catalog and Crawlers. Modular Python validation gates sanitize inputs, check boundaries, and enforce schema compliance.",
      tech: "AWS Glue Data Catalog, Python Data Validation, Schema Enforcement",
      metric: "+25% Improvement in Source Data Quality"
    },
    {
      title: "03. Distributed Databricks & PySpark",
      desc: "Executing high-performance PySpark transformations on Databricks clusters and AWS Glue ETL with custom partitioning, broadcast joins, and cloud storage mounts (Azure & S3).",
      tech: "Databricks, PySpark, AWS Glue ETL, Delta Lake, Azure Storage Mounts",
      metric: "+30% Faster transformation runtime & memory efficiency"
    },
    {
      title: "04. Multi-Warehouse Management & SCD Versioning",
      desc: "Dedicated Snowflake virtual warehouses isolating compute for distinct business teams (Lazard Inc.), combined with automated SCD Type I & II tracking via MERGE logic.",
      tech: "Snowflake Virtual Warehouses, Clustering Keys, MERGE Logic",
      metric: "90% Reduction in manual tracking effort & zero team contention"
    },
    {
      title: "05. SQL Execution Plans & Fast Dashboards",
      desc: "Refactored SQL Stored Procedures analyzed via execution plans (Student Housing), serverless Athena queries over S3, and Python SP output handlers delivering sub-second BI metrics.",
      tech: "AWS Athena, SQL Stored Procedures, Execution Plans, Python Handlers",
      metric: "25–30% Query latency reduction & sub-second dashboard refreshes"
    }
  ];

  function setActiveStage(index) {
    stepNodes.forEach((node, i) => {
      node.classList.toggle('active', i === index);
    });

    const data = stageData[index];
    if (data) {
      detailTitle.textContent = data.title;
      detailDesc.textContent = data.desc;
      detailTech.textContent = data.tech;
      detailMetric.textContent = data.metric;
    }
  }

  stepNodes.forEach((node, idx) => {
    node.addEventListener('click', () => {
      setActiveStage(idx);
    });
  });

  // Optional subtle auto-rotation if user hasn't clicked
  let currentStep = 0;
  let autoTimer = setInterval(() => {
    currentStep = (currentStep + 1) % stageData.length;
    setActiveStage(currentStep);
  }, 6000);

  // Stop auto rotation when user interacts
  stepNodes.forEach(node => {
    node.addEventListener('mouseenter', () => clearInterval(autoTimer));
    node.addEventListener('click', () => clearInterval(autoTimer));
  });
}

/* --------------------------------------------------------------------------
   3. Project Category Filtering
   -------------------------------------------------------------------------- */
function initProjectFiltering() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const projectCards = document.querySelectorAll('.project-card');

  if (!filterBtns.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      filterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.getAttribute('data-filter');

      projectCards.forEach(card => {
        const category = card.getAttribute('data-category');
        if (filter === 'all' || category === filter) {
          card.style.display = 'flex';
          card.style.animation = 'fadeIn 0.4s ease forwards';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/* --------------------------------------------------------------------------
   4. Clipboard Utility (Copy Email / Phone)
   -------------------------------------------------------------------------- */
function initClipboardButtons() {
  const copyButtons = document.querySelectorAll('.copy-trigger');

  copyButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const textToCopy = btn.getAttribute('data-copy');
      if (!textToCopy) return;

      navigator.clipboard.writeText(textToCopy).then(() => {
        showToast(`Copied to clipboard: ${textToCopy}`);
      }).catch(() => {
        // Fallback
        const textarea = document.createElement('textarea');
        textarea.value = textToCopy;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
        showToast(`Copied: ${textToCopy}`);
      });
    });
  });
}

function showToast(message) {
  let toast = document.getElementById('portfolio-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'portfolio-toast';
    toast.className = 'toast-msg';
    document.body.appendChild(toast);
  }

  toast.innerHTML = `
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#00e5ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M20 6L9 17l-5-5"></path>
    </svg>
    <span>${message}</span>
  `;

  toast.classList.add('show');
  setTimeout(() => {
    toast.classList.remove('show');
  }, 3200);
}

/* --------------------------------------------------------------------------
   5. Contact Form Handler
   -------------------------------------------------------------------------- */
function initContactForm() {
  const form = document.getElementById('portfolio-contact-form');
  const statusBox = document.getElementById('form-status');

  if (!form) return;

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = form.elements['name'].value.trim();
    const email = form.elements['email'].value.trim();
    const subject = form.elements['subject'].value.trim();
    const message = form.elements['message'].value.trim();
    const submitBtn = form.querySelector('button[type="submit"]');

    if (!name || !email || !message) {
      showStatus('Please fill in all required fields.', 'error');
      return;
    }

    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.textContent = 'Sending Message...';
    }

    try {
      // Try sending to Flask API
      const res = await fetch('/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, subject, message })
      });

      if (res.ok) {
        const data = await res.json();
        showStatus(data.message || 'Message sent successfully! Yatin will respond shortly.', 'success');
        form.reset();
      } else {
        throw new Error('API submission not available');
      }
    } catch (err) {
      // Fallback for static mode: open direct mailto link
      const mailtoUrl = `mailto:yatin536@gmail.com?subject=${encodeURIComponent(subject || 'Portfolio Inquiry')}&body=${encodeURIComponent(`Hi Yatin,\n\nName: ${name}\nEmail: ${email}\n\nMessage:\n${message}`)}`;
      showStatus('Redirecting to your email client to send your message directly to yatin536@gmail.com...', 'success');
      setTimeout(() => {
        window.location.href = mailtoUrl;
      }, 1000);
    } finally {
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.textContent = 'Send Message';
      }
    }
  });

  function showStatus(msg, type) {
    if (!statusBox) return;
    statusBox.textContent = msg;
    statusBox.className = `form-status ${type}`;
    statusBox.style.display = 'block';
  }
}

/* --------------------------------------------------------------------------
   6. Smooth Nav Active State on Scroll
   -------------------------------------------------------------------------- */
function initScrollNav() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  if (!sections.length || !navLinks.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navLinks.forEach(link => {
          link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
        });
      }
    });
  }, { threshold: 0.3 });

  sections.forEach(sec => observer.observe(sec));
}

/* --------------------------------------------------------------------------
   7. Theme Switcher (Dark / Light)
   -------------------------------------------------------------------------- */
function initThemeToggle() {
  const toggleBtn = document.getElementById('theme-toggle-btn');
  if (!toggleBtn) return;

  const savedTheme = localStorage.getItem('yatin_portfolio_theme') || 'dark';
  document.documentElement.setAttribute('data-theme', savedTheme);

  toggleBtn.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('yatin_portfolio_theme', newTheme);
  });
}

/* --------------------------------------------------------------------------
   8. Mobile Navigation Menu
   -------------------------------------------------------------------------- */
function initMobileMenu() {
  const menuBtn = document.getElementById('mobile-menu-btn');
  const navList = document.getElementById('nav-links');

  if (!menuBtn || !navList) return;

  menuBtn.addEventListener('click', () => {
    navList.classList.toggle('open');
  });

  // Close when link clicked
  navList.querySelectorAll('.nav-link').forEach(link => {
    link.addEventListener('click', () => {
      navList.classList.remove('open');
    });
  });
}

/* --------------------------------------------------------------------------
   9. Interactive Python & Flask Architecture Explorer
   -------------------------------------------------------------------------- */
function initArchitectureExplorer() {
  const stepNodes = document.querySelectorAll('.arch-step-node');
  const tabBtns = document.querySelectorAll('.arch-tab-btn');
  const stageTitle = document.getElementById('arch-stage-title');
  const stageBadge = document.getElementById('arch-stage-badge');
  const stageFile = document.getElementById('arch-stage-file');
  const stageDesc = document.getElementById('arch-stage-desc');
  const stageHighlights = document.getElementById('arch-stage-highlights');
  const codeDisplay = document.getElementById('arch-code-display');
  const copyBtn = document.getElementById('copy-arch-code');

  if (!stepNodes.length || !codeDisplay) return;

  const archStages = [
    {
      tab: "data.py",
      step: "STAGE 01",
      title: "Decoupled Python Data Model",
      badge: "Single Source of Truth",
      fileTag: "data.py",
      desc: "All portfolio content—including profile data, client projects (GE Vernova, Lazard Inc., Student Housing), technical skills, and metrics—is maintained in a centralized, typed Python dictionary schema (data.py). This strictly decouples content from UI markup, ensuring seamless synchronization between the interactive website and the printable resume without duplicate edits.",
      highlights: [
        "Pure Python data structures without database overhead",
        "Shared seamlessly by both the dynamic Flask server and the headless static builder",
        "Zero HTML duplication: change data once, updates both web portfolio and printable resume"
      ],
      code: `# data.py - Centralized Python Data Architecture
PROFILE = {
    "name": "Yatin Kumar Singh",
    "role": "Senior Data Engineer",
    "summary": "Specializing in AWS Data Engg, Databricks & Snowflake..."
}

EXPERIENCE = [
    {
        "company": "Accenture",
        "client": "GE Vernova",
        "role": "Sr. Data Engineer",
        "projects": [
            {"name": "Automating Cash Flow Application", "desc": "AWS Kinesis & S3 Lake"}
        ]
    },
    {
        "company": "Syven Global Services",
        "projects": [
            {"name": "Client Lazard Inc.", "desc": "Databricks & Snowflake Warehouses"},
            {"name": "Student Housing Dashboards", "desc": "SQL SP Tuning & Python Handlers"}
        ]
    }
]`
    },
    {
      tab: "app.py",
      step: "STAGE 02",
      title: "Flask Backend & Jinja2 Templating",
      badge: "Dynamic Web Engine",
      fileTag: "app.py",
      desc: "A lightweight Flask application serves the site during development. Jinja2 templates consume the Python data dictionary, dynamically rendering HTML layouts, responsive project cards, filterable categories, and a dedicated printable resume with semantic markup.",
      highlights: [
        "Flask microframework with modular routing and Jinja2 templating",
        "Clean template inheritance separating layout from page structure",
        "Built-in REST API endpoints (/api/profile, /api/contact) and test suite"
      ],
      code: `# app.py - Flask Web Server & Templating
from flask import Flask, render_template, jsonify
from data import PROFILE, SKILLS, EXPERIENCE, PROJECTS

app = Flask(__name__)

@app.route('/')
def index():
    # Pass Python data model directly into Jinja2 template
    return render_template('index.html',
                           profile=PROFILE, skills=SKILLS,
                           experience=EXPERIENCE, projects=PROJECTS,
                           is_static=False)

@app.route('/resume')
def resume_view():
    return render_template('resume.html', profile=PROFILE,
                           experience=EXPERIENCE, is_static=False)

@app.route('/api/profile')
def api_profile():
    return jsonify(PROFILE)`
    },
    {
      tab: "build_static.py",
      step: "STAGE 03",
      title: "Headless Static Site Generator",
      badge: "Zero-Cost Compilation",
      fileTag: "build_static.py",
      desc: "To deploy over the public internet with zero server hosting bills ($0/month), a custom Python compiler (build_static.py) initializes Jinja2 headlessly using FileSystemLoader, injects the Python data model, and pre-renders standalone production-ready index.html and resume.html files.",
      highlights: [
        "Headless Jinja2 Environment compiles dynamic templates to pure static HTML",
        "Builds in under 200 milliseconds without requiring Node.js or heavy bundlers",
        "Eliminates server execution runtime, security vulnerabilities, and database maintenance"
      ],
      code: `# build_static.py - Headless Jinja2 Site Compiler
from jinja2 import Environment, FileSystemLoader
from data import PROFILE, SKILLS, EXPERIENCE, PROJECTS

def build():
    # 1. Initialize headless Jinja2 environment
    env = Environment(loader=FileSystemLoader('templates'), autoescape=True)
    context = {
        "profile": PROFILE, "skills": SKILLS,
        "experience": EXPERIENCE, "projects": PROJECTS,
        "is_static": True
    }
    # 2. Pre-render templates into standalone static HTML
    for page in ['index.html', 'resume.html']:
        rendered = env.get_template(page).render(context)
        with open(page, 'w', encoding='utf-8') as f:
            f.write(rendered)
    print('[BUILD SUCCESS] Static portfolio pre-rendered!')

if __name__ == '__main__':
    build()`
    },
    {
      tab: "deploy.sh",
      step: "STAGE 04",
      title: "Git & GitHub Pages Edge Hosting",
      badge: "Serverless Global Delivery",
      fileTag: "deploy.sh",
      desc: "The pre-rendered HTML and optimized static assets (CSS, JS) are committed to GitHub and served globally via GitHub Pages. A worldwide edge CDN delivers the portfolio with sub-50ms load times, 100% uptime, and exactly $0 infrastructure cost.",
      highlights: [
        "Zero monthly hosting bills ($0.00/mo) with unlimited global bandwidth",
        "Sub-50ms Time To First Byte (TTFB) via GitHub Global Edge CDN",
        "Continuous deployment: automated publish on every git commit & push"
      ],
      code: `# deploy.sh - Automated Deploy Pipeline to GitHub Pages
# 1. Compile latest Python data into static HTML
python build_static.py

# 2. Stage pre-rendered static HTML and assets
git add index.html resume.html data.py static/

# 3. Commit and push to main branch
git commit -m "Deploy latest portfolio updates"
git push origin main

# Live Site: https://yatin536.github.io/portfolio/
# Cost: $0/month | Uptime: 99.99% | TTFB: <50ms`
    }
  ];

  let currentStageIndex = 0;

  function renderSyntaxHighlighted(rawCode) {
    const escaped = rawCode
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");

    return escaped
      .replace(/(#.*$)/gm, '<span class="c-com">$1</span>')
      .replace(/(&quot;[\s\S]*?&quot;)/g, '<span class="c-str">$1</span>')
      .replace(/('[\s\S]*?')/g, '<span class="c-str">$1</span>')
      .replace(/\b(from|import|def|return|class|if|else|elif|for|in|as|True|False|None)\b/g, '<span class="c-kw">$1</span>')
      .replace(/\b(print|open|render_template|jsonify|Environment|FileSystemLoader|build)\b(?=\()/g, '<span class="c-fn">$1</span>');
  }

  function setActiveStage(index) {
    currentStageIndex = index;
    const stage = archStages[index];
    if (!stage) return;

    stepNodes.forEach((node, i) => {
      node.classList.toggle('active', i === index);
    });

    tabBtns.forEach((btn, i) => {
      btn.classList.toggle('active', i === index);
    });

    if (stageTitle) stageTitle.textContent = stage.title;
    if (stageBadge) stageBadge.textContent = stage.badge;
    if (stageFile) stageFile.innerHTML = `<code>${stage.fileTag}</code>`;
    if (stageDesc) stageDesc.textContent = stage.desc;

    if (stageHighlights) {
      stageHighlights.innerHTML = stage.highlights.map(hl => `
        <li>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="2.5">
            <polyline points="20 6 9 17 4 12"></polyline>
          </svg>
          <span>${hl}</span>
        </li>
      `).join('');
    }

    if (codeDisplay) {
      codeDisplay.innerHTML = renderSyntaxHighlighted(stage.code);
    }

    if (copyBtn) {
      copyBtn.setAttribute('data-copy', stage.code);
    }
  }

  stepNodes.forEach((node, idx) => {
    node.addEventListener('click', () => setActiveStage(idx));
  });

  tabBtns.forEach((btn, idx) => {
    btn.addEventListener('click', () => setActiveStage(idx));
  });

  // Copy Code Button handler
  if (copyBtn) {
    copyBtn.addEventListener('click', (e) => {
      e.preventDefault();
      const code = copyBtn.getAttribute('data-copy') || archStages[currentStageIndex].code;
      navigator.clipboard.writeText(code).then(() => {
        showToast(`Copied ${archStages[currentStageIndex].fileTag} code to clipboard!`);
      }).catch(() => {
        const textarea = document.createElement('textarea');
        textarea.value = code;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
        showToast(`Copied ${archStages[currentStageIndex].fileTag} code to clipboard!`);
      });
    });
  }

  // Lifecycle Mode Switcher
  const modeBtns = document.querySelectorAll('.arch-mode-btn');
  const statCost = document.getElementById('mode-stat-cost');
  const statLatency = document.getElementById('mode-stat-latency');
  const statMaint = document.getElementById('mode-stat-maint');
  const flowText = document.getElementById('mode-flow-text');

  modeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      modeBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const mode = btn.getAttribute('data-mode');

      if (mode === 'dynamic') {
        if (statCost) {
          statCost.textContent = '$10 - $20 / month';
          statCost.className = 'val text-amber';
        }
        if (statLatency) {
          statLatency.textContent = '~120ms - 250ms (Server Round-Trip)';
          statLatency.className = 'val text-cyan';
        }
        if (statMaint) {
          statMaint.textContent = 'Linux / Nginx / WSGI Config';
          statMaint.className = 'val text-muted';
        }
        if (flowText) {
          flowText.innerHTML = '<code>Browser HTTP Request ➔ Nginx Reverse Proxy ➔ Gunicorn WSGI ➔ Flask app.py ➔ Jinja2 ➔ Dynamic Response</code>';
        }
      } else {
        if (statCost) {
          statCost.textContent = '$0.00 / month';
          statCost.className = 'val text-success';
        }
        if (statLatency) {
          statLatency.textContent = '< 35ms (Global CDN)';
          statLatency.className = 'val text-cyan';
        }
        if (statMaint) {
          statMaint.textContent = 'Zero Maintenance';
          statMaint.className = 'val text-muted';
        }
        if (flowText) {
          flowText.innerHTML = '<code>Python data.py ➔ Headless Jinja2 Compile ➔ Standalone HTML ➔ GitHub Pages Edge CDN</code>';
        }
      }
    });
  });

  // Initial stage render
  setActiveStage(0);
}
