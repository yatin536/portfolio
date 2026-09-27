/**
 * Yatin Kumar Singh - Senior Data Engineer Portfolio
 * Interactive client-side controller
 */

document.addEventListener('DOMContentLoaded', () => {
  initTypingEffect();
  initPipelineSimulator();
  initProjectFiltering();
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
