# 💊 Pharmacy Inventory Optimization Analysis

**Author:** Ioannis Michelis

## 📋 Project Overview

This project focuses on data-driven inventory management for a pharmacy setting. By analyzing a sample dataset of **301 product SKUs**, the goal is to optimize stock levels, identify sales patterns, and reduce the risk of stockouts, overstocking, and product expiration.

The project simulates a real pharmacy inventory problem where sales, stock levels, supplier lead times, and expiry dates are used to support better purchasing and stock control decisions.

## ❓ Business Question

Which pharmacy products require reordering, which are overstocked, and which are at risk of expiration based on sales, stock levels, supplier lead times, and expiry dates?

## 🛠 Tech Stack

- **Language:** Python
- **Libraries:** Pandas, Matplotlib
- **Data Format:** CSV

## 📁 Project Structure

```text
pharmacy-inventory-optimization/
│
├── README.md
├── analysis.py
├── pharmacy_inventory_sample.csv
├── requirements.txt
└── sales_distribution.png
```

## 📊 Dataset Description

The analysis was performed on a structured pharmacy inventory dataset containing **301 records**.

The dataset includes:

- **Product Name:** Name of each pharmacy or OTC product
- **Category:** Product classification
- **Sales Data:** Quantity sold over a selected period
- **Stock Level:** Current available inventory
- **Supplier:** Supplier information for reorder planning
- **Lead Time:** Estimated supplier delivery time
- **Expiration Date:** Product expiry tracking
- **Reorder Point:** Minimum stock level used to trigger replenishment decisions

## 🔍 Analysis Performed

The analysis focuses on four key inventory management areas:

1. **Inventory Velocity**
   - Products were categorized into fast-moving, medium-moving, and slow-moving groups based on sales activity.

2. **Reorder Identification**
   - Products with stock levels at or below the reorder point were flagged as requiring replenishment.

3. **Overstock Detection**
   - Products with high stock levels compared to sales were identified as potential overstock risks.

4. **Expiration Risk**
   - Products close to their expiration date were isolated to support proactive stock rotation, discounting, or priority sales.

## 📈 Key Results & Actionable Insights

- **Fast-moving products** can be prioritized for regular replenishment to prevent stockouts.
- **Slow-moving products** can be reviewed to avoid unnecessary purchasing and reduce capital tied up in inventory.
- **Overstocked items** can be monitored to prevent waste and improve cash flow.
- **Products near expiration** can be rotated, discounted, or promoted before they become unsellable.
- **Reorder thresholds** help support more consistent and data-driven supplier ordering decisions.

## 📊 Output / Visualization

The project includes a sales distribution chart:

```text
sales_distribution.png
```

This visualization helps show how sales volume is distributed across products and supports decisions around fast-moving and slow-moving inventory.

## 🚀 Installation & Usage

1. **Clone the repository:**

```bash
git clone https://github.com/Mioan37/pharmacy-inventory-optimization.git
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the analysis:**

```bash
python analysis.py
```

## 🎯 Business Value

By applying basic inventory analysis, a pharmacy can improve the balance between product availability and stock control.

This helps the business:

- Reduce stockouts for high-demand products
- Avoid overstocking slow-moving products
- Minimize expired stock and waste
- Improve supplier ordering decisions
- Support better customer service through improved product availability

## ✅ Skills Demonstrated

- Python data analysis
- CSV data handling
- Data cleaning and transformation
- Inventory performance analysis
- Pharmacy stock management logic
- Reorder and expiration risk identification
- Business insight generation
- Data visualization with Matplotlib
