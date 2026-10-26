
from pathlib import Path
import sqlite3

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "data" / "processed" / "online_retail.db"

with sqlite3.connect(DB_PATH) as connection:
    total_rows = connection.execute(
        "SELECT COUNT(*) FROM online_retail"
    ).fetchone()[0]

    date_range = connection.execute(
        """
        SELECT MIN(InvoiceDate), MAX(InvoiceDate)
        FROM online_retail
        """
    ).fetchone()

    preview = connection.execute(
        """
        SELECT InvoiceNo, Description, Quantity, UnitPrice, Country
        FROM online_retail
        LIMIT 10
        """
    ).fetchall()

print(f"Total rows: {total_rows:,}")
print(f"First transaction date: {date_range[0]}")
print(f"Last transaction date: {date_range[1]}")

print("\nFirst 10 records:")
for row in preview:
    print(row)


print("\nMonthly Sales Analysis:")

with sqlite3.connect(DB_PATH) as connection:
    query = """
    SELECT
        strftime('%Y-%m', InvoiceDate) AS sales_month,
        COUNT(DISTINCT InvoiceNo) AS total_orders,
        ROUND(SUM(Quantity * UnitPrice), 2) AS total_revenue,
        SUM(Quantity) AS units_sold
    FROM online_retail
    WHERE Quantity > 0
      AND UnitPrice > 0
    GROUP BY strftime('%Y-%m', InvoiceDate)
    ORDER BY sales_month;
    """

    for row in connection.execute(query):
        print(row)

print("\nTop 10 Products by Revenue:")

with sqlite3.connect(DB_PATH) as connection:
    query = """
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
    """

    for row in connection.execute(query):
        print(row)

print("\nInvestigation: PAPER CRAFT, LITTLE BIRDIE")

with sqlite3.connect(DB_PATH) as connection:
    query = """
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
    """

    for row in connection.execute(query):
        print(row)

print("\nInvestigation: Entire Invoice 581483")

with sqlite3.connect(DB_PATH) as connection:
    query = """
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
    """

    for row in connection.execute(query):
        print(row)

print("\nImpact of the Unusual Transaction")

with sqlite3.connect(DB_PATH) as connection:
    query = """
    SELECT
        'All transactions' AS dataset,
        ROUND(SUM(Quantity * UnitPrice), 2) AS total_revenue,
        SUM(Quantity) AS total_units
    FROM online_retail
    WHERE Quantity > 0
      AND UnitPrice > 0

    UNION ALL

    SELECT
        'Excluding unusual transaction' AS dataset,
        ROUND(SUM(Quantity * UnitPrice), 2) AS total_revenue,
        SUM(Quantity) AS total_units
    FROM online_retail
    WHERE Quantity > 0
      AND UnitPrice > 0
      AND NOT (
          InvoiceNo = '581483'
          AND StockCode = '23843'
      );
    """

    for row in connection.execute(query):
        print(row)

print("\nTop 10 Products by Revenue (Adjusted Ranking)")

with sqlite3.connect(DB_PATH) as connection:
    query = """
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
    """

    for row in connection.execute(query):
        print(row)

print("\nTop 10 Countries by Revenue")

with sqlite3.connect(DB_PATH) as connection:
    query = """
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
    """

    for row in connection.execute(query):
        print(row)

print("\nAverage Order Value by Country")

with sqlite3.connect(DB_PATH) as connection:
    query = """
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
    """

    for row in connection.execute(query):
        print(row)

print("\nCustomer Revenue Concentration")

with sqlite3.connect(DB_PATH) as connection:
    query = """
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
    """

    for row in connection.execute(query):
        print(row)