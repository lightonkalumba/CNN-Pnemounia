import streamlit as st
import joblib

# Load the trained model from the saved file
model = joblib.load("C:\\Users\\kalum\\decision_tree_models.pkl")

# Create a Streamlit app
st.title("Cheapest Food Item Predictor")

# Input fields for the user
product_options = [
    "Apple",
    "Milk",
    "Bread",
    "Chicken",
    "Pasta",
    "Yogurt",
    "Eggs",
    "Banana",
    "Cereal",
    "Orange Juice",
]
category_options = [
    "Fruit",
    "Dairy",
    "Bakery",
    "Meat",
    "Pasta",
    "Breakfast",
    "Beverages",
]

product = st.selectbox("Product", product_options)
category = st.selectbox("Category", category_options)  # Fixed the variable name

# Convert user input to numeric values
product_mapping = {
    "Apple": 0,
    "Milk": 1,
    "Bread": 2,
    "Chicken": 3,
    "Pasta": 4,
    "Yogurt": 5,
    "Eggs": 6,
    "Banana": 7,
    "Cereal": 8,
    "Orange Juice": 9,
}

product_code = product_mapping[product]

# Create a mapping for categories if needed
category_mapping = {
    "Fruit": 0,
    "Dairy": 1,
    "Bakery": 2,
    "Meat": 3,
    "Pasta": 4,
    "Breakfast": 5,
    "Beverages": 6,
}

category_code = category_mapping[category]

# Predict the price for all shops
shop_prices = {
    "A": model.predict([[product_code, category_code, 0]])[0],
    "B": model.predict([[product_code, category_code, 1]])[0],
    "C": model.predict([[product_code, category_code, 2]])[0],
}

# Find the shop with the lowest price
cheapest_shop = min(shop_prices, key=shop_prices.get)

# Display the recommended shop with the cheapest price and the predicted price
st.write(
    f"The recommended shop for {product} ({category}) is: Shop {cheapest_shop} with the lowest price."
)
st.write(f"The predicted price is: ${shop_prices[cheapest_shop]:.2f}")
