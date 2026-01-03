# Vendor Performance Analysis 

## 📌 Project Overview
This project focuses on analyzing vendor performance using sales, purchase, pricing, and freight data to support data-driven procurement and inventory decisions. It demonstrates an end-to-end analytics workflow—from raw data ingestion to business insight generation—using Python, SQL, and SQLite.

---

## 🏢 Business Problem
Organizations often struggle to evaluate vendor effectiveness due to fragmented transactional data spread across multiple sources. Without a consolidated analytical view, procurement decisions can result in:
- Low profit margins  
- High freight costs  
- Poor inventory turnover  
- Inefficient vendor selection  

This project addresses these challenges by creating a unified, vendor-level performance dataset.

---

## 🎯 Project Objectives
- Build an automated data ingestion pipeline for raw CSV files  
- Consolidate multi-source transactional data into a relational database  
- Engineer key vendor performance metrics  
- Identify high-performing and underperforming vendors  
- Generate actionable business insights for decision-making  

---

## 🛠️ Tech Stack
- **Programming Language:** Python  
- **Libraries:** Pandas, Logging  
- **Database:** SQLite  
- **Querying:** SQL (CTEs, Joins, Aggregations)  
- **Tools:** Jupyter Notebook, Git  

---

## 🔄 Data Pipeline Workflow
1. Ingest raw CSV files into SQLite using Python  
2. Aggregate sales, purchase, and freight data using SQL CTEs  
3. Clean and preprocess data in Python  
4. Perform feature engineering and metric calculation  
5. Create a curated `vendor_sales_summary` analytical table  
6. Conduct Exploratory Data Analysis (EDA)  

---

## 📊 Key Business Metrics Engineered
- **Gross Profit** = Total Sales Dollars − Total Purchase Dollars  
- **Profit Margin (%)** = Gross Profit / Total Sales Dollars  
- **Stock Turnover** = Total Sales Quantity / Total Purchase Quantity  
- **Sales-to-Purchase Ratio** = Total Sales Dollars / Total Purchase Dollars  
- **Freight Cost Impact** on profitability  

---

## 🔍 Exploratory Data Analysis (EDA)
EDA was performed to:
- Analyze vendor-wise purchase and sales contribution  
- Identify profit margin distribution across vendors  
- Detect low stock turnover and overstocking risks  
- Highlight vendors with high freight cost impact  

---

## 💡 Key Insights
- A small subset of vendors contributes a majority of total purchase value  
- High purchase volume does not necessarily indicate high profitability  
- Several vendors exhibit low stock turnover, increasing inventory risk  
- Freight costs significantly reduce net profit for certain vendors  

---

## 📈 Business Recommendations
- Prioritize vendors with high profit margins and strong stock turnover  
- Renegotiate pricing with low-margin vendors  
- Optimize inventory levels to improve cash flow  
- Review and control freight-heavy vendor relationships  

---

## 📂 Project Structure
├── data/
├── ingestion_db.py
├── get_vendor_summary.py
├── exploratory data analysis.ipynb
├── vendor performance analysis.ipynb
├── inventory.db
└── logs/


---

## 🚀 Future Enhancements
- Power BI / Tableau dashboard integration  
- Migration to PostgreSQL or cloud databases  
- Automated pipeline scheduling (Airflow)  
- Predictive analytics for vendor risk scoring  

---

## ✅ What This Project Demonstrates
- Strong SQL querying and data modeling skills  
- Practical data engineering fundamentals  
- Business-focused analytical thinking  
- End-to-end project ownership and documentation  

---

## 📎 Author
**Gautam Mishra**  
Aspiring Data Analyst | Business Analyst  

