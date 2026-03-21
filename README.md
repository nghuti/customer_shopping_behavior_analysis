# 🛍️ Customer Shopping Behavior Analysis

## 📌 Project Overview

This project analyzes the shopping behavior of customers based on the **Customer Shopping Behavior** dataset with 3,900 data rows. The goal is to explore shopping trends, segment customers, and generate valuable business insights for retail businesses.
> This project was completed as a Guided Project to practice Data Analyst skills including Python, SQL, and Power BI.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| ![Python](https://img.shields.io/badge/Python-3.14-blue) | Data cleaning and processing |
| ![Pandas](https://img.shields.io/badge/Pandas-3.0.1-green) | Data analysis and transformation |
| ![SQL Server](https://img.shields.io/badge/SQL%20Server-2019-red) | Data storage and querying |
| ![Power BI](https://img.shields.io/badge/Power%20BI-Desktop-yellow) | Data visualization and Dashboard |

---



## 🔄 Project Workflow

### Step 1 - Data Cleaning (Python)
- Read CSV file using Pandas
- Handle missing values using median per Category
- Standardize column names (lowercase, replace spaces with `_`)
- Create new `age_group` column using `pd.qcut()` into 4 age groups
- Convert `frequency_of_purchases` into number of days (`purchase_frequency_days`)
- Drop duplicate column (`promo_code_used`)
- Load cleaned data into SQL Server using SQLAlchemy


---

### Step 2 - Data Analysis (SQL Server)
Performed analytical queries including:
- Top 5 best-selling products and highest revenue products
- Revenue comparison by Shipping Type
- Subscribed vs non-subscribed customer spending analysis
- Top 3 products per Category using `ROW_NUMBER()`
- Customer segmentation into New / Returning / Loyal


---

### Step 3 - Data Visualization (Power BI)
Built a 3-page interactive Dashboard:

#### 📊 Page 1 - Overview
- KPIs: Number of Customers, Avg Purchase Amount, Avg Review Rating, Total Revenue
- Revenue and Sales distribution by Category and Age Group
- Subscription Status breakdown

#### 📦 Page 2 - Product Analysis
- KPIs: Best Seller, Highest Revenue Product, Best Rated Product, Avg Discount Rate
- Top 5 products by revenue and sales count
- Revenue distribution by Season and Location
- Sales distribution by Size

#### 👥 Page 3 - Customer Analysis
- KPIs: Total Customers, Avg Previous Purchases, Avg Purchase Frequency, Subscription Rate
- Customer segmentation: New / Returning / Loyal
- Spending analysis by Age Group and Gender
- Payment Method distribution

---

## 💡 Key Insights

| Insight | Detail |
|---|---|
| 🏆 **Best Seller** | **Blouse** is the top-selling and highest-revenue product |
| ⭐ **Best Rated** | **Jewelry** has the highest average review rating |
| 👥 **Loyal Customers** | **79%** of customers are Loyal (more than 15 purchases) |
| 💳 **Subscription** | Only **27%** of customers have an active subscription |
| 🌟 **Top Category** | **Clothing** leads in both revenue and sales volume |
| 👴 **Purchase Frequency** | **Senior** customers shop most frequently |
| 🏷️ **Discount Rate** | **41.91%** of orders were purchased with a discount |
| 🌤️ **Best Season** | **Fall** generates the highest revenue |
| 💰 **Spending** | **Adult** age group has the highest average spend |

---

## 📸 Dashboard Preview

### Page 1 - Overview
<img width="1213" height="702" alt="image" src="https://github.com/user-attachments/assets/0f3d33ca-4256-4976-9ba6-96e0dd666738" />


### Page 2 - Product Analysis
<img width="1208" height="696" alt="image" src="https://github.com/user-attachments/assets/0858dc37-4c9c-4c1e-81de-8a43d7ca6eda" />

### Page 3 - Customer Analysis
<img width="1211" height="704" alt="image" src="https://github.com/user-attachments/assets/867118f9-bccf-42d6-bcaf-0da4cae816e7" />

## 📜 License & Credits

This project is based on a guided project by **Amlan Mohanty**.  
Licensed under the [MIT License](LICENSE).

> This repository contains my own implementation, analysis, and dashboard  
> built upon the original guided project structure.
