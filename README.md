# Online Retail Data Analysis

## Project Overview

This project explores transactional data from an online retailer to identify sales trends, top-performing products, geographic sales patterns, and customer purchasing behavior.

The analysis includes data cleaning, exploratory data analysis (EDA), sales performance analysis, customer concentration analysis, and RFM customer segmentation.

## Business Objectives

- Analyze monthly sales trends and identify high-performing periods.
- Identify products generating the highest sales value.
- Compare sales performance across countries.
- Evaluate customer sales concentration.
- Segment customers based on recency, frequency, and monetary value.
- Develop data-driven recommendations for customer retention and sales growth.

## Dataset

The project uses the **Online Retail** dataset from the UCI Machine Learning Repository.

- Source: https://archive.ics.uci.edu/dataset/352/online+retail
- Period: December 2010 – December 2011
- Data type: Online retail transactions

## Tools and Technologies

- Python
- pandas
- NumPy
- Matplotlib
- Jupyter Notebook
- Excel

## Project Structure

- `data/` — source dataset and processed data
- `notebooks/` — data cleaning, exploration, and analysis
- `sql/` — SQL analysis
- `powerbi/` — Power BI files
- `reports/` — analytical report and visualizations

## Key Findings

- **Monthly sales:** November 2011 was the strongest full month, with approximately 1.50 million in sales value from positive-quantity transactions.
- **Product performance:** PAPER CRAFT, LITTLE BIRDIE was among the leading products by sales value and units sold.
- **Geographic distribution:** The United Kingdom accounted for approximately 84.6% of sales value.
- **Customer concentration:** The top 10 customers contributed approximately 17.3% of sales value among customers with an identified CustomerID.
- **RFM segmentation:** The Best Customers segment represented 30.24% of identified customers and contributed 72.88% of their sales value.

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

## Business Recommendations

- Explore loyalty initiatives and personalized offers for high-value customers.
- Test follow-up campaigns to encourage repeat purchases among recent customers.
- Evaluate targeted re-engagement campaigns for at-risk customers.
- Investigate opportunities to expand sales in markets outside the United Kingdom.

## Limitations

- The dataset covers a limited historical period.
- December 2011 contains data only through December 9.
- Customer-level analyses exclude transactions without a CustomerID.
- Sales value is not equivalent to profit.
- Analyses based on positive-quantity transactions do not deduct returns or cancellations.

## Author

Leanila Kavalevich
Junior Data Analyst