#  Online Retail Sales Analysis

**Tools:** Python, SQL (MySQL), Pandas, Matplotlib, Seaborn  
**Dataset:** [UCI Online Retail Dataset](https://archive.ics.uci.edu/ml/datasets/online+retail)  
**Period Covered:** December 2010 – December 2011  
**Rows:** ~54,910 transactions  
**Languages:** SQL, Python

---

## Project Overview

This project analyzes real transactional data from a UK-based online retailer with the goal of:

- Identifying high-performing products and revenue patterns  
- Understanding seasonal demand fluctuations  
- Segmenting product performance by country  
- Making business recommendations for inventory, sales, and marketing strategies

---

##  Deliverables

- 🧮 [SQL Queries & Schema Design](Scripts/)
- 🐍 [Python Scripts](Scripts/)
- 📈 [Charts & Visualizations](Charts/)
- 📄 [Detailed Report (PDF)](OnlineRetail_Report.pdf)

---

##  Approach

- **Data Cleaning:** Cleaned the raw data in Python for missing values, negative quantities/prices, canceled invoices, and outliers  
- **SQL Analysis:** Created relational schema in MySQL with tables for customers, products, invoices, and orders  
- **Python Analysis:** Used Pandas, Matplotlib, and Seaborn to explore trends and create visualizations  

---

##  Key Findings

### 1.  Top Products & Seasonal Demand

- Core products show consistent demand across the year  
- Some products experienced **significant sales spikes**, indicating seasonality or promotions:
  - *Medium Ceramic Storage Jar* in January
  - *Picnic Basket* in June
  - *Rabbit Night Light* in October–November
  - *Paper Craft, Little Birdie* in December

### 2.  Regional Sales Differences

- UK dominates sales (~£374k from top 3 products)  
- There are clear regional differences in product demand

### 3.  Product Strategy

- Some items deliver high revenue despite low unit sales (high margin)  
- Others are high in volume but lower in price (low margin)

---

##  Business Recommendations

###  Inventory Planning

- Ensure top-selling products are available consistently  
- Track and plan for seasonal spikes in demand

###  Product Strategy

- Promote high-margin products strategically  
- Consider bundling low-margin, high-volume items

###  Marketing Strategy

- Tailor campaigns by country based on product popularity  
- Reassess Q4 strategies to better capture holiday season sales

---

##  Visual Insights

Charts created in Python using Seaborn & Matplotlib:

-  Monthly revenue trends (Top 10 products)  
-  Top products by quarter (Revenue & Quantity)  
-  Top products overall (Revenue vs. Quantity)  
-  Top 3 products by country

 All charts are saved in the [`Charts/`](Charts/) folder.

---

##  Skills Demonstrated

- **SQL:** Joins, aggregations, segmentation queries  
- **Python:** Data cleaning with Pandas, data visualization with Seaborn & Matplotlib  
- **Business Analysis:** Extracting actionable insights from transactional data  
- **Data Storytelling:** Communicating findings through narrative and visuals

---

##  Final Summary

This analysis revealed consistent top-selling products and several seasonal demand spikes. Regional differences in product popularity highlight opportunities for targeted marketing and inventory optimization. Combining SQL and Python enabled deep, flexible insights that inform practical business strategies.

