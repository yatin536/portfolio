"""
Script to generate a comprehensive, interview-focused Project Guide PDF
for Yatin Kumar Singh, covering end-to-end architectures, problems faced,
technical resolutions, and STAR interview scripts across all organizations.
"""

import os
import subprocess

OUTPUT_HTML = r"c:\Users\yatin\Desktop\Workspace1\Yatin_Kumar_Singh_Projects_Interview_Guide.html"
OUTPUT_PDF = r"c:\Users\yatin\Desktop\Workspace1\Yatin_Kumar_Singh_Projects_Interview_Guide.pdf"
EDGE_EXE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Yatin Kumar Singh - Senior Data Engineer Project Deep-Dive & Interview Handbook</title>
  <style>
    @page {
      size: A4;
      margin: 18mm 15mm;
    }
    
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      color: #1e293b;
      line-height: 1.55;
      font-size: 9.8pt;
      background: #ffffff;
    }

    /* Cover / Header Section */
    .doc-header {
      border-bottom: 3px solid #0284c7;
      padding-bottom: 14px;
      margin-bottom: 22px;
    }

    .doc-title-row {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
    }

    .candidate-name {
      font-size: 22pt;
      font-weight: 800;
      color: #0f172a;
      letter-spacing: -0.02em;
    }

    .doc-subtitle {
      font-size: 11pt;
      font-weight: 600;
      color: #0284c7;
      margin-top: 2px;
    }

    .contact-info {
      text-align: right;
      font-size: 8.8pt;
      color: #475569;
      line-height: 1.45;
    }

    .contact-info a {
      color: #0284c7;
      text-decoration: none;
    }

    .exec-summary-box {
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-left: 4px solid #0284c7;
      padding: 12px 14px;
      border-radius: 4px;
      margin-bottom: 22px;
      font-size: 9.2pt;
    }

    .exec-summary-box strong {
      color: #0f172a;
    }

    /* Section & Project Headers */
    .page-break {
      page-break-before: always;
    }

    /* Callout Boxes */
    .callout {
      border-radius: 5px;
      padding: 10px 14px;
      margin: 10px 0;
      font-size: 9.1pt;
      line-height: 1.5;
      page-break-inside: avoid;
      break-inside: avoid;
    }

    .arch-flow-box {
      background: #0f172a;
      color: #f8fafc;
      padding: 10px 14px;
      border-radius: 6px;
      font-family: "JetBrains Mono", Consolas, Monaco, monospace;
      font-size: 8.2pt;
      line-height: 1.5;
      margin: 8px 0 12px;
      white-space: pre-wrap;
      page-break-inside: avoid;
      break-inside: avoid;
    }

    .company-banner {
      background: #0f172a;
      color: #ffffff;
      padding: 9px 14px;
      border-radius: 4px;
      margin-top: 14px;
      margin-bottom: 12px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      page-break-after: avoid;
      break-after: avoid;
    }

    .company-banner h2 {
      font-size: 12.5pt;
      font-weight: 700;
      letter-spacing: -0.01em;
    }

    .company-banner .tenure {
      font-size: 8.8pt;
      font-weight: 500;
      color: #94a3b8;
    }

    .project-card {
      margin-bottom: 20px;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 16px;
      background: #ffffff;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
      page-break-inside: auto;
    }

    .project-title {
      font-size: 11.5pt;
      font-weight: 700;
      color: #0f172a;
      display: flex;
      justify-content: space-between;
      align-items: baseline;
      border-bottom: 1.5px solid #e2e8f0;
      padding-bottom: 6px;
      margin-bottom: 10px;
    }

    .project-tag {
      font-size: 8.5pt;
      font-weight: 600;
      background: #e0f2fe;
      color: #0369a1;
      padding: 3px 8px;
      border-radius: 12px;
    }

    .section-h3 {
      font-size: 9.8pt;
      font-weight: 700;
      color: #1e293b;
      margin-top: 12px;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .tech-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin: 8px 0 12px;
    }

    .tech-pill {
      font-size: 8pt;
      font-weight: 600;
      background: #f1f5f9;
      color: #334155;
      border: 1px solid #cbd5e1;
      padding: 2px 7px;
      border-radius: 4px;
    }

    table.matrix-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 8.6pt;
      margin: 14px 0;
      page-break-inside: avoid;
      break-inside: avoid;
    }

    .callout-challenge {
      background: #fff1f2;
      border-left: 4px solid #e11d48;
      color: #881337;
    }

    .callout-challenge strong {
      color: #9f1239;
    }

    .callout-solution {
      background: #f0fdf4;
      border-left: 4px solid #16a34a;
      color: #14532d;
    }

    .callout-solution strong {
      color: #15803d;
    }

    .callout-script {
      background: #faf5ff;
      border: 1px solid #e9d5ff;
      border-left: 4px solid #9333ea;
      color: #581c87;
    }

    .callout-script strong {
      color: #7e22ce;
    }

    .callout-qa {
      background: #fffbeb;
      border-left: 4px solid #f59e0b;
      color: #78350f;
    }

    .bullets {
      padding-left: 18px;
      margin: 6px 0;
    }

    .bullets li {
      margin-bottom: 4px;
      color: #334155;
    }

    .bullets strong {
      color: #0f172a;
    }

    /* Matrix Table */
    table.matrix-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 8.6pt;
      margin: 14px 0;
    }

    table.matrix-table th, table.matrix-table td {
      border: 1px solid #cbd5e1;
      padding: 7px 10px;
      text-align: left;
    }

    table.matrix-table th {
      background: #f1f5f9;
      color: #0f172a;
      font-weight: 700;
    }

    table.matrix-table tr:nth-child(even) {
      background: #f8fafc;
    }

    .footer-note {
      font-size: 8pt;
      color: #64748b;
      text-align: center;
      margin-top: 24px;
      border-top: 1px solid #e2e8f0;
      padding-top: 8px;
    }
  </style>
</head>
<body>

  <!-- DOCUMENT HEADER -->
  <div class="doc-header">
    <div class="doc-title-row">
      <div>
        <h1 class="candidate-name">Yatin Kumar Singh</h1>
        <div class="doc-subtitle">Senior Data Engineer • Project Deep-Dive &amp; Interview Handbook</div>
      </div>
      <div class="contact-info">
        <div><strong>Phone:</strong> +91 9068630131</div>
        <div><strong>Email:</strong> <a href="mailto:yatin536@gmail.com">yatin536@gmail.com</a></div>
        <div><strong>Location:</strong> Noida &amp; Gurugram, India</div>
        <div><strong>LinkedIn:</strong> linkedin.com/in/yatin-kumar-s-8691b2138</div>
        <div><strong>Portfolio:</strong> yatin536.github.io/portfolio</div>
      </div>
    </div>
  </div>

  <!-- EXECUTIVE SUMMARY & MATRIX -->
  <div class="exec-summary-box">
    <strong>Document Purpose:</strong> This guide provides a comprehensive, end-to-end technical breakdown of every client project across my 3.5+ years of Data Engineering experience (Accenture, Syven Global Services, Acidaes Solutions). It is organized specifically to prepare for technical interviews—detailing business context, end-to-end data pipelines, exact tech stack choices, real production hurdles faced &amp; solved, and verbatim <strong>STAR interview pitch scripts</strong>.
  </div>

  <h3 class="section-h3">Career Projects Quick Matrix</h3>
  <table class="matrix-table">
    <thead>
      <tr>
        <th>Organization &amp; Client</th>
        <th>Project Name</th>
        <th>Core Architecture</th>
        <th>Primary Technical Challenge</th>
        <th>Key Result</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Accenture</strong><br>(GE Vernova)</td>
        <td>Automating Cash Flow Application (Agentic AI Team)</td>
        <td>AWS Kinesis &rarr; S3 Data Lake &rarr; PySpark &rarr; Athena &rarr; Snowflake</td>
        <td>High-throughput streaming data skew &amp; out-of-order financial events</td>
        <td>Sub-second ingestion, 100% financial reconciliation</td>
      </tr>
      <tr>
        <td><strong>Syven Global</strong><br>(Lazard Inc.)</td>
        <td>Multi-Warehouse Management &amp; Databricks ETL</td>
        <td>Databricks PySpark &rarr; Azure Storage &rarr; Snowflake Multi-Warehouse</td>
        <td>Concurrent multi-team query contention &amp; runaway credit consumption</td>
        <td>-35% Snowflake credits, isolated compute per team, automated SCD I &amp; II</td>
      </tr>
      <tr>
        <td><strong>Syven Global</strong><br>(Student Housing)</td>
        <td>Dashboard Performance &amp; SQL SP Optimization</td>
        <td>SQL Server SPs &rarr; Execution Plan Tuning &rarr; Python Output Handlers</td>
        <td>45s dashboard refresh latency due to table scans &amp; implicit conversions</td>
        <td>Latency cut by 90% (&lt;3s load time), automated Python SP parser</td>
      </tr>
      <tr>
        <td><strong>Acidaes Solutions</strong></td>
        <td>Relational Query Tuning &amp; Data Automation</td>
        <td>MS SQL Server &rarr; T-SQL CTEs &rarr; Index Optimization &rarr; Python</td>
        <td>Parameter sniffing &amp; index fragmentation in heavy transactional tables</td>
        <td>25-30% query speedup, 15% manual validation effort saved</td>
      </tr>
    </tbody>
  </table>

  <!-- PAGE BREAK FOR PROJECT 1: ACCENTURE / GE VERNOVA -->
  <div class="page-break"></div>

  <div class="company-banner">
    <h2>1. ACCENTURE — Client: GE Vernova (Agentic AI Team)</h2>
    <span class="tenure">August 2026 – Present | Senior Data Engineer</span>
  </div>

  <div class="project-card">
    <div class="project-title">
      <span>Project: Automating Cash Flow Application</span>
      <span class="project-tag">AWS Data Engineering &bull; Real-Time Streaming</span>
    </div>

    <div class="tech-pills">
      <span class="tech-pill">AWS Kinesis Data Streams</span>
      <span class="tech-pill">Amazon S3 (Data Lake)</span>
      <span class="tech-pill">Python</span>
      <span class="tech-pill">PySpark</span>
      <span class="tech-pill">AWS Athena</span>
      <span class="tech-pill">AWS Glue Data Catalog</span>
      <span class="tech-pill">Snowflake</span>
      <span class="tech-pill">SQL</span>
    </div>

    <h3 class="section-h3">1. Business Context &amp; Objective</h3>
    <p>
      GE Vernova's financial and treasury operations required real-time visibility into multi-currency cash flows, enterprise receivables, vendor disbursements, and liquid assets across global divisions. Prior workflows relied on fragmented batch exports and end-of-day reconciliations, resulting in delayed cash forecasting and liquidity estimation errors. The Agentic AI team was tasked with building an autonomous cash-flow intelligence platform powered by an enterprise AWS real-time data engineering backbone.
    </p>

    <h3 class="section-h3">2. End-to-End Architectural Pipeline</h3>
    <div class="arch-flow-box">[Multi-Source Financial Feeds: ERPs, Bank APIs, Invoices, SAP]
                      &darr; (JSON / Avro Events)
[AWS Kinesis Data Streams] (Partition key: entity_id &bull; 8 Shards &bull; Sub-Second Latency)
                      &darr; (Micro-batch Stream Consumer)
[Amazon S3 Raw Staging Zone] (Raw Event Lake &bull; Date Partitioned: s3://ge-cashflow/raw/YYYY/MM/DD)
                      &darr; (Distributed Cleansing &amp; Enrichment)
[Databricks / PySpark Processing Layer] (Deduplication, Currency Normalization, Event Watermarking)
                      &darr; (Curated Parquet Files)
[Amazon S3 Curated Zone] &larr;&rarr; [AWS Glue Data Catalog] &larr;&rarr; [AWS Athena Serverless SQL]
                      &darr; (High-Value Aggregations Load)
[Snowflake Virtual Warehouse: FINANCE_CASHFLOW_WH] &rarr; [Agentic AI Forecasting &amp; Executive Dashboards]</div>

    <h3 class="section-h3">3. Key Engineering Responsibilities</h3>
    <ul class="bullets">
      <li><strong>Streaming Ingestion:</strong> Configured AWS Kinesis Data Streams to ingest continuous transactional events from banking APIs and ERP systems with sub-second latency.</li>
      <li><strong>Data Lake Tiering:</strong> Designed a multi-tier S3 data lake architecture (Raw, Staging, Curated) with daily and hourly partitioning strategies to optimize query scan costs.</li>
      <li><strong>PySpark Stream Cleansing:</strong> Built PySpark jobs to perform schema validation, currency conversions using real-time FX rate lookup tables, and financial deduplication.</li>
      <li><strong>Serverless Ad-Hoc Analytics:</strong> Registered schemas in AWS Glue Data Catalog and authored optimized Athena SQL queries for finance controllers.</li>
      <li><strong>Reconciliation Engine:</strong> Formulated SQL validation procedures ensuring zero-loss audit trails and 100% mathematical reconciliation between source bank transactions and downstream financial marts.</li>
    </ul>

    <h3 class="section-h3">4. Real Production Problems Faced &amp; Solutions</h3>
    
    <div class="callout callout-challenge">
      <strong>Problem 1: Kinesis Out-of-Order Financial Events &amp; Data Skew</strong><br>
      <em>Symptom:</em> Transactions for large regional entities (e.g., US / EU hubs) were significantly higher in volume than others, causing hotspotting on specific Kinesis shards. Furthermore, network re-transmissions caused duplicate and out-of-order transaction timestamps, leading to temporary negative balances in real-time cash calculations.<br>
      <strong>Solution:</strong>
      <ul style="padding-left: 14px; margin-top: 4px;">
        <li>Refactored partition keys using a compound hash of <code>entity_id + hash(transaction_id) % shard_count</code> to distribute throughput evenly across all Kinesis shards.</li>
        <li>Implemented PySpark structured streaming windowing with event-time watermarking (15-minute threshold) and applied windowed deduplication over <code>(transaction_id, entity_id)</code> ordered by <code>event_timestamp DESC</code> to discard stale duplicates.</li>
      </ul>
    </div>

    <div class="callout callout-challenge">
      <strong>Problem 2: "Small File Problem" in S3 &amp; Athena Query Degradation</strong><br>
      <em>Symptom:</em> Real-time streaming into S3 created tens of thousands of tiny 50KB–200KB JSON files every hour. When Athena ran queries over the raw zone, query latency degraded to over 90 seconds due to S3 GET metadata overhead and full partition scanning.<br>
      <strong>Solution:</strong>
      <ul style="padding-left: 14px; margin-top: 4px;">
        <li>Architected an automated PySpark hourly compaction job that reads raw streaming chunks, coalesces them, and writes columnar, snappy-compressed Parquet files (sized optimally at 256MB to 512MB).</li>
        <li>Partitioned S3 files by <code>year=YYYY/month=MM/day=DD/currency=XXX</code>. Athena query execution dropped from 90+ seconds to under 4 seconds, and S3 scan costs were reduced by ~65%.</li>
      </ul>
    </div>

    <h3 class="section-h3">5. How to Pitch This Project to an Interviewer (STAR Script)</h3>
    <div class="callout callout-script">
      <strong>Interviewer Question: "Tell me about your current project at Accenture."</strong><br>
      <em>"At Accenture, I work within the Agentic AI team for our client GE Vernova, where we architected a real-time data engineering platform to automate enterprise cash flow operations. 
      <br><br>
      <strong>Situation &amp; Task:</strong> GE Vernova needed real-time visibility into multi-currency global liquidity across disparate ERPs and banking feeds, which were historically delayed by end-of-day batch processing. My role was to design the end-to-end ingestion and transformation pipeline on AWS.
      <br><br>
      <strong>Action:</strong> I implemented AWS Kinesis Data Streams for high-velocity streaming ingestion, routing events into a multi-tiered Amazon S3 data lake. I built distributed PySpark pipelines to cleanse, deduplicate, and normalize financial records, using event-time watermarking to guarantee accurate event ordering. For analytical querying, I leveraged the AWS Glue Data Catalog and Athena for serverless SQL access, loading curated financial aggregates into Snowflake virtual warehouses.
      <br><br>
      <strong>Result:</strong> We reduced cash flow data latency from 24 hours to sub-second ingestion, achieved 100% financial audit reconciliation, and enabled downstream AI agents to deliver predictive liquidity forecasts with zero manual intervention."</em>
    </div>

    <h3 class="section-h3">6. Key Interview Q&amp;A for this Project</h3>
    <div class="callout callout-qa">
      <strong>Q: Why did you use AWS Athena with S3 instead of loading everything directly into a database?</strong><br>
      <em>Answer:</em> "Cost efficiency and query flexibility. Daily financial streaming generates massive volumes of raw event data. Storing raw data in S3 and using Athena serverless queries allowed us to catalog everything in AWS Glue without paying continuous compute charges for raw staging. Only refined, aggregated reporting marts were pushed to Snowflake, ensuring we utilized expensive warehouse compute strictly for high-value business queries."
    </div>
  </div>

  <!-- PAGE BREAK FOR PROJECT 2: SYVEN / LAZARD INC -->
  <div class="page-break"></div>

  <div class="company-banner">
    <h2>2. SYVEN GLOBAL SERVICES — Client: Lazard Inc.</h2>
    <span class="tenure">December 2023 – August 2026 | Data Engineer</span>
  </div>

  <div class="project-card">
    <div class="project-title">
      <span>Project: Multi-Warehouse Management &amp; Databricks Ingestion</span>
      <span class="project-tag">Databricks &bull; Snowflake &bull; Azure Storage &bull; SCD I &amp; II</span>
    </div>

    <div class="tech-pills">
      <span class="tech-pill">Databricks</span>
      <span class="tech-pill">PySpark</span>
      <span class="tech-pill">Snowflake Virtual Warehouses</span>
      <span class="tech-pill">Azure Storage Accounts (ADLS Gen2)</span>
      <span class="tech-pill">SCD Type I &amp; II</span>
      <span class="tech-pill">SQL</span>
      <span class="tech-pill">Python</span>
    </div>

    <h3 class="section-h3">1. Business Context &amp; Objective</h3>
    <p>
      Lazard Inc. is a preeminent global financial advisory and asset management firm. Different internal business units—Trading, Risk Assessment, Wealth Advisory, and Corporate Analytics—were competing for computational resources on a shared, monolithic warehouse. Heavy risk simulation queries during peak trading hours caused query queuing and performance degradation for trading desk analytics. Additionally, historical financial accounts lacked automated versioning, requiring extensive manual intervention for audit tracking.
    </p>

    <h3 class="section-h3">2. End-to-End Architectural Pipeline</h3>
    <div class="arch-flow-box">[Multi-Departmental Sources: Financial Feeds, CRM, Trading Desks, Asset Logs]
                                  &darr;
[Azure Storage Accounts (ADLS Gen2 / Blob)] (Staging containers: bronze/silver/gold)
                                  &darr; (Mounted via DBFS &amp; Azure Service Principal)
[Databricks PySpark Engine] (High-throughput distributed transformations &amp; join optimizations)
                                  &darr; (Snowflake Connector with Direct Staging)
[Snowflake Cloud Data Platform]
  &boxdr;&boxh;&boxh; [Trading Virtual Warehouse] (High Concurrency &bull; Auto-scaling &bull; Size M)
  &boxdr;&boxh;&boxh; [Risk Management Warehouse] (Heavy Compute &bull; Multi-cluster &bull; Size L)
  &boxdr;&boxh;&boxh; [Corporate Analytics Warehouse] (Standard Ad-Hoc &bull; Auto-suspend 60s &bull; Size S)
                                  &darr;
[Automated SCD Type I &amp; II Framework] (MERGE semantics &bull; start_date, end_date, is_current)</div>

    <h3 class="section-h3">3. Key Engineering Responsibilities</h3>
    <ul class="bullets">
      <li><strong>Multi-Warehouse Architecture:</strong> Architected purpose-fit Snowflake virtual warehouses for each department, isolating compute workloads, preventing query queuing, and eliminating resource contention.</li>
      <li><strong>Databricks Distributed ETL:</strong> Built scalable PySpark batch pipelines on Databricks clusters, processing multi-million record transactional datasets with custom partitioning and broadcast joins.</li>
      <li><strong>Cloud Storage Integration:</strong> Mounted Azure Storage Accounts (ADLS Gen2) to Databricks workspace using secure Azure AD service principals, facilitating smooth multi-cloud data movement.</li>
      <li><strong>Automated SCD Type I &amp; II Processing:</strong> Designed and deployed automated Slowly Changing Dimension pipelines using Snowflake SQL <code>MERGE</code> statements, maintaining complete historical audit trails.</li>
      <li><strong>Cost Optimization:</strong> Configured warehouse auto-suspend (60 seconds) and auto-resume policies, avoiding idle compute credit burn.</li>
    </ul>

    <h3 class="section-h3">4. Real Production Problems Faced &amp; Solutions</h3>

    <div class="callout callout-challenge">
      <strong>Problem 1: Query Contention &amp; Snowflake Credit Runaway</strong><br>
      <em>Symptom:</em> All teams queried a single large virtual warehouse. When Risk Analysts ran heavy statistical models at 4:00 PM market close, trading queries queued for minutes. Moreover, warehouses stayed active during idle hours, wasting thousands of credits.<br>
      <strong>Solution:</strong>
      <ul style="padding-left: 14px; margin-top: 4px;">
        <li>Separated workloads into dedicated virtual warehouses: <code>TRADING_WH</code> (Medium, multi-cluster for high concurrency) and <code>RISK_WH</code> (Large, single-cluster for memory-heavy transforms).</li>
        <li>Implemented strict auto-suspend timers (set to 60 seconds of inactivity) and auto-resume.</li>
        <li>Eliminated query contention completely and reduced overall monthly Snowflake compute credit consumption by ~35%.</li>
      </ul>
    </div>

    <div class="callout callout-challenge">
      <strong>Problem 2: Data Skew &amp; Shuffle Spill in Databricks PySpark Joins</strong><br>
      <em>Symptom:</em> When joining multi-million row transaction tables with account dimension tables, jobs experienced severe execution skew. 95% of tasks finished in 2 minutes, but 2 tasks hung for over 25 minutes due to memory spill to disk caused by null/default customer keys.<br>
      <strong>Solution:</strong>
      <ul style="padding-left: 14px; margin-top: 4px;">
        <li>Isolated salted keys for skewed values and utilized <strong>broadcast hash joins</strong> (<code>broadcast(dim_accounts)</code>) for smaller dimension lookup tables (&lt;100MB), bypassing expensive network shuffles.</li>
        <li>Re-partitioned DataFrames by account hash before performing wide transformations, achieving a 30% reduction in total pipeline runtimes.</li>
      </ul>
    </div>

    <div class="callout callout-challenge">
      <strong>Problem 3: Manual SCD II Maintenance &amp; Historical Record Inconsistencies</strong><br>
      <em>Symptom:</em> Dimension changes (client address, risk profiles, regulatory tiers) were previously updated with manual scripts, causing broken date ranges, overlapping records, and missing historical states.<br>
      <strong>Solution:</strong>
      <ul style="padding-left: 14px; margin-top: 4px;">
        <li>Designed a standardized SQL <code>MERGE</code> pipeline that compares incoming source hashes with existing target records.</li>
        <li>For SCD Type I (corrections): updated attributes directly. For SCD Type II (historical changes): closed active record (<code>is_current = FALSE, end_date = CURRENT_TIMESTAMP</code>) and inserted the new active row with a new surrogate key. Slashing manual maintenance effort by 90%.</li>
      </ul>
    </div>

    <h3 class="section-h3">5. How to Pitch This Project to an Interviewer (STAR Script)</h3>
    <div class="callout callout-script">
      <strong>Interviewer Question: "Describe your experience with Databricks and Snowflake at Syven Global."</strong><br>
      <em>"At Syven Global, I led the data ingestion and warehousing architecture for our client, Lazard Inc. 
      <br><br>
      <strong>Situation &amp; Task:</strong> Lazard had multiple analytical teams—Trading, Risk, and Wealth Management—experiencing severe warehouse contention on a shared database during market closing hours. Furthermore, managing historical dimension tracking was largely manual and prone to inconsistencies.
      <br><br>
      <strong>Action:</strong> I built distributed PySpark ETL pipelines on Databricks to ingest and transform multi-departmental feeds staged in Azure Storage Accounts. To solve the concurrency bottleneck, I redesigned their Snowflake topology into isolated, purpose-fit virtual warehouses with automated scaling and 60-second auto-suspend. Additionally, I architected an automated SCD Type I &amp; II framework using Snowflake MERGE logic to capture historical audit states seamlessly.
      <br><br>
      <strong>Result:</strong> We completely eliminated query queuing during peak market close, cut monthly Snowflake credit consumption by 35%, and eliminated 90% of manual data maintenance overhead."</em>
    </div>
  </div>

  <!-- PAGE BREAK FOR PROJECT 3 & 4: STUDENT HOUSING & ACIDAES -->
  <div class="page-break"></div>

  <div class="company-banner">
    <h2>3. SYVEN GLOBAL SERVICES — Student Housing Dashboards</h2>
    <span class="tenure">Syven Global Services | Data Engineer</span>
  </div>

  <div class="project-card">
    <div class="project-title">
      <span>Project: Dashboard Performance Tuning &amp; SQL SP Optimization</span>
      <span class="project-tag">SQL Stored Procedures &bull; Execution Plans &bull; Python Handlers</span>
    </div>

    <div class="tech-pills">
      <span class="tech-pill">SQL Stored Procedures</span>
      <span class="tech-pill">Query Execution Plans</span>
      <span class="tech-pill">MS SQL Server</span>
      <span class="tech-pill">Python Automation</span>
      <span class="tech-pill">Index Optimization</span>
      <span class="tech-pill">CTEs &bull; Window Functions</span>
    </div>

    <h3 class="section-h3">1. Business Context &amp; Objective</h3>
    <p>
      The Student Housing organization managed thousands of residential beds across multiple campus properties. Operational and financial dashboards were powered by complex legacy SQL stored procedures calculating occupancy rates, revenue per bed, billing arrears, and maintenance workflows. Over time, as transaction volumes grew, executive dashboards suffered from load times exceeding 45–60 seconds, leading to timeouts during management reviews.
    </p>

    <h3 class="section-h3">2. Real Production Problems Faced &amp; Solutions</h3>
    
    <div class="callout callout-challenge">
      <strong>Problem 1: 45+ Second Dashboard Load Times &amp; Expensive Table Scans</strong><br>
      <em>Root Cause Discovery:</em> Evaluated SQL Execution Plans (Graphical &amp; XML) for the critical stored procedures. Identified:
      <ul style="padding-left: 14px; margin-top: 4px;">
        <li>Full clustered index scans across a 15-million row leasing history table caused by non-sargable <code>WHERE CONVERT(VARCHAR, lease_date, 101) = @target_date</code> conditions.</li>
        <li>Implicit data type conversion (<code>VARCHAR</code> compared against <code>NVARCHAR</code> column), preventing index seeks.</li>
        <li>Nested correlated subqueries recalculating occupancy percentages repeatedly for every row.</li>
      </ul>
      <strong>Solution:</strong>
      <ul style="padding-left: 14px; margin-top: 4px;">
        <li>Refactored query predicates to be sargable (<code>lease_date &gt;= @start AND lease_date &lt; @end</code>) and aligned data types to enable direct <strong>Index Seeks</strong>.</li>
        <li>Replaced correlated subqueries with Common Table Expressions (CTEs) and <code>SUM() OVER(PARTITION BY property_id)</code> window functions.</li>
        <li>Created targeted covering non-clustered indexes on <code>(property_id, lease_status) INCLUDE (monthly_rent, lease_date)</code>.</li>
        <li><strong>Result:</strong> Dashboard query execution dropped from <strong>48 seconds to 2.8 seconds</strong> (&gt;90% reduction in query latency).</li>
      </ul>
    </div>

    <div class="callout callout-challenge">
      <strong>Problem 2: Handling Complex Multi-Result-Set Stored Procedure Outputs</strong><br>
      <em>Challenge:</em> Legacy reporting tools struggled to ingest and parse multi-table output returned by stored procedures with varying parameter combinations.<br>
      <strong>Solution:</strong>
      <ul style="padding-left: 14px; margin-top: 4px;">
        <li>Developed modular Python automation scripts that execute stored procedures programmatically, capture multiple cursor result sets, and validate boundary limits.</li>
        <li>Parsed and structured outputs into clean, sanitized JSON feeds for downstream reporting tools, eliminating manual export steps.</li>
      </ul>
    </div>

    <h3 class="section-h3">3. How to Pitch This Project to an Interviewer (STAR Script)</h3>
    <div class="callout callout-script">
      <strong>Interviewer Question: "Can you give an example of a time you resolved a major SQL performance issue?"</strong><br>
      <em>"At Syven Global, our Student Housing executive dashboard was experiencing severe latency—taking upwards of 45 to 50 seconds to refresh, frequently causing gateway timeouts. 
      <br><br>
      <strong>Action:</strong> I opened the SQL Execution Plans for the underlying stored procedures and discovered that non-sargable date conversions and implicit data type mismatches were forcing full table scans on a 15-million row table. I refactored the stored procedures to eliminate scalar functions in the WHERE clause, restructured nested subqueries into CTEs with window functions, and designed covering non-clustered indexes. In addition, I created Python scripts to automate and validate the stored procedure outputs for the reporting layer.
      <br><br>
      <strong>Result:</strong> Query response time plummeted from 48 seconds down to under 3 seconds—a 90%+ latency reduction—completely resolving the dashboard timeout issues."</em>
    </div>
  </div>

  <div class="company-banner" style="margin-top: 24px;">
    <h2>4. ACIDAES SOLUTIONS — Relational Database Tuning &amp; Automation</h2>
    <span class="tenure">November 2022 – December 2023 | Graduate Engineer Trainee</span>
  </div>

  <div class="project-card">
    <div class="project-title">
      <span>Project: SQL Server Optimization &amp; Python Automation</span>
      <span class="project-tag">MS SQL Server &bull; T-SQL &bull; Python Cleansing</span>
    </div>

    <h3 class="section-h3">Core Highlights &amp; Interview Problem Scenario</h3>
    <div class="callout callout-challenge">
      <strong>Problem: Parameter Sniffing &amp; Plan Cache Inefficiencies</strong><br>
      <em>Scenario:</em> A high-frequency customer search stored procedure performed fast for common queries but occasionally hung, consuming 90%+ database CPU when users searched across broader parameters.<br>
      <strong>Solution:</strong> Diagnosed parameter sniffing in the SQL Server plan cache. The stored procedure compiled an execution plan optimized for a single-record lookup and reused it for broad scans. Resolved by re-assigning parameters to local variables inside the stored procedure and applying <code>OPTIMIZE FOR UNKNOWN</code> hints, providing consistent sub-second execution across all query variants.
    </div>

    <div class="callout callout-solution">
      <strong>Python Validation Impact:</strong> Built Python scripts to automate format normalization and schema assertion checks across incoming raw customer feeds, eliminating manual reconciliation steps and reducing data-handling errors by 15%.
    </div>
  </div>

  <!-- SUMMARY CHECKLIST FOR INTERVIEWS -->
  <div class="page-break"></div>

  <div class="company-banner">
    <h2>5. TECHNICAL INTERVIEW MASTER CHEAT-SHEET</h2>
    <span class="tenure">Quick-Fire Concepts &amp; Architecture Justifications</span>
  </div>

  <div class="project-card">
    <h3 class="section-h3">Key Technology Decision Justifications (Why did you choose X over Y?)</h3>
    <table class="matrix-table">
      <thead>
        <tr>
          <th>Technology Choice</th>
          <th>Alternative</th>
          <th>Why You Chose It (Interview Answer)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>AWS Kinesis</strong></td>
          <td>AWS SQS / Batch Kafka</td>
          <td>Managed real-time streaming with exact shard throughput guarantees, ordered event streaming per partition key, and native zero-code S3 delivery via Firehose/Spark.</td>
        </tr>
        <tr>
          <td><strong>Amazon S3 + Athena</strong></td>
          <td>Redshift / RDS</td>
          <td>True serverless decoupled storage and compute. Storing raw and historical files in S3 costs ~$0.023/GB, while Athena allows ad-hoc Presto SQL queries paying only for data scanned.</td>
        </tr>
        <tr>
          <td><strong>Snowflake Virtual Warehouses</strong></td>
          <td>Single Monolithic DW</td>
          <td>Compute-storage separation. Different business teams (Risk vs Trading) can run on dedicated compute clusters without locking or contending for resources, with automated 60s suspension.</td>
        </tr>
        <tr>
          <td><strong>Databricks PySpark</strong></td>
          <td>Single-node Python (Pandas)</td>
          <td>Distributed memory processing. When data exceeds single-machine RAM (multi-million rows), PySpark partitions data across cluster nodes and optimizes physical execution plans.</td>
        </tr>
        <tr>
          <td><strong>SCD Type II MERGE</strong></td>
          <td>Full Table Overwrite</td>
          <td>Preserves historical states (auditing, compliance) without duplicating unchanged records. MERGE allows atomic update of expired records and insertion of new records in one transaction.</td>
        </tr>
      </tbody>
    </table>

    <h3 class="section-h3">Top 5 Behavioral &amp; Technical Interview Traps to Avoid</h3>
    <ul class="bullets">
      <li><strong>Trap 1: Mentioning tools you haven't used.</strong> <em>Rule:</em> Stick strictly to Python, SQL, PySpark, Snowflake, AWS Data Engg (Kinesis, S3, Athena, Glue), Databricks, and basic Azure Storage. If asked about Kafka or Airflow, say: <em>"In my recent projects, we standardized on AWS Kinesis for streaming and Python/native cloud schedules, which met our throughput requirements with lower operational overhead."</em></li>
      <li><strong>Trap 2: Explaining projects only from a high-level.</strong> <em>Rule:</em> Interviewers want to hear the plumbing: partition keys, shard counts, execution plans, broadcast joins, S3 storage tiers, and MERGE semantics.</li>
      <li><strong>Trap 3: Claiming everything worked smoothly.</strong> <em>Rule:</em> Senior engineers are evaluated on how they handle failures. Always mention data skew, small files in S3, or non-sargable query scans and how you diagnosed and resolved them.</li>
    </ul>

    <div class="footer-note">
      Compiled for <strong>Yatin Kumar Singh</strong> • Senior Data Engineer • Confidential Interview Preparation Document
    </div>
  </div>

</body>
</html>
"""

def generate():
    # 1. Write the HTML file
    with open(OUTPUT_HTML, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    print(f"Created HTML file: {OUTPUT_HTML}")

    # 2. Run Edge in headless mode to generate the PDF
    cmd = [
        EDGE_EXE,
        "--headless",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={OUTPUT_PDF}",
        f"file:///{OUTPUT_HTML.replace(os.sep, '/')}"
    ]

    print("Generating PDF via Microsoft Edge...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0 and os.path.exists(OUTPUT_PDF):
        size_kb = os.path.getsize(OUTPUT_PDF) / 1024
        print(f"SUCCESS: PDF generated at: {OUTPUT_PDF} ({size_kb:.1f} KB)")
    else:
        print("Error generating PDF:", result.stderr)

if __name__ == "__main__":
    generate()
