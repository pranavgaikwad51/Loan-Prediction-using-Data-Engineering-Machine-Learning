import streamlit as st
import pandas as pd
import pickle

# === Load Model and Version Info from Pickle =====
with open("bigmart_best_model.pkl", "rb") as f:
    model, sklearn_version = pickle.load(f)

# === Page Configuration ===
st.set_page_config(
    page_title="BigMart Sales Prediction App",
    page_icon="💰",
    layout="wide",
)

# === Sidebar (Developer Info) =====
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2331/2331944.png", width=120)  # finance icon-----
    st.markdown(
        """
        <h2 style='text-align:center; color:#1E90FF;'>📊 Developer Info</h2>
        <hr style='border:1px solid #1E90FF;'>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        **👨‍💻 Name:** Pranav Gaikwad  
        **🎯 Role:** Student | Aspiring AI Engineer  
        **💼 Focus:** Data Science & AI in Finance  
        ---
        **📧 Email:** [gaikwadpranav988@gmail.com](mailto:gaikwadpranav988@gmail.com)  
        **🌐 GitHub:** [github.com/pranavgaikwad51](https://github.com/pranavgaikwad51)  
        **🔗 LinkedIn:** [linkedin.com/in/pranav-gaikwad-0b94032a](https://www.linkedin.com/in/pranav-gaikwad-0b94032a)  
        ---
        <p style='color:gray; font-size:13px;'>“Turning Data into Smart Financial Insights.”</p>
        """,
        unsafe_allow_html=True
    )

# === Main App Header ===
st.title("💼 BigMart Sales Prediction App")
st.markdown(
    f"<p style='color:gray;'>Powered by <b>scikit-learn v{sklearn_version}</b> | Predicting retail sales with precision 📈</p>",
    unsafe_allow_html=True
)

# === Input Form ===
st.markdown("---")
st.header("🧾 Enter Product & Outlet Details")

col1, col2 = st.columns(2)

with col1:
    Item_Identifier = st.text_input("Item Identifier", "FDA15")
    Item_Weight = st.number_input("Item Weight", min_value=0.0, value=12.5)
    Item_Fat_Content = st.selectbox("Item Fat Content", ["Low Fat", "Regular"])
    Item_Visibility = st.slider("Item Visibility", min_value=0.0, max_value=0.3, step=0.01, value=0.1)
    Item_Type = st.selectbox("Item Type", [
        "Dairy", "Soft Drinks", "Meat", "Fruits and Vegetables", "Household",
        "Baking Goods", "Snack Foods", "Frozen Foods", "Breakfast", 
        "Health and Hygiene", "Hard Drinks", "Canned", "Breads", 
        "Starchy Foods", "Others", "Seafood"
    ])

with col2:
    Item_MRP = st.number_input("Item MRP", min_value=0.0, value=150.0)
    Outlet_Identifier = st.selectbox("Outlet Identifier", [
        "OUT027", "OUT013", "OUT049", "OUT035", "OUT046", 
        "OUT017", "OUT045", "OUT018", "OUT019", "OUT010"
    ])
    Outlet_Size = st.selectbox("Outlet Size", ["Small", "Medium", "High"])
    Outlet_Location_Type = st.selectbox("Outlet Location Type", ["Tier 1", "Tier 2", "Tier 3"])
    Outlet_Type = st.selectbox("Outlet Type", [
        "Supermarket Type1", "Supermarket Type2", 
        "Supermarket Type3", "Grocery Store"
    ])
    Outlet_Age = st.slider("Outlet Age (Years)", 0, 40, 15)

# === Predict Button ===
st.markdown("---")
if st.button("🚀 Predict Sales", use_container_width=True):
    input_df = pd.DataFrame([{
        "Item_Identifier": Item_Identifier,
        "Item_Weight": Item_Weight,
        "Item_Fat_Content": Item_Fat_Content,
        "Item_Visibility": Item_Visibility,
        "Item_Type": Item_Type,
        "Item_MRP": Item_MRP,
        "Outlet_Identifier": Outlet_Identifier,
        "Outlet_Size": Outlet_Size,
        "Outlet_Location_Type": Outlet_Location_Type,
        "Outlet_Type": Outlet_Type,
        "Outlet_Age": Outlet_Age
    }])

    # Make prediction
    prediction = model.predict(input_df)[0]

    st.success(f"💰 **Predicted Item Outlet Sales:** ₹{prediction:,.2f}")

    st.markdown(
        "<p style='color:green;'>This prediction helps in financial forecasting and retail decision-making.</p>",
        unsafe_allow_html=True
    )

# === Footer ===
st.markdown("---")
st.markdown(
    """
    <div style='text-align:center; color:gray;'>
    © 2025 <b>Pranav Gaikwad</b> | BigMart Sales Predictor | AI & Finance 💹
    </div>
    """,
    unsafe_allow_html=True
)
