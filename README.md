# 🏬 Dark Store Efficiency Dashboard

A Streamlit-based analytics dashboard for monitoring and optimizing operations inside dark stores, focused on picker productivity, SKU demand, inventory alerts, and guided picking paths.

---

## 🚀 Features

- **Order & Picker Metrics**: Total orders, SLA breaches, average pick times, and picker-wise productivity.
- **Top SKUs Visualization**: Bar chart showing most frequently picked items.
- **Inventory Alerts**: Low-stock SKU warnings for proactive replenishment.
- **Guided Picking Path**: Optimized SKU path for pickers based on location and sequence.
- **Location-Aware SKU Management**: Each SKU mapped to aisle/rack/shelf layout.

---

## 📁 Files

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit app script |
| `picker_productivity.csv` | Picker performance data |
| `top_skus.csv` | Top picked SKUs |
| `low_stock_skus.csv` | Low inventory alert list |
| `sku_locations.csv` | SKU locations in store (aisle/rack/shelf) |
| `guided_pick_path.csv` | Ordered picking path for incoming order |

---

## 🔗 Live Demo

Deploy using [Streamlit Cloud](https://streamlit.io/cloud):

1. Fork this repo.
2. Go to Streamlit Cloud → New App → Connect your GitHub → Select `app.py`.
3. Click “Deploy”.

Check the deployed verison [Dark Store Dashbboard](https://dsmindashboard.streamlit.app/)

---

## 🛠 Tech Stack

- **Streamlit** – UI framework
- **Pandas** – Data manipulation
- **CSV** – Lightweight data source (can be replaced with DB/API)

---

## ✅ Future Improvements

- ✅ Filter by picker or SKU
- ✅ Real-time API integration
- ✅ Visual store map with route overlay
- ✅ Historical trends & exportable reports

---

## 👨‍💼 Use Case

Ideal for **Program Managers**, **Ops Leaders**, and **Q-Commerce teams** seeking visibility and control across multiple dark stores.

---

## 📬 Contact

Built by [@ankit-mba22014](https://github.com/ankit-mba22014)

