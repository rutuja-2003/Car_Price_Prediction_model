import streamlit as st
import pandas as pd
import pickle

# ==========================================================
# Load Models and Dataset
# ==========================================================
lr = pickle.load(open("LinearRegressionModel.pkl", "rb"))
dt = pickle.load(open("DecisionTreeModel.pkl", "rb"))
rf = pickle.load(open("RandomForestModel.pkl", "rb"))

car = pd.read_csv("Cleaned_Car_data.csv")

# ==========================================================
# Streamlit UI
# ==========================================================
st.set_page_config(page_title="Car Price Prediction", page_icon="🚗", layout="wide")

st.title("🚗 Car Price Prediction")
st.markdown("Welcome! Enter car details in the sidebar and get instant price predictions. "
            "You can also explore model performance metrics in the tabs below.")

# Sidebar title
st.sidebar.markdown("<h2 style='margin-top:0;'>🚘 Car Price Predictor</h2>", unsafe_allow_html=True)

# Logo with reduced size
st.sidebar.image("car_logo.jpg")

# Custom CSS for centering and rounding the image
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 50%;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.sidebar.header("🔧 Enter Car Details")

companies = sorted(car["company"].unique())
company = st.sidebar.selectbox("Company", companies)

# Filter models based on selected company
models_for_company = sorted(car[car["company"] == company]["name"].unique())
car_model = st.sidebar.selectbox("Car Model", models_for_company)

years = sorted(car["year"].unique(), reverse=True)
fuel_types = car["fuel_type"].unique()

year = st.sidebar.selectbox("Year", years)
fuel_type = st.sidebar.selectbox("Fuel Type", fuel_types)
kms_driven = st.sidebar.number_input("Kilometers Driven", min_value=0, max_value=400000, step=1000)


# Choose model
model_choice = st.sidebar.radio("Choose Model", ["Linear Regression", "Decision Tree", "Random Forest"])

# ==========================================================
# Tabs for Prediction & Comparison
# ==========================================================
tab1, tab2 = st.tabs(["🔮 Prediction", "📊 Model Comparison"])

with tab1:
    st.subheader("Car Price Prediction")
    if st.sidebar.button("Predict Price"):
        input_df = pd.DataFrame(
            [[car_model, company, int(year), int(kms_driven), fuel_type]],
            columns=["name","company","year","kms_driven","fuel_type"]
        )

        if model_choice == "Linear Regression":
            prediction = lr.predict(input_df)[0]
        elif model_choice == "Decision Tree":
            prediction = dt.predict(input_df)[0]
        else:
            prediction = rf.predict(input_df)[0]

        st.success(f"Estimated Price ({model_choice}): ₹ {int(prediction):,}")

        # Show input summary in columns
        col1, col2 = st.columns(2)
        with col1:
            st.write("**Company:**", company)
            st.write("**Model:**", car_model)
        with col2:
            st.write("**Year:**", year)
            st.write("**Fuel Type:**", fuel_type)
            st.write("**Kms Driven:**", kms_driven)

with tab2:
    st.subheader("📊 Model Performance Comparison")

    # Show metrics side by side
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Linear Regression R²", value="-0.091")
        st.metric(label="MAE", value="188,346")
        st.metric(label="RMSE", value="465,385")
    with col2:
        st.metric(label="Decision Tree R²", value="0.174")
        st.metric(label="MAE", value="184,446")
        st.metric(label="RMSE", value="404,749")
    with col3:
        st.metric(label="Random Forest R²", value="0.047")
        st.metric(label="MAE", value="187,173")
        st.metric(label="RMSE", value="434,783")

    st.markdown("---")
    st.info(
        "🏆 **Best Model: Decision Tree**\n\n"
        "- ✅ Highest R² score (≈0.17), meaning it explains more variance in car prices.\n"
        "- ✅ Lowest RMSE, showing smaller prediction errors compared to others.\n"
        "- 🔄 Captures complex, non‑linear relationships between features (brand, year, fuel type) and price.\n"
        "- ⚖️ Random Forest performed moderately but didn’t generalize as well on this dataset.\n"
        "- ❌ Linear Regression struggled because car prices don’t follow a simple straight line trend.\n\n"
        "👉 In short, the Decision Tree is the most reliable choice for your dataset."
    )



# Highlight the best model
st.sidebar.markdown("---")
st.sidebar.info("🏆 **Best Model: Decision Tree**\n\nIt achieved the highest R² score (≈0.17) and lowest error values, meaning it predicts car prices more accurately than the others.")

# Footer
st.markdown("---")
st.markdown("Project by Rutuja ❤️")
