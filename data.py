"""
Yatin Kumar Singh - Portfolio Data Source
Centralized structured data model for the portfolio website and resume.
Contains verified client projects, achievements, and tech stack.
"""

PROFILE = {
    "name": "Yatin Kumar Singh",
    "role": "Senior Data Engineer",
    "title_tagline": "AWS Data Engineering (Kinesis, S3, Athena, Glue) • Databricks & PySpark • Snowflake • SQL Optimization",
    "location": "Noida & Gurugram, Uttar Pradesh, India",
    "email": "yatin536@gmail.com",
    "phone": "+91 9068630131",
    "phone_clean": "+919068630131",
    "linkedin": "https://www.linkedin.com/in/yatin-kumar-s-8691b2138",
    "linkedin_short": "in/yatin-kumar-s-8691b2138",
    "github": "https://github.com/yatin536",
    "years_experience": "3.5+",
    "summary": (
        "Data Engineer with 3.5+ years of experience designing, building, and optimizing scalable cloud data "
        "pipelines, real-time streaming architectures, and multi-tenant data warehouses. Strong expertise in "
        "AWS Data Engineering (Kinesis, S3, Athena, Glue ETL), Databricks & PySpark distributed processing, "
        "Snowflake multi-warehouse management, advanced SQL query & stored procedure optimization (execution plan analysis), "
        "and foundational Azure Storage integration."
    ),
    "about_long": (
        "I am a Senior Data Engineer specializing in building scalable real-time streaming, high-throughput "
        "batch data architectures, and optimized data warehousing solutions. In my current role at Accenture, "
        "I work within the Agentic AI team for Client GE Vernova, architecting AWS Data Engineering pipelines "
        "for automating the enterprise Cash Flow application—ingesting multi-source financial and operational data "
        "using AWS Kinesis for real-time streaming, Amazon S3 as a centralized data lake, and Python/PySpark for automated transformations.\n\n"
        "Previously at Syven Global Services, I delivered on two core enterprise projects: for Client Lazard Inc., "
        "I created and managed end-to-end data ingestion pipelines, managed multiple Snowflake virtual warehouses across "
        "diverse business teams to isolate compute and eliminate contention, and built distributed Databricks ETL pipelines "
        "with PySpark (connecting Azure Storage to Databricks). On the Student Housing Dashboards project, I significantly "
        "accelerated dashboard performance by analyzing SQL Stored Procedures, examining query execution plans to eliminate "
        "bottlenecks, and writing Python scripts to automate stored procedure outputs. My overall technical expertise is firmly "
        "grounded in Python, SQL, PySpark, Snowflake, AWS Data Engineering, Databricks, and Azure Storage solutions."
    ),
    "stats": [
        {"value": "3.5+", "label": "Years Experience", "sub": "Enterprise Data Engineering"},
        {"value": "50+", "label": "Optimized SQL Workloads", "sub": "Stored Procs, Views & Execution Plans"},
        {"value": "90%", "label": "Manual Effort Reduced", "sub": "Automated SCD I & II Pipelines"},
        {"value": "30%", "label": "Performance Boost", "sub": "Databricks & PySpark Workloads"},
        {"value": "25-30%", "label": "Query Latency Reduction", "sub": "SQL & Dashboard Optimization"},
        {"value": "100%", "label": "Reconciliation Accuracy", "sub": "Cash Flow & Reporting Automation"}
    ]
}

SKILLS = {
    "AWS Data Engineering": [
        {"name": "AWS Kinesis (Real-Time Event Streaming)", "level": 92, "highlight": True},
        {"name": "Amazon S3 (Data Lake Architecture & Partitioning)", "level": 95, "highlight": True},
        {"name": "AWS Athena (Serverless SQL Querying)", "level": 94, "highlight": True},
        {"name": "AWS Glue ETL (Serverless Spark & Data Catalog)", "level": 90, "highlight": True},
        {"name": "Multi-Source Data Ingestion", "level": 92, "highlight": True}
    ],
    "Databricks & PySpark": [
        {"name": "Databricks (Lakehouse Architecture & Compute Clusters)", "level": 94, "highlight": True},
        {"name": "PySpark (Distributed DataFrames & Spark SQL)", "level": 92, "highlight": True},
        {"name": "Performance Tuning (Partitioning, Broadcast Joins)", "level": 90, "highlight": True},
        {"name": "Connecting Cloud Storage to Databricks", "level": 92, "highlight": True},
        {"name": "Delta Lake & Parquet Formats", "level": 88, "highlight": False}
    ],
    "Snowflake & Data Warehousing": [
        {"name": "Snowflake Cloud Data Platform", "level": 95, "highlight": True},
        {"name": "Multi-Warehouse Management & Team Compute Isolation", "level": 95, "highlight": True},
        {"name": "Clustering Keys & Micro-Partitioning", "level": 92, "highlight": True},
        {"name": "SCD Type I & Type II Automation", "level": 94, "highlight": True},
        {"name": "Dimensional Modeling (Star & Snowflake Schema)", "level": 92, "highlight": True}
    ],
    "SQL & Performance Tuning": [
        {"name": "SQL (Advanced CTEs, Window Functions, Complex Joins)", "level": 98, "highlight": True},
        {"name": "SQL Stored Procedures & Logic Optimization", "level": 96, "highlight": True},
        {"name": "Query Execution Plan Analysis & Bottleneck Elimination", "level": 95, "highlight": True},
        {"name": "Dashboard Query Performance Tuning", "level": 94, "highlight": True},
        {"name": "MS SQL Server & T-SQL", "level": 88, "highlight": False}
    ],
    "Python & Data Automation": [
        {"name": "Python (Data Pipelines, Ingestion & Automation)", "level": 94, "highlight": True},
        {"name": "Python SP Output Parsing & Handling Scripts", "level": 92, "highlight": True},
        {"name": "Data Cleansing, Boundary Checks & Schema Validation", "level": 92, "highlight": True},
        {"name": "REST API Ingestion & JSON Transformation", "level": 90, "highlight": False}
    ],
    "Azure (Basics)": [
        {"name": "Azure Storage Accounts (ADLS Gen2 / Blob Storage)", "level": 84, "highlight": True},
        {"name": "Connecting Azure Storage to Databricks", "level": 88, "highlight": True},
        {"name": "Hybrid Cloud Storage Mounts", "level": 82, "highlight": False}
    ]
}

EXPERIENCE = [
    {
        "role": "Sr. Data Engineer",
        "company": "Accenture",
        "client": "GE Vernova",
        "location": "Gurugram, Haryana, India",
        "period": "August 2026 - Present",
        "badge": "Current Role",
        "summary": "Working in the Agentic AI team for Client GE Vernova, architecting AWS Data Engineering pipelines for Cash Flow application automation.",
        "projects": [
            {
                "name": "Agentic AI Team — Automating Cash Flow Application",
                "desc": "Client: GE Vernova • AWS Data Engineering & Real-Time Streaming",
                "highlights": [
                    "Spearheading AWS Data Engineering architecture for GE Vernova within the Agentic AI team to automate financial Cash Flow operations and analytics.",
                    "Engineered real-time data ingestion pipelines using AWS Kinesis Data Streams to ingest multi-source transactional, ERP, and cash flow events continuously into an Amazon S3 data lake.",
                    "Designed Amazon S3 data lake storage hierarchy with partitioned raw, staging, and curated zones, ensuring optimal parquet storage and high data availability.",
                    "Developing modular Python and PySpark workflows to parse, cleanse, and normalize financial records, feeding downstream agentic AI inference and cash flow forecasting models.",
                    "Employed AWS Athena and AWS Glue Data Catalog for serverless schema discovery, executing ad-hoc and automated SQL queries over S3 data lake tables.",
                    "Constructed optimized SQL queries, financial aggregations, and automated validation scripts, guaranteeing 100% reconciliation and data consistency across financial reporting."
                ]
            }
        ],
        "highlights": [
            "Spearheading AWS Data Engineering architecture for GE Vernova within the Agentic AI team to automate financial Cash Flow operations and analytics.",
            "Engineered real-time data ingestion pipelines using AWS Kinesis Data Streams to ingest multi-source transactional, ERP, and cash flow events continuously into an Amazon S3 data lake.",
            "Designed Amazon S3 data lake storage hierarchy with partitioned raw, staging, and curated zones, ensuring optimal parquet storage and high data availability.",
            "Developing modular Python and PySpark workflows to parse, cleanse, and normalize financial records, feeding downstream agentic AI inference and cash flow forecasting models.",
            "Employed AWS Athena and AWS Glue Data Catalog for serverless schema discovery, executing ad-hoc and automated SQL queries over S3 data lake tables.",
            "Constructed optimized SQL queries, financial aggregations, and automated validation scripts, guaranteeing 100% reconciliation and data consistency across financial reporting."
        ],
        "tags": ["AWS Kinesis", "Amazon S3", "AWS Athena", "AWS Glue ETL", "PySpark", "Python", "SQL", "Agentic AI", "GE Vernova"]
    },
    {
        "role": "Data Engineer",
        "company": "Syven Global Services Pvt. Ltd.",
        "location": "Noida, Uttar Pradesh, India",
        "period": "December 2023 - August 2026",
        "badge": "2 yrs 9 mos",
        "summary": "Delivered two enterprise client initiatives: multi-warehouse data ingestion and Databricks ETL for Lazard Inc., and SQL Stored Procedure performance tuning for Student Housing Dashboards.",
        "projects": [
            {
                "name": "Project 1: Data Ingestion & Multi-Warehouse Management",
                "desc": "Client: Lazard Inc. • Databricks ETL & Snowflake Warehousing",
                "highlights": [
                    "Created and managed end-to-end data ingestion pipelines integrating multiple cross-organizational data sources across business teams at Lazard Inc.",
                    "Configured and managed multiple Snowflake virtual warehouses to isolate compute workloads across distinct Lazard teams, eliminating query contention and reducing compute costs.",
                    "Built robust, distributed ETL pipelines using Databricks and PySpark, processing and transforming multi-departmental datasets into curated analytical models.",
                    "Engineered automated Slowly Changing Dimensions (SCD Type I & II) using Snowflake SQL and MERGE statements, slashing manual data maintenance effort by 90%.",
                    "Connected Azure Storage Accounts to Databricks to mount cloud storage containers, enabling reliable hybrid cloud data ingestion."
                ]
            },
            {
                "name": "Project 2: Student Housing Dashboards",
                "desc": "Dashboard Performance Optimization & SQL Stored Procedures",
                "highlights": [
                    "Significantly boosted dashboard performance and data refresh speeds across Student Housing Dashboards by auditing and refactoring SQL Stored Procedures.",
                    "Analyzed multiple SQL Execution Plans to pinpoint performance bottlenecks, eliminate expensive full-table scans, and optimize indexing structures.",
                    "Developed modular Python scripts to capture, parse, and automate the handling of outputs from SQL stored procedures for downstream analytics and reporting.",
                    "Restructured complex analytical queries, views, and CTEs, achieving a 25–30% reduction in query latency and ensuring sub-second metric refreshes."
                ]
            }
        ],
        "highlights": [
            "Client Lazard Inc.: Created and managed end-to-end data ingestion pipelines integrating multiple cross-organizational data sources across Lazard.",
            "Client Lazard Inc.: Configured and managed multiple Snowflake virtual warehouses to isolate compute workloads across distinct teams, eliminating contention.",
            "Client Lazard Inc.: Built distributed ETL pipelines using Databricks and PySpark to process and transform multi-departmental datasets into curated analytical models.",
            "Client Lazard Inc.: Engineered automated Slowly Changing Dimensions (SCD Type I & II) with Snowflake SQL MERGE logic, slashing manual effort by 90%.",
            "Client Lazard Inc.: Connected Azure Storage Accounts to Databricks to mount cloud storage containers for hybrid cloud ingestion.",
            "Student Housing: Significantly boosted dashboard performance by analyzing and refactoring SQL Stored Procedures.",
            "Student Housing: Examined multiple SQL Execution Plans to identify bottlenecks, eliminate full-table scans, and optimize index structures.",
            "Student Housing: Developed modular Python scripts to capture, parse, and automate the handling of outputs from SQL stored procedures."
        ],
        "tags": ["Databricks", "PySpark", "Snowflake", "SQL Stored Procedures", "Execution Plans", "Python", "Azure Storage", "Lazard Inc.", "SCD I & II"]
    },
    {
        "role": "Graduate Engineer Trainee",
        "company": "Acidaes Solutions Pvt. Ltd.",
        "location": "Noida, Uttar Pradesh, India",
        "period": "November 2022 - December 2023",
        "badge": "1 yr 2 mos",
        "summary": "Specialized in relational database performance tuning, SQL Server stored procedure optimization, execution plan analysis, and Python automation.",
        "highlights": [
            "Engineered and optimized Microsoft SQL Server queries, stored procedures, Common Table Expressions (CTEs), and views, boosting execution performance by ~25-30%.",
            "Analyzed SQL execution plans to identify bottlenecks, eliminate full-table scans, and optimize index utilization across transactional tables.",
            "Created modular Python automation scripts for data cleansing, validation, and format normalization, reducing manual data handling by 15%.",
            "Conducted data profiling, schema validation, and reconciliation checks to safeguard data accuracy across operational reporting systems.",
            "Configured dynamic SQL parameters, filters, and aggregations for reporting layers, boosting query responsiveness."
        ],
        "tags": ["MS SQL Server", "T-SQL", "Stored Procedures", "Execution Plans", "Python", "Query Optimization", "Data Profiling"]
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
        "id": "ge-vernova-cashflow-automation",
        "title": "GE Vernova - Cash Flow Automation Platform",
        "subtitle": "Client: GE Vernova • Agentic AI Team • AWS Kinesis • S3 Data Lake",
        "description": (
            "Architected real-time streaming and ingestion pipelines for GE Vernova's Agentic AI initiative to automate "
            "enterprise Cash Flow calculations. Ingests high-velocity financial streams via AWS Kinesis into an Amazon S3 "
            "Data Lake, using Athena for serverless SQL querying and Python/PySpark for automated transformations and financial reconciliation."
        ),
        "metrics": [
            {"label": "Streaming Engine", "val": "AWS Kinesis"},
            {"label": "Data Lake", "val": "Amazon S3"},
            {"label": "Reconciliation", "val": "100% Accuracy"}
        ],
        "tech_stack": ["AWS Kinesis", "Amazon S3", "AWS Athena", "AWS Glue", "Python", "PySpark", "SQL"],
        "category": "AWS Data Engg",
        "icon": "zap"
    },
    {
        "id": "lazard-multiwarehouse-databricks",
        "title": "Lazard Inc. - Multi-Warehouse & Databricks Ingestion",
        "subtitle": "Client: Lazard Inc. • Databricks PySpark • Snowflake Multi-Warehouse",
        "description": (
            "Created and managed end-to-end data ingestion pipelines and dedicated Snowflake virtual warehouses across diverse "
            "business teams at Lazard Inc. Built distributed PySpark ETL pipelines on Databricks to transform multi-departmental "
            "datasets, connecting Azure Storage Accounts to Databricks for unified lakehouse storage."
        ),
        "metrics": [
            {"label": "Compute Gain", "val": "+30% Faster"},
            {"label": "Warehousing", "val": "Multi-Warehouse"},
            {"label": "Storage Integration", "val": "Azure & Databricks"}
        ],
        "tech_stack": ["Databricks", "PySpark", "Snowflake", "Azure Storage", "Python", "SQL"],
        "category": "Databricks & PySpark",
        "icon": "cpu"
    },
    {
        "id": "student-housing-sql-optimization",
        "title": "Student Housing - Dashboard Performance & SQL SP Tuning",
        "subtitle": "SQL Stored Procedures • Execution Plan Analysis • Python SP Output Handler",
        "description": (
            "Dramatically improved dashboard performance for Student Housing analytics by analyzing SQL Stored Procedures and "
            "examining multiple query Execution Plans. Produced modular Python scripts to parse and handle outputs from stored "
            "procedures, eliminating bottlenecks and slashing dashboard load times."
        ),
        "metrics": [
            {"label": "Dashboard Speed", "val": "25-30% Faster"},
            {"label": "Output Handling", "val": "Python Automated"},
            {"label": "Analysis", "val": "SQL Execution Plans"}
        ],
        "tech_stack": ["SQL Stored Procedures", "Execution Plans", "Python", "T-SQL", "Query Profiling"],
        "category": "SQL Optimization",
        "icon": "zap"
    },
    {
        "id": "snowflake-automated-scd-tracker",
        "title": "Snowflake Automated SCD Type I & II Platform",
        "subtitle": "Historical Data Tracking • MERGE Semantics • Audit Compliance",
        "description": (
            "Designed and deployed an automated Slowly Changing Dimension (SCD Type I and II) framework on Snowflake for historical "
            "records across business teams. Implemented Snowflake MERGE logic, clustering keys, and audit timestamps, reducing "
            "manual maintenance effort by 90%."
        ),
        "metrics": [
            {"label": "Manual Effort", "val": "-90% Reduced"},
            {"label": "Audit Traceability", "val": "100% Verified"},
            {"label": "Warehouse", "val": "Snowflake"}
        ],
        "tech_stack": ["Snowflake SQL", "PySpark", "MERGE Logic", "Dimensional Modeling"],
        "category": "Snowflake & Warehousing",
        "icon": "git-commit"
    },
    {
        "id": "aws-athena-s3-lakehouse",
        "title": "Serverless S3 Lakehouse & Athena Query Optimization",
        "subtitle": "Amazon S3 Data Lake • AWS Glue Catalog • Serverless Athena SQL",
        "description": (
            "Engineered serverless analytics infrastructure over Amazon S3 using AWS Glue Data Catalog and AWS Athena. "
            "Implemented intelligent partition pruning strategies and columnar Parquet data structures, cutting query "
            "scan sizes and execution times by ~25-30%."
        ),
        "metrics": [
            {"label": "Query Latency", "val": "-25-30% Faster"},
            {"label": "Query Engine", "val": "AWS Athena"},
            {"label": "Data Catalog", "val": "AWS Glue"}
        ],
        "tech_stack": ["AWS Athena", "Amazon S3", "AWS Glue Catalog", "SQL", "Parquet"],
        "category": "AWS Data Engg",
        "icon": "database"
    },
    {
        "id": "python-data-validation-automation",
        "title": "Python Ingestion & Automated Validation Pipelines",
        "subtitle": "Pre-Ingestion Cleansing • Boundary Verification • Automated Handling",
        "description": (
            "Built modular Python data-handling pipelines to automate multi-source data extraction, cleansing, and schema "
            "validation before loading into lakehouse and warehouse storage. Validates boundary limits, prunes anomalies, "
            "and handles stored procedure outputs seamlessly."
        ),
        "metrics": [
            {"label": "Data Quality", "val": "+25% Increase"},
            {"label": "Automation", "val": "100% Python"},
            {"label": "Ingestion Errors", "val": "Near Zero"}
        ],
        "tech_stack": ["Python", "SQL", "JSON Processing", "Data Cleansing", "Automation"],
        "category": "Python Automation",
        "icon": "shield-check"
    }
]

PIPELINE_STAGES = [
    {
        "step": "01. INGEST",
        "title": "Real-Time & Multi-Source Ingestion",
        "desc": "Ingesting high-velocity transactional and cash flow event streams via AWS Kinesis and multi-source feeds into an Amazon S3 centralized data lake.",
        "tech": "AWS Kinesis, Amazon S3, Python Ingestion Scripts, REST APIs"
    },
    {
        "step": "02. CATALOG & VALIDATE",
        "title": "Schema Discovery & Quality Gate",
        "desc": "Automated AWS Glue Data Catalog crawlers, schema enforcement, and Python data profiling scripts that prune anomalies and validate boundaries.",
        "tech": "AWS Glue Catalog, Python Data Validation, Schema Enforcement"
    },
    {
        "step": "03. TRANSFORM",
        "title": "Distributed Databricks & PySpark Processing",
        "desc": "Scalable PySpark processing on Databricks clusters and AWS Glue ETL with custom partitioning, Delta Lake, and SCD Type I/II versioning.",
        "tech": "Databricks, PySpark, AWS Glue ETL, Delta Lake, Azure Storage Mounts"
    },
    {
        "step": "04. WAREHOUSE",
        "title": "Multi-Warehouse Management & SCD Versioning",
        "desc": "Dedicated Snowflake virtual warehouses isolating compute for distinct business teams (Lazard Inc.), with automated SCD I & II historical tracking.",
        "tech": "Snowflake Virtual Warehouses, Clustering Keys, MERGE Logic"
    },
    {
        "step": "05. OPTIMIZE & SERVE",
        "title": "SQL Execution Plans & Fast Dashboards",
        "desc": "Serverless Athena SQL over S3, tuned SQL Stored Procedures analyzed via query execution plans, and Python output handlers powering executive dashboards.",
        "tech": "AWS Athena, SQL Stored Procedures, Execution Plans, Python Handlers"
    }
]
