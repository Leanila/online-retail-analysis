# SQL Analysis Report - Online Retail

## Project Overview

This report presents SQL-based analysis of the Online Retail dataset using SQLite. The analysis focuses on sales performance, product revenue, geographic distribution, average order value, and customer revenue concentration.

The database contains 536,641 cleaned transaction rows.

## 1. Monthly Sales Performance

- November 2011 was the strongest full month in the analyzed period, generating approximately £1.50 million in positive sales revenue across 2,769 invoices.
- Sales revenue increased during autumn 2011.
- December 2011 covers only the period through December 9 and should not be compared directly with complete months.

**Business implication:** Monthly reporting should account for incomplete periods to avoid misleading comparisons.

## 2. Top Products by Revenue

After excluding postage-related and manual transaction codes, as well as the investigated transaction for product `23843`, the leading product by revenue was `REGENCY CAKESTAND 3 TIER`, generating £174,156.54.

Other leading products included `WHITE HANGING HEART T-LIGHT HOLDER`, `PARTY BUNTING`, and `JUMBO BAG RED RETROSPOT`.

**Business implication:** Revenue, units sold, and order count should be reviewed together to understand product performance.

## 3. Geographic Sales Distribution

The United Kingdom generated approximately £9.00 million in positive sales revenue, representing about 84.6% of positive sales revenue across all countries.

The Netherlands, EIRE, Germany, and France were among the next-largest markets by revenue.

**Business implication:** The business is highly concentrated in the UK market. International markets may offer opportunities for further investigation.

## 4. Average Order Value by Country

Among countries with at least 20 invoices, the Netherlands had the highest average order value at £3,036.66, followed by Australia at £2,429.01.

These results may reflect larger orders or differences in customer purchasing patterns. Further analysis is needed before drawing conclusions about market potential.

## 5. Customer Revenue Concentration

Among customers with a known `CustomerID` and positive sales:

- Identified customers: 4,338
- Total revenue: £8,887,208.89
- Top 10 customers' revenue: £1,537,659.21 (17.30%)
- Top 20 customers' revenue: £2,125,228.46 (23.91%)

**Business implication:** The largest customers account for a meaningful share of identified-customer revenue. Customer retention and concentration should be monitored.

## Data Limitations

- Approximately 24.9% of cleaned rows have a missing `CustomerID`, limiting customer-level analysis.
- December 2011 is an incomplete month in the dataset.
- Positive-quantity and positive-price filters exclude returns and other negative-quantity transactions. The resulting revenue measures are not net revenue after returns or profit.
- Transaction `581483`, containing 80,995 units of product `23843`, was excluded from the adjusted product ranking for sensitivity analysis. The record was not removed from the database.
- Postage and manual codes were excluded from the adjusted product ranking, but not from every analysis.
- The average order value calculation uses positive transaction lines and may be affected by unusually large orders.

## Conclusion

The SQL analysis highlights the dominance of the UK market, identifies leading products, compares order values across countries, and quantifies revenue concentration among identified customers. The findings should be interpreted in light of missing customer identifiers, incomplete periods, and unusual transactions.
