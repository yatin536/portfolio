"""
Yatin Kumar Singh - Portfolio Data Source
Centralized structured data model for the portfolio website.
Update this file anytime you want to add new skills, projects, or experiences.
"""

PROFILE = {
    "name": "Yatin Kumar Singh",
    "role": "Senior Data Engineer",
    "title_tagline": "AWS Data Stack (Athena, Glue ETL, Kinesis) • Databricks & PySpark • Snowflake • Real-Time & Batch Streaming",
    "location": "Noida & Gurugram, Uttar Pradesh, India",
    "email": "yatin536@gmail.com",
    "phone": "+91 9068630131",
    "phone_clean": "+919068630131",
    "linkedin": "https://www.linkedin.com/in/yatin-kumar-s-8691b2138",
    "linkedin_short": "in/yatin-kumar-s-8691b2138",
    "github": "https://github.com/yatin-singh",
    "years_experience": "3.5+",
    "summary": (
        "Data Engineer with 3.5+ years of experience designing, building, and optimizing scalable "
        "data pipelines and analytics solutions. Strong expertise in AWS big data services (Athena, "
        "Glue ETL, Kinesis, S3), Databricks & PySpark distributed processing, Snowflake data warehousing, "
        "and SQL optimization, enabling real-time streaming, high-throughput batch ETL, and reliable business intelligence."
    ),
    "about_long": (
        "I am a Senior Data Engineer specializing in building scalable real-time streaming and high-throughput "
        "batch data architectures. Over the last 3.5+ years across enterprise environments including Accenture, "
        "Syven Global Services, and Acidaes Solutions, I have focused heavily on the AWS big data ecosystem—leveraging "
        "AWS Kinesis for real-time streaming data ingestion, AWS Glue ETL for serverless Spark transformations, "
        "Amazon Athena for fast interactive SQL queries over S3 data lakes, and Amazon S3 for resilient data lake storage.\n\n"
        "I have a strong hold over Databricks and PySpark, designing memory-optimized distributed processing "
        "pipelines that cut compute runtimes by 30%. In addition, I bring deep expertise in Snowflake data warehousing "
        "(clustering keys, micro-partitioning, and automated SCD Type I & II change data capture), advanced SQL tuning "
        "(reducing query latencies by 25-30%), and foundational experience with Azure Storage Accounts and connecting Azure "
        "storage layers to Databricks for unified storage solutions."
    ),
    "stats": [
        {"value": "3.5+", "label": "Years Experience", "sub": "Enterprise Data Engineering"},
        {"value": "50+", "label": "Optimized SQL Workloads", "sub": "Views, Procedures & CTEs"},
        {"value": "90%", "label": "Manual Effort Reduced", "sub": "Automated SCD I & II Workflows"},
        {"value": "30%", "label": "Performance Boost", "sub": "Databricks & PySpark Pipelines"},
        {"value": "25%", "label": "Query Latency Reduction", "sub": "Snowflake & Athena Optimization"},
        {"value": "95-99%", "label": "Reporting Accuracy", "sub": "Delivered across BI Dashboards"}
    ]
}

SKILLS = {
    "AWS & Big Data Streaming": [
        {"name": "AWS Athena (Serverless SQL Querying)", "level": 94, "highlight": True},
        {"name": "AWS Glue ETL (Serverless Spark & Catalog)", "level": 92, "highlight": True},
        {"name": "AWS Kinesis (Real-Time Streaming Data)", "level": 90, "highlight": True},
        {"name": "Amazon S3 (Data Lake Architecture & Partitioning)", "level": 95, "highlight": True},
        {"name": "AWS Glue Data Catalog & Crawlers", "level": 90, "highlight": False},
        {"name": "Real-Time Event Stream Ingestion", "level": 90, "highlight": True}
    ],
    "Databricks & PySpark": [
        {"name": "Databricks (Lakehouse Architecture & Clusters)", "level": 94, "highlight": True},
        {"name": "PySpark (Distributed DataFrames & Spark SQL)", "level": 92, "highlight": True},
        {"name": "Partitioning, Broadcast Joins & Shuffling", "level": 90, "highlight": True},
        {"name": "Delta Lake & Parquet Formats", "level": 88, "highlight": False},
        {"name": "Connecting Cloud Storage to Databricks", "level": 92, "highlight": True}
    ],
    "Snowflake & Data Warehousing": [
        {"name": "Snowflake Cloud Data Platform", "level": 95, "highlight": True},
        {"name": "Snowflake Virtual Warehouses & Multi-Cluster", "level": 95, "highlight": True},
        {"name": "Clustering Keys & Micro-partitions", "level": 92, "highlight": True},
        {"name": "SCD Type I & Type II Automation", "level": 95, "highlight": True},
        {"name": "Dimensional Modeling (Star & Snowflake Schema)", "level": 94, "highlight": True},
        {"name": "Snowflake External Stages & Snowpipe", "level": 90, "highlight": False}
    ],
    "Programming & SQL Tuning": [
        {"name": "SQL (Advanced CTEs, Windowing, Stored Procs)", "level": 98, "highlight": True},
        {"name": "Python (Data Pipelines, API Ingestion, Automation)", "level": 92, "highlight": True},
        {"name": "Athena / Presto SQL Tuning", "level": 92, "highlight": True},
        {"name": "Snowflake SQL & UDFs", "level": 94, "highlight": True},
        {"name": "Query Profiling & Execution Plan Analysis", "level": 94, "highlight": True},
        {"name": "MS SQL Server & T-SQL", "level": 88, "highlight": False}
    ],
    "Azure (Foundational) & Tools": [
        {"name": "Azure Storage Accounts (ADLS Gen2 / Blob)", "level": 80, "highlight": False},
        {"name": "Connecting Azure Storage to Databricks", "level": 84, "highlight": True},
        {"name": "Apache Airflow (DAGs & Scheduling)", "level": 88, "highlight": False},
        {"name": "Data Validation & Quality Reconciliation", "level": 92, "highlight": False},
        {"name": "Pentaho Data Integration (PDI)", "level": 85, "highlight": False},
        {"name": "Git, Documentation & Stakeholder Collaboration", "level": 92, "highlight": False}
    ]
}

EXPERIENCE = [
    {
        "role": "Sr. Data Engineer",
        "company": "Accenture",
        "location": "Gurugram, Haryana, India",
        "period": "August 2026 - Present",
        "badge": "Current Role",
        "summary": "Driving cloud data engineering initiatives with emphasis on AWS data lakes (S3, Athena, Glue), Databricks PySpark workloads, and Snowflake.",
        "highlights": [
            "Contributing to enterprise-scale cloud data engineering initiatives and modern analytical environments.",
            "Building and optimizing AWS-based data engineering workflows, including Amazon S3 data ingestion, AWS Glue ETL jobs, and interactive Athena querying.",
            "Developing distributed PySpark pipelines on Databricks for high-throughput batch transformations and stream enrichment.",
            "Architecting high-performance SQL and Python workflows for data querying, transformation, automated validation, and data-processing activities.",
            "Configuring cloud storage integrations, connecting Azure Storage Accounts to Databricks for unified lakehouse storage solutions.",
            "Strengthening production architectures across Snowflake virtual warehouses, clustering keys, AWS services, and modern big data ecosystems.",
            "Enforcing engineering best practices around Git version control, testing frameworks, comprehensive technical documentation, and cross-functional agile delivery."
        ],
        "tags": ["AWS S3", "AWS Athena", "AWS Glue ETL", "Databricks", "PySpark", "Snowflake", "Python", "SQL", "Azure Storage"]
    },
    {
        "role": "Data Engineer",
        "company": "Syven Global Services Pvt. Ltd.",
        "location": "Noida, Uttar Pradesh, India",
        "period": "December 2023 - August 2026",
        "badge": "2 yrs 9 mos",
        "summary": "Engineered real-time streaming with AWS Kinesis, serverless data lake querying with Athena, distributed PySpark pipelines on Databricks, and Snowflake warehouses.",
        "highlights": [
            "Implemented real-time streaming data ingestion pipelines using AWS Kinesis, streaming event datasets reliably into Amazon S3 storage layers.",
            "Leveraged AWS Athena and Glue Data Catalog to execute ad-hoc and scheduled analytical queries directly over large S3 data lakes with sub-minute response times.",
            "Developed distributed PySpark pipelines on Databricks for processing large-scale structured and semi-structured datasets, utilizing custom partitioning, broadcast joins, and incremental processing to boost transformation performance by ~30%.",
            "Connected Azure Storage Accounts to Databricks to mount remote storage containers and support hybrid cloud data ingestion workflows.",
            "Designed and managed Snowflake data warehouses across multiple business domains, configuring purpose-fit virtual warehouses to isolate and accelerate analytical workloads.",
            "Implemented Snowflake clustering keys and query optimization techniques on massive multi-million row datasets, reducing query execution times by approximately 25%.",
            "Engineered automated Slowly Changing Dimension (SCD Type I and Type II) processing for millions of historical records, automating change data capture and slashing manual intervention by ~90%.",
            "Developed and optimized 50+ complex SQL queries, views, functions, stored procedures, and triggers, supporting reporting and analytical workloads for 20+ users.",
            "Authored modular Python scripts for API data cleansing, schema validation, and pruning, improving dataset quality by ~25% and reducing downstream ingestion errors to near zero.",
            "Built and maintained scheduled data workflows using Apache Airflow, ensuring high availability and reliable execution of recurring data-processing pipelines.",
            "Designed and delivered weekly, monthly, and yearly performance dashboards using advanced dimensional modeling, supporting 10+ stakeholders with 95–99% reporting accuracy."
        ],
        "tags": ["AWS Kinesis", "AWS Athena", "AWS Glue ETL", "AWS S3", "Databricks", "PySpark", "Snowflake", "SCD I & II", "Python", "Airflow", "Azure Storage"]
    },
    {
        "role": "Graduate Engineer Trainee",
        "company": "Acidaes Solutions Pvt. Ltd.",
        "location": "Noida, Uttar Pradesh, India",
        "period": "November 2022 - December 2023",
        "badge": "1 yr 2 mos",
        "summary": "Specialized in relational database performance tuning, SQL Server stored procedure optimization, and automated Pentaho ETL data pipelines.",
        "highlights": [
            "Engineered and optimized Microsoft SQL Server queries, stored procedures, Common Table Expressions (CTEs), views, and database objects, lifting query performance by up to 30% across reporting and application workloads.",
            "Optimized resource-heavy SQL workloads using CTEs, correlated subqueries, selective indexing, and filtering techniques, reducing execution times by ~25% for high-frequency queries.",
            "Created Python automation scripts for data cleansing, validation, and format normalization, reducing manual data-handling workloads by approximately 15%.",
            "Developed and maintained Pentaho Data Integration (PDI) ETL workflows integrating data from CSV, Excel, flat files, and relational databases, improving end-to-end processing efficiency by ~40%.",
            "Conducted rigorous data profiling, boundary testing, and reconciliation checks across source datasets, safeguarding near-perfect data accuracy for analytics consumers.",
            "Configured dynamic parameters, filters, and aggregations for analytical reporting layers, enhancing report usability and boosting stakeholder satisfaction by ~20%."
        ],
        "tags": ["MS SQL Server", "T-SQL", "Pentaho PDI", "Python", "Data Profiling", "ETL Pipelines", "Query Optimization", "Reporting"]
    }
]

EDUCATION = {
    "degree": "B.Tech, Computer Science & Engineering",
    "institution": "JECRC UNIVERSITY",
    "location": "Jaipur, Rajasthan, India",
    "year": "2022",
    "grade": "8.5 CGPA",
    "highlights": [
        "Strong academic foundation in Database Management Systems (DBMS), Distributed Computing, Data Structures & Algorithms, and Cloud Architectures.",
        "Graduated with distinction (8.5 CGPA), actively engaged in hands-on data modeling and algorithmic computing projects."
    ]
}

PROJECTS = [
    {
        "id": "aws-kinesis-realtime-streaming",
        "title": "Real-Time Streaming & Lakehouse Pipeline",
        "subtitle": "AWS Kinesis Data Streams • S3 Data Lake • Athena Serverless",
        "description": (
            "Designed and implemented an end-to-end real-time streaming pipeline using AWS Kinesis Data Streams "
            "to capture continuous API events and transactional logs. Ingests data into Amazon S3 raw buckets, formats into "
            "partitioned Parquet, and exposes datasets via AWS Glue Data Catalog and AWS Athena for near-instantaneous SQL analytics."
        ),
        "metrics": [
            {"label": "Latency", "val": "Sub-Second Ingestion"},
            {"label": "Query Engine", "val": "AWS Athena"},
            {"label": "Streaming Source", "val": "AWS Kinesis"}
        ],
        "tech_stack": ["AWS Kinesis", "AWS Athena", "AWS Glue", "Amazon S3", "Parquet", "Python"],
        "category": "AWS & Streaming",
        "icon": "zap"
    },
    {
        "id": "databricks-pyspark-distributed-engine",
        "title": "High-Performance Databricks & PySpark Engine",
        "subtitle": "Distributed Processing with Cloud Storage Integration",
        "description": (
            "Engineered distributed PySpark ETL pipelines on Databricks to transform multi-million record datasets. "
            "Mounted and connected Azure Storage Accounts (ADLS Gen2) and AWS S3 buckets to Databricks workspace. "
            "Applied custom column partitioning, broadcast hash joins, and memory caching, achieving a 30% reduction in job runtime."
        ),
        "metrics": [
            {"label": "Compute Gain", "val": "+30% Faster"},
            {"label": "Storage Integration", "val": "Azure & AWS S3"},
            {"label": "Scale", "val": "Millions of Records"}
        ],
        "tech_stack": ["Databricks", "PySpark", "Delta Lake", "Azure Storage", "AWS S3", "Airflow"],
        "category": "Databricks & PySpark",
        "icon": "cpu"
    },
    {
        "id": "aws-glue-etl-snowflake-lakehouse",
        "title": "Serverless AWS Glue ETL & Snowflake Warehouse",
        "subtitle": "Serverless Data Catalog, Crawlers & Departmental Warehouses",
        "description": (
            "Built automated serverless ETL jobs using AWS Glue ETL and Glue Crawlers to catalog and transform raw data "
            "from Amazon S3. Ingested curated datasets into Snowflake virtual warehouses with clustering keys to optimize "
            "analytical reporting queries for multiple business departments without resource contention."
        ),
        "metrics": [
            {"label": "Query Latency", "val": "-25% Faster"},
            {"label": "ETL Architecture", "val": "Serverless Spark"},
            {"label": "Cataloging", "val": "AWS Glue Catalog"}
        ],
        "tech_stack": ["AWS Glue ETL", "AWS S3", "Snowflake", "Clustering Keys", "SQL", "Python"],
        "category": "AWS & Streaming",
        "icon": "database"
    },
    {
        "id": "automated-scd-historical-tracker",
        "title": "Automated SCD Type I & II Change Data Platform",
        "subtitle": "Historical Record Versioning & Audit Reconciliation",
        "description": (
            "Designed and deployed an automated Slowly Changing Dimension (SCD Type I and II) processing framework "
            "for dimensional tables containing millions of records. Utilized Snowflake MERGE semantics, effective date stamping "
            "(`start_date`, `end_date`, `is_current`), and surrogate key generation, reducing manual developer overhead by 90%."
        ),
        "metrics": [
            {"label": "Manual Work", "val": "-90% Reduced"},
            {"label": "Audit Traceability", "val": "100%"},
            {"label": "Processing Type", "val": "SCD Type I & II"}
        ],
        "tech_stack": ["Snowflake SQL", "Python", "MERGE Logic", "Dimensional Modeling", "Data Auditing"],
        "category": "Data Modeling",
        "icon": "git-commit"
    },
    {
        "id": "enterprise-query-optimization",
        "title": "High-Impact SQL & Serverless Query Optimization",
        "subtitle": "Refactoring Athena Queries, Snowflake Clustering & Stored Procs",
        "description": (
            "Audited and optimized over 50+ mission-critical queries, views, stored procedures, and triggers across "
            "AWS Athena, Snowflake, and SQL Server. Restructured joins, eliminated full partition scans using S3 date keys, "
            "and tuned Snowflake clustering keys, cutting query latency by 25–30%."
        ),
        "metrics": [
            {"label": "Execution Time", "val": "25-30% Faster"},
            {"label": "Workloads Refactored", "val": "50+ Objects"},
            {"label": "Platforms Tuned", "val": "Athena & Snowflake"}
        ],
        "tech_stack": ["AWS Athena", "Snowflake", "SQL Server", "Execution Plans", "Clustering Keys"],
        "category": "SQL Optimization",
        "icon": "zap"
    },
    {
        "id": "api-cleansing-automation",
        "title": "Python API Cleansing & Validation Pipeline",
        "subtitle": "Pre-Ingestion Data Sanitization & Ingestion Quality Gate",
        "description": (
            "Created modular Python automation micro-pipelines to ingest raw JSON responses from external REST APIs. "
            "Performs schema enforcement, anomaly pruning, null reconciliation, and deduplication prior to staging in "
            "Amazon S3 and Kinesis, raising data quality by 25% and reducing downstream ingestion errors to near zero."
        ),
        "metrics": [
            {"label": "Data Quality", "val": "+25% Increase"},
            {"label": "Ingestion Errors", "val": "Near Zero"},
            {"label": "Automation", "val": "100% Scheduled"}
        ],
        "tech_stack": ["Python", "AWS S3", "REST APIs", "Pandas", "JSON Parsing", "Airflow"],
        "category": "Data Modeling",
        "icon": "shield-check"
    }
]

PIPELINE_STAGES = [
    {
        "step": "01. INGEST",
        "title": "Real-Time & Batch Ingestion",
        "desc": "Ingesting high-velocity event streams via AWS Kinesis and batch files into Amazon S3 data lakes and Azure Storage Accounts.",
        "tech": "AWS Kinesis, Amazon S3, Azure Storage Accounts, REST APIs, Python"
    },
    {
        "step": "02. CATALOG & VALIDATE",
        "title": "Quality Gate & Schema Catalog",
        "desc": "Automated AWS Glue Data Catalog crawlers, schema enforcement, deduplication, and anomaly pruning to guarantee clean ingestion.",
        "tech": "AWS Glue Catalog, Python Data Profilers, Custom Assertions"
    },
    {
        "step": "03. TRANSFORM",
        "title": "Distributed Databricks & Glue Processing",
        "desc": "Scalable PySpark processing on Databricks clusters and AWS Glue ETL with custom partitioning, Delta Lake, and SCD Type I/II versioning.",
        "tech": "Databricks, PySpark, AWS Glue ETL, Delta Lake, Snowflake"
    },
    {
        "step": "04. ORCHESTRATE",
        "title": "Workflow Automation & Airflow DAGs",
        "desc": "Dependency management, automated retry policies, sensor triggers, and failure alerts across pipeline workflows.",
        "tech": "Apache Airflow, AWS EventBridge, Python, Git"
    },
    {
        "step": "05. SERVE",
        "title": "Serverless Athena & Snowflake Warehousing",
        "desc": "Serving fast ad-hoc SQL queries with AWS Athena over S3 and clustered Snowflake virtual warehouses powering executive dashboards.",
        "tech": "AWS Athena, Snowflake Multi-Cluster, Star Schema, BI Dashboards"
    }
]
