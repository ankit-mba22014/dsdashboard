import streamlit as st
import pandas as pd
import datetime as dt

st.set_page_config(page_title="Dark Store Efficiency Dashboard", layout="wide")

st.title("🏬 Dark Store Efficiency Dashboard")

# ✅ Load data from GitHub raw links
picker_data_url = "https://raw.githubusercontent.com/ankit-mba22014/dsdashboard/main/picker_productivity.csv"
sku_data_url = "https://raw.githubusercontent.com/ankit-mba22014/dsdashboard/main/top_skus.csv"
low_stock_url = "https://raw.githubusercontent.com/ankit-mba22014/dsdashboard/main/low_stock_skus.csv"
sku_locations_url = "https://raw.githubusercontent.com/ankit-mba22014/dsdashboard/main/sku_locations.csv"
guided_path_url = "https://raw.githubusercontent.com/ankit-mba22014/dsdashboard/main/guided_pick_path.csv"

# Load CSVs
picker_data = pd.read_csv(picker_data_url)
sku_df = pd.read_csv(sku_data_url)
low_stock_skus = pd.read_csv(low_stock_url)
sku_locations = pd.read_csv(sku_locations_url)
guided_path = pd.read_csv(guided_path_url)

# Sidebar filters (dummy for now)
st.sidebar.header("🔍 Filters")
selected_store = st.sidebar.selectbox("Select Store", ['Store A', 'Store B', 'Store C'])
date_range = st.sidebar.date_input("Select Date Range", [dt.date.today() - dt.timedelta(days=7), dt.date.today()])

# Sample simulated KPIs (static for now)
total_orders = picker_data['Orders Picked'].sum()
pending_dispatch = 65
avg_pick_time = picker_data['Avg Pick Time (min)'].mean().round(2)
sla_breach_pct = 5.2  # Static for demo

# KPI Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("📦 Total Orders", f"{total_orders}")
col2.metric("🕒 Avg Pick Time (min)", f"{avg_pick_time}")
col3.metric("🚦 SLA Breach %", f"{sla_breach_pct}%")
col4.metric("📬 Pending Dispatch", f"{pending_dispatch}")

st.markdown("---")

# Picker Productivity Table
st.subheader("👷 Picker Productivity")
picker_data['Orders/Hour'] = (picker_data['Orders Picked'] / picker_data['Shift Hours']).round(2)
st.dataframe(picker_data, use_container_width=True)

st.markdown("---")

# Top Picked SKUs Bar Chart
st.subheader("🔥 Top 10 Picked SKUs")
st.bar_chart(sku_df.set_index('SKU'))

st.markdown("---")

# Inventory Alerts
st.subheader("📊 Inventory Alerts")
st.warning("⚠️ The following SKUs are low in stock:")
st.dataframe(low_stock_skus, use_container_width=True)

st.markdown("---")

# Guided Picking Path for Incoming Order
st.subheader("🚀 Guided Pick Path for Incoming Order")
st.dataframe(guided_path, use_container_width=True)

st.markdown("---")

st.caption(f"Last updated: {dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
