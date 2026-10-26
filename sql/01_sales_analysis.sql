SELECT
    COUNT(*) AS total_rows
FROM online_retail;

SELECT
    InvoiceNo,
    StockCode,
    Description,
    Quantity,
    InvoiceDate,
    UnitPrice,
    CustomerID,
    Country,
    Revenue,
    IsCancellation
FROM online_retail
LIMIT 10;

SELECT
    MIN(InvoiceDate) AS first_transaction,
    MAX(InvoiceDate) AS last_transaction
FROM online_retail;

-- Monthly sales analysis
SELECT
    strftime('%Y-%m', InvoiceDate) AS sales_month,
    COUNT(DISTINCT InvoiceNo) AS total_orders,
    SUM(Quantity * UnitPrice) AS total_revenue,
    SUM(Quantity) AS units_sold
FROM online_retail
WHERE Quantity > 0
  AND UnitPrice > 0
GROUP BY strftime('%Y-%m', InvoiceDate)
ORDER BY sales_month;

-- Top 10 products by revenue
SELECT
    StockCode,
    Description,
    SUM(Quantity) AS units_sold,
    ROUND(SUM(Quantity * UnitPrice), 2) AS total_revenue,
    COUNT(DISTINCT InvoiceNo) AS total_orders
FROM online_retail
WHERE Quantity > 0
  AND UnitPrice > 0
  AND Description IS NOT NULL
GROUP BY StockCode, Description
ORDER BY total_revenue DESC
LIMIT 10;

-- Investigate PAPER CRAFT, LITTLE BIRDIE
SELECT
    InvoiceNo,
    InvoiceDate,
    StockCode,
    Description,
    Quantity,
    UnitPrice,
    Quantity * UnitPrice AS line_revenue,
    Country
FROM online_retail
WHERE StockCode = '23843'
  AND Quantity > 0
ORDER BY InvoiceDate;

-- Investigate the entire invoice containing the unusual quantity
SELECT
    InvoiceNo,
    InvoiceDate,
    StockCode,
    Description,
    Quantity,
    UnitPrice,
    ROUND(Quantity * UnitPrice, 2) AS line_revenue,
    Country
FROM online_retail
WHERE InvoiceNo = '581483'
ORDER BY line_revenue DESC;

-- Measure the impact of the unusual transaction
SELECT
    'All transactions' AS dataset,
    SUM(Quantity * UnitPrice) AS total_revenue,
    SUM(Quantity) AS total_units
FROM online_retail
WHERE Quantity > 0
  AND UnitPrice > 0

UNION ALL

SELECT
    'Excluding unusual transaction' AS dataset,
    SUM(Quantity * UnitPrice) AS total_revenue,
    SUM(Quantity) AS total_units
FROM online_retail
WHERE Quantity > 0
  AND UnitPrice > 0
  AND NOT (
      InvoiceNo = '581483'
      AND StockCode = '23843'
  );

-- Top 10 products by revenue, excluding non-merchandise
-- items and the unusual transaction
SELECT
    StockCode,
    Description,
    SUM(Quantity) AS units_sold,
    ROUND(SUM(Quantity * UnitPrice), 2) AS total_revenue,
    COUNT(DISTINCT InvoiceNo) AS total_orders
FROM online_retail
WHERE Quantity > 0
  AND UnitPrice > 0
  AND Description IS NOT NULL
  AND StockCode NOT IN ('DOT', 'POST', 'M')
  AND NOT (
      InvoiceNo = '581483'
      AND StockCode = '23843'
  )
GROUP BY StockCode, Description
ORDER BY total_revenue DESC
LIMIT 10;

-- 10. Sales performance by country
SELECT
    Country,
    COUNT(DISTINCT InvoiceNo) AS total_orders,
    SUM(Quantity) AS units_sold,
    ROUND(SUM(Quantity * UnitPrice), 2) AS total_revenue
FROM online_retail
WHERE Quantity > 0
  AND UnitPrice > 0
GROUP BY Country
ORDER BY total_revenue DESC
LIMIT 10;

-- Average order value by country
WITH country_orders AS (
    SELECT
        Country,
        InvoiceNo,
        SUM(Quantity * UnitPrice) AS order_revenue,
        CustomerID
    FROM online_retail
    WHERE Quantity > 0
      AND UnitPrice > 0
    GROUP BY Country, InvoiceNo
)
SELECT
    Country,
    COUNT(*) AS total_orders,
    COUNT(DISTINCT CustomerID) AS unique_customers,
    ROUND(SUM(order_revenue), 2) AS total_revenue,
    ROUND(AVG(order_revenue), 2) AS average_order_value
FROM country_orders
GROUP BY Country
HAVING COUNT(*) >= 20
ORDER BY average_order_value DESC
LIMIT 10;

-- 12. Revenue concentration among top customers
WITH customer_revenue AS (
    SELECT
        CustomerID,
        SUM(Quantity * UnitPrice) AS total_revenue
    FROM online_retail
    WHERE Quantity > 0
      AND UnitPrice > 0
      AND CustomerID IS NOT NULL
    GROUP BY CustomerID
),
ranked_customers AS (
    SELECT
        CustomerID,
        total_revenue,
        ROW_NUMBER() OVER (
            ORDER BY total_revenue DESC
        ) AS customer_rank
    FROM customer_revenue
)
SELECT
    COUNT(*) AS identified_customers,
    ROUND(SUM(total_revenue), 2) AS total_revenue,
    ROUND(SUM(CASE WHEN customer_rank <= 10
        THEN total_revenue ELSE 0 END), 2) AS top_10_revenue,
    ROUND(
        100.0 * SUM(CASE WHEN customer_rank <= 10
            THEN total_revenue ELSE 0 END)
        / SUM(total_revenue),
        2
    ) AS top_10_revenue_share_pct,
    ROUND(SUM(CASE WHEN customer_rank <= 20
        THEN total_revenue ELSE 0 END), 2) AS top_20_revenue,
    ROUND(
        100.0 * SUM(CASE WHEN customer_rank <= 20
            THEN total_revenue ELSE 0 END)
        / SUM(total_revenue),
        2
    ) AS top_20_revenue_share_pct
FROM ranked_customers;