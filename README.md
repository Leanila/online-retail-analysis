# Online Retail Data Analysis

## Project Overview

This project analyzes transactional data from an online retailer to identify sales trends, top-performing products, geographic sales patterns, and customer purchasing behavior.

The project combines data cleaning, exploratory data analysis (EDA), SQL-based sales analysis, and RFM customer segmentation to derive actionable business insights.

## Business Objectives

- Analyze monthly sales trends and identify high-performing periods.
- Identify top-performing products by sales value.
- Compare sales performance across countries.
- Evaluate customer revenue concentration.
- Segment customers using Recency, Frequency, and Monetary (RFM) analysis.
- Develop data-driven recommendations for customer retention and sales growth.

## Dataset

The project uses the **Online Retail** dataset from the UCI Machine Learning Repository.

- **Source:** [UCI Online Retail Dataset](https://archive.ics.uci.edu/dataset/352/online+retail)
- **Period:** December 2010 – December 2011
- **Data type:** Online retail transactions
- **Cleaned dataset size:** 536,641 transaction rows

## Tools and Technologies

- **Python:** pandas, NumPy
- **Data visualization:** Matplotlib
- **SQL:** SQLite
- **Environment:** Jupyter Notebook
- **Version control:** Git and GitHub
- **Data source format:** Excel

## Project Structure

```text
online-retail-analysis/
├── data/                 # Local source and processed data (not committed)
├── notebooks/            # Data cleaning, EDA, and RFM analysis
├── sql/
│   ├── 01_sales_analysis.sql
│   ├── load_data_to_sqlite.py
│   └── run_sql_query.py
└── reports/
    ├── figures/          # Analysis visualizations
    ├── online_retail_analysis_report.md
    └── sql_analysis_report.md
```

## Key Findings

- **Monthly sales performance:** November 2011 was the strongest complete month, with approximately **£1.50 million** in sales value from transactions with positive quantities and unit prices.
- **Product performance:** After excluding postage, manual adjustment codes, and one unusual high-volume transaction from the product ranking, **REGENCY CAKESTAND 3 TIER** was the leading product by sales value, generating approximately **£174,157**.
- **Geographic distribution:** The United Kingdom accounted for approximately **84.6%** of sales value across transactions with positive quantities and unit prices.
- **Customer concentration:** The top 10 identified customers contributed approximately **17.3%** of sales value within the customer analysis.
- **RFM segmentation:** In the notebook's RFM analysis, the Best Customers segment represented **30.24%** of identified customers and contributed **72.88%** of customer sales value.

## Visualizations

### Monthly Sales Trends

![Monthly Sales Value](reports/figures/monthly_sales.png)

### Top Products by Sales Value

![Top Products by Sales Value](reports/figures/top_products_by_sales.png)

### Sales by Country

![Top Countries by Sales Value](reports/figures/top_countries_by_sales.png)

### Customer Segmentation

![Customer Distribution by RFM Segment](reports/figures/rfm_customer_distribution.png)

![Sales Contribution by RFM Segment](reports/figures/rfm_sales_share.png)

## SQL Analysis

SQL queries were executed against a local SQLite database created from the cleaned dataset.

The analysis covers:

- Monthly sales performance
- Top products by sales value
- Sales by country
- Average order value by country
- Customer revenue concentration

See the [SQL Analysis Report](reports/sql_analysis_report.md) for detailed results, methodology, and data limitations.

The database and datasets are kept locally and are not included in the repository.

## Business Recommendations

- Develop loyalty initiatives and personalized offers for high-value customers.
- Test follow-up campaigns to encourage repeat purchases.
- Investigate targeted re-engagement campaigns for at-risk customers.
- Explore opportunities to grow sales in international markets.
- Review unusually large transactions to understand their impact on product rankings and reported sales.

## Limitations

- The dataset covers a historical period from December 2010 to December 2011.
- December 2011 data ends on December 9, so the month is incomplete.
- Customer-level analyses exclude transactions without an identified `CustomerID`.
- Sales value is not equivalent to profit because product costs and operating expenses are not available.
- Analyses using positive quantities and positive unit prices do not deduct returns or cancellations.
- One unusually large transaction materially affects the ranking of products by sales value; it is retained in the data but excluded from the adjusted product ranking.
- RFM and SQL analyses may use different filters, so their totals are not directly interchangeable.

## Author

**Leanila Kavalevich**
Junior Data Analyst
