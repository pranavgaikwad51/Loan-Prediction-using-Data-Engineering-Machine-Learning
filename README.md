# 🏦 BigMart Sales Prediction App

## 📘 Overview

The **BigMart Sales Prediction App** is a **Streamlit-based Machine Learning project** that predicts item outlet sales for retail stores. This app leverages **data-driven insights** to assist in financial forecasting and inventory planning, enabling businesses to make smart, AI-powered decisions.

---

## 🎯 Problem Statement

Retail chains often face challenges in forecasting product sales due to multiple influencing factors such as item type, visibility, outlet size, and location.
This app uses a trained **scikit-learn regression model** to predict sales based on these variables, helping store managers plan inventory and pricing strategies efficiently.

---

## 🧠 Objective

To build a **robust and interactive web app** that:

* Takes product and outlet details as inputs
* Predicts the expected sales using a machine learning model
* Provides a simple and intuitive UI for business decision-makers

---

## 🧮 Dataset

The dataset used for training is derived from the **BigMart Sales Data**, which includes:

* Product features (Item type, weight, visibility, MRP, etc.)
* Outlet details (Location, size, age, type)
* Target variable: `Item_Outlet_Sales`

---

## 🛠️ Tools & Libraries

* **Python**
* **Streamlit**
* **scikit-learn**
* **Pandas**
* **NumPy**
* **Pickle**

---

## 🤉 Model Architecture

The model was built using scikit-learn’s regression algorithms.
After comparing multiple models, the best-performing one was selected and saved as a `.pkl` file (`bigmart_best_model.pkl`) for deployment.

The app dynamically loads the model and predicts sales values based on real-time user input.

---

## ⚙️ Data Preprocessing

* Missing value imputation
* Encoding categorical features
* Feature scaling
* Splitting data into training and testing sets
* Model evaluation and tuning

---

## 📊 Evaluation Metrics

Model performance was evaluated using:

* **Mean Absolute Error (MAE)**
* **Mean Squared Error (MSE)**
* **R² Score**

---

## 🚀 Deployment

The app is deployed live using **Streamlit Cloud** and can be accessed here:

🔗 **Live App:** [BigMart Sales Prediction](https://loan-prediction-using-data-engineering-machine-learning--pranav.streamlit.app/)

---

## 💻 Usage

1. Visit the [Streamlit App](https://loan-prediction-using-data-engineering-machine-learning--pranav.streamlit.app/).
2. Enter product and outlet details (Item Weight, MRP, Outlet Type, etc.).
3. Click **“Predict Sales”** to view the predicted sales value.
4. The result will appear as an estimated financial forecast for the entered product.

---

## 📧 Contact & Developer Info

**👨‍💻 Developer:** Pranav Gaikwad
**📞 Phone:** +91 7028719844
**📧 Email:** [gaikwadpranav988@gmail.com](mailto:gaikwadpranav988@gmail.com)
**🔗 LinkedIn:** [linkedin.com/in/pranav-gaikwad-0b94032a](https://www.linkedin.com/in/pranav-gaikwad-0b94032a)
**🌐 GitHub:** [github.com/pranavgaikwad51](https://github.com/pranavgaikwad51)

---

## 🪙 Acknowledgements

Special thanks to:

* **BigMart Dataset Providers**
* **Streamlit Community** for their open-source contributions
* **scikit-learn team** for providing powerful machine learning tools

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use, modify, and share with attribution.
