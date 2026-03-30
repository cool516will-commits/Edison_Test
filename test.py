import streamlit as st

st.title("滷味店經營回本計算機 🍢")
st.write("輸入你的經營成本，幫你算出每日目標營業額！")

# --- 設定輸入區 ---
st.header("1. 固定成本 (每月)")
rent = st.number_input("每月房租", value=25000)
utilities = st.number_input("水電瓦斯預估", value=5000)
other_fixed = st.number_input("其他固定開銷 (如人事、雜支)", value=0)

st.header("2. 投資與回本")
transfer_fee = st.number_input("頂讓金 (投資總額)", value=200000)
target_months = st.number_input("預計幾個月要回本？", value=12)

st.header("3. 毛利與營運")
# 假設進貨 6000 元可以賣出的總金額
stock_cost = st.number_input("一次進貨成本 (元)", value=6000)
expected_sales = st.number_input("這批貨預計可賣出的營業額 (元)", value=15000)
days_per_month = st.number_input("每月工作天數", value=26)

# --- 計算邏輯 ---
# 毛利率 = (售價 - 成本) / 售價
if expected_sales > 0:
    margin = (expected_sales - stock_cost) / expected_sales
else:
    margin = 0.6 # 預設 60%

monthly_fixed_total = rent + utilities + other_fixed
monthly_amortization = transfer_fee / target_months if target_months > 0 else 0

# --- 顯示結果 ---
if st.button("開始計算"):
    st.divider()
    
    # 損益平衡點 (不含頂讓金)
    be_monthly = monthly_fixed_total / margin if margin > 0 else 0
    be_daily = be_monthly / days_per_month
    
    # 回本目標 (含頂讓金攤提)
    target_monthly = (monthly_fixed_total + monthly_amortization) / margin if margin > 0 else 0
    target_daily = target_monthly / days_per_month

    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("每日保本低消", f"{int(be_daily)} 元")
        st.caption("至少要賣這麼多，才付得起房租水電。")

    with col2:
        st.metric("每日回本目標", f"{int(target_daily)} 元")
        st.caption(f"每天賣這麼多，可在 {target_months} 個月內拿回頂讓金。")

    st.info(f"💡 目前計算毛利率為：{margin*100:.1f}%")
