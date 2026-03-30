import streamlit as st

st.set_page_config(page_title="超級計算機", page_icon="🧮")

st.title("我的 Python 互動小工具 🛠️")

# 1. 簡單的問候
name = st.text_input("請輸入你的名字：")
if name:
    st.success(f"歡迎光臨，{name}！")

# 2. 數值運算
st.subheader("隨身計算機")
num1 = st.number_input("輸入第一個數字", value=10)
num2 = st.number_input("輸入第二個數字", value=20)
st.write(f"兩個數字相加的結果是： **{num1 + num2}**")

# 3. 顏色挑選器
st.subheader("調色盤測試")
color = st.color_picker("選一個你喜歡的顏色", "#00f900")
st.write(f"你選擇的顏色代碼是： `{color}`")

# 4. 慶祝按鈕
if st.button("完成開發！點我慶祝"):
    st.balloons()
    st.snow() # 除了氣球，還會下雪喔！