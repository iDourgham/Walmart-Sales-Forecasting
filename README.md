# Sales Forecasting for Walmart

<img src="images/Walmart.jpg" alt="Walmart" width="400"/>

====================================================================

This project focuses on a real-world time series forecasting challenge: predicting **weekly sales for a specific department within a Walmart dataset**. Utilizing historical sales data, the goal is to develop and evaluate a forecasting model that can accurately predict future weekly sales.

* * * * *

📊 Project Overview
-------------------

This repository contains the analysis and forecasting model for predicting weekly sales for **Department 2** from a cleaned Walmart dataset. The project follows a multi-step forecasting approach, aiming to provide robust predictions for future sales periods.

Key aspects of this project include:

-   **Target Variable:** Predicting `Weekly_Sales`.
-   **Data Filtering:** The analysis is strictly scoped to a single, assigned department, ensuring a focused and practical forecasting problem.
-   **Time Series Preparation:** Handling date and time features, and preparing the data for time series modeling.
-   **Multi-Step Forecasting:** Implementation of strategies (e.g., recursive single-step or direct multi-step) to predict sales for multiple future time periods.
-   **Model Development:** Building and evaluating a time series forecasting model tailored to the characteristics of the departmental sales data.
-   **Deployment:** Deployment of the forecasting model for practical use in the real world using streamlit.

* * * * *

🚀 Getting Started
------------------

To explore this project and run the analysis yourself, follow these steps:

1.  **Clone the Repository:**

    Bash

    ```
    git clone https://github.com/iDourgham/Walmart-Sales-Forecasting.git
    cd Walmart-Sales-Forecasting

    ```

2.  **Create a Virtual Environment (Recommended):**

    Bash

    ```
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate

    ```

3.  **Install Dependencies:** Install all the required libraries using pip. A `requirements.txt` file is usually included for this.

    Bash

    ```
    pip install -r requirements.txt

    ```

* * * * *

📊 Dataset
----------

This project utilizes a cleaned **Walmart sales dataset**. Each row represents weekly sales data, including:

-   **Date:** The week of the sales.
-   **Weekly_Sales:** The target variable to be predicted.
-   **Dept:** The department ID (this project focuses on a single, assigned department).
-   Other relevant features (e.g., `IsHoliday`, `Temperature`, `Fuel_Price`, `CPI`, `Unemployment`).

* * * * *

🛠️ Technologies Used
---------------------

-   **Python:** The core programming language.
-   **Pandas:** For efficient data manipulation and time series handling.
-   **NumPy:** For numerical operations.
-   **Matplotlib & Seaborn:** For data visualization and exploratory data analysis.
-   **Statsmodels / Scikit-learn / Prophet / Neural Prophet / SARIMAX / Auto ARIMA / XGBoost.**
-   **Deep Learning: LSTM / GRU / CNN / RNN.**
-   **Deployment:** Streamlit

