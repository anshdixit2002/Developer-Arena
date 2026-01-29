import pandas as pd

# Day 1: Setup & Load Data
# ------------------------
# Read the CSV file (make sure 'sales_data.csv' is in the same directory)
df = pd.read_csv("C:\Users\dixit\Downloads\sales_data.csv")

# Day 2: Explore Data
# -------------------
print("First 5 rows of data:")
print(df.head(), "\n")

print("Basic info about the dataset:")
print(df.info(), "\n")

print("Dataset shape (rows, columns):", df.shape)
print("Column names:", df.columns.tolist(), "\n")

# Day 3: Clean Data
# -----------------
print("Missing values in each column before cleaning:")
print(df.isna().sum(), "\n")

# Example handling of missing values:
# For numeric columns, fill missing with column mean
numeric_cols = df.select_dtypes(include="number").columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# For non-numeric columns, fill missing with a placeholder
non_numeric_cols = df.select_dtypes(exclude="number").columns
df[non_numeric_cols] = df[non_numeric_cols].fillna("Unknown")

# Remove duplicate rows if any
df = df.drop_duplicates()

print("Missing values after cleaning:")
print(df.isna().sum(), "\n")

# Day 4: Analyze Sales
# --------------------
# NOTE: Adjust column names according to your CSV.
# Example expected columns:
# - 'Product'       : Product name
# - 'Quantity'      : Units sold
# - 'Price'         : Price per unit
# - 'Total_Sales'   : Total revenue per row (if not present, we compute it)

# If 'Total_Sales' column does not exist, create it as Quantity * Price
if "Total_Sales" not in df.columns:
    if {"Quantity", "Price"}.issubset(df.columns):
        df["Total_Sales"] = df["Quantity"] * df["Price"]
    else:
        raise ValueError("Columns 'Total_Sales' or ('Quantity' and 'Price') are required.")

# 1) Total Revenue
total_revenue = df["Total_Sales"].sum()

# 2) Average, Maximum, Minimum sales (per row)
avg_sale = df["Total_Sales"].mean()
max_sale = df["Total_Sales"].max()
min_sale = df["Total_Sales"].min()

# 3) Best-selling product by total revenue
if "Product" in df.columns:
    product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
    best_product = product_sales.idxmax()
    best_product_revenue = product_sales.max()
else:
    best_product = "N/A (no 'Product' column)"
    best_product_revenue = 0

# Day 5: Create Report (console output – you copy to analysis_report.md)
# ---------------------------------------------------------------------
print("===== SALES ANALYSIS REPORT =====")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Average Revenue per entry: ₹{avg_sale:,.2f}")
print(f"Maximum Revenue in a single entry: ₹{max_sale:,.2f}")
print(f"Minimum Revenue in a single entry: ₹{min_sale:,.2f}")
print("\nBest-selling product (by revenue):", best_product)
print(f"Revenue of best-selling product: ₹{best_product_revenue:,.2f}")

print("\nTop 5 products by revenue:")
if "Product" in df.columns:
    print(product_sales.head())
else:
    print("Cannot show product-wise breakdown (no 'Product' column).")