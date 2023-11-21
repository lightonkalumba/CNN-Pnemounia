import streamlit as st
from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array

# Load the saved model
model_path = "C:\\Users\\kalum\\Downloads\\model.h5"
model = load_model(model_path)


# Function to preprocess image for prediction
def preprocess_image(image_data):
    img = load_img(image_data, target_size=(64, 64))
    img_array = img_to_array(img)
    img_array = img_array.reshape((1,) + img_array.shape)
    return img_array


# Streamlit app code
st.title("Pneumonia Prediction from X-ray Images")

uploaded_file = st.file_uploader("Choose a chest X-ray image...", type=["jpg", "png"])

if uploaded_file is not None:
    img_array = preprocess_image(uploaded_file)
    st.image(uploaded_file, caption="Uploaded X-ray Image", use_column_width=True)

    # Make prediction with the loaded model
    predictions = model.predict(img_array)

    # Display the prediction
    if predictions[0][0] > 0.5:
        st.write(f"Prediction: Pneumonia (Confidence: {predictions[0][0]:.2f})")
    else:
        st.write(f"Prediction: Normal (Confidence: {1 - predictions[0][0]:.2f})")
