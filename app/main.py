import streamlit as st
import pandas as pd
from predict import predict_sales
import matplotlib.pyplot as plt  


st.title("🛒 Walmart Weekly Sales Forecasting")
st.markdown("Upload a CSV file with the required features to get sales predictions.")

# Sample format hint
st.markdown("Example format should include all model features except `Weekly_Sales` and `Date`.")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    try:
        input_df = pd.read_csv(uploaded_file)

        # 🧹 Clean unwanted index column if present
        if 'Unnamed: 0' in input_df.columns:
            input_df.drop(columns=['Unnamed: 0'], inplace=True)

        st.write("📊 Uploaded Data Preview:", input_df.head())

        predictions = predict_sales(input_df)
        st.write("📈 Predicted Weekly Sales:")
        st.write(pd.DataFrame({'Predicted_Weekly_Sales': predictions}))
    
    except Exception as e:
        st.error(f"❌ Error: {e}")



def plot_model(train, test, y_pred, model_name=""):
    plt.figure(figsize=(20,6))
    plt.title(f'Prediction of Weekly Sales Using {model_name}', fontsize=20)
    plt.plot(train, label='Train')
    plt.plot(test, label='Test')
    plt.plot(y_pred, label=f'Prediction of {model_name}')
    plt.legend(loc='best')
    plt.xlabel('Index', fontsize=14)
    plt.ylabel('Weekly Sales', fontsize=14)
    st.pyplot(plt)  # <-- This renders the plot in Streamlit
