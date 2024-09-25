import streamlit as st
import numpy as np
import joblib

# Muat model
model = joblib.load('model.pkl')

# Judul aplikasi
st.title('Diamond Price Prediction App')

# Input dari pengguna
carat = st.number_input('Carat Weight', min_value=0.0, max_value=5.0, value=0.23)
cut = st.selectbox('Cut', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
color = st.selectbox('Color', ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
clarity = st.selectbox('Clarity', ['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'])
depth = st.slider('Depth Percentage', min_value=50.0, max_value=70.0, value=61.5)
table = st.slider('Table Percentage', min_value=40.0, max_value=80.0, value=55.0)
x = st.number_input('Length (x) in mm', min_value=0.0, max_value=10.0, value=3.95)
y = st.number_input('Width (y) in mm', min_value=0.0, max_value=10.0, value=3.98)
z = st.number_input('Height (z) in mm', min_value=0.0, max_value=10.0, value=2.43)

# Dictionary untuk mengonversi nilai kategori menjadi angka
cut_dict = {'Fair': 0, 'Good': 1, 'Very Good': 2, 'Premium': 3, 'Ideal': 4}
color_dict = {'D': 0, 'E': 1, 'F': 2, 'G': 3, 'H': 4, 'I': 5, 'J': 6}
clarity_dict = {'IF': 0, 'VVS1': 1, 'VVS2': 2, 'VS1': 3, 'VS2': 4, 'SI1': 5, 'SI2': 6, 'I1': 7}

# Kumpulkan fitur untuk prediksi
features = [carat, cut_dict[cut], color_dict[color], clarity_dict[clarity], depth, table, x, y, z]

# Fungsi untuk memprediksi harga
def predict_price(features):
    # Ubah fitur menjadi array 2D untuk prediksi
    features_array = np.array(features).reshape(1, -1)
    prediction = model.predict(features_array)
    return prediction[0]

# Tombol untuk melakukan prediksi
if st.button('Predict Price'):
    prediction = predict_price(features)
    st.success(f'The predicted price of the diamond is ${prediction:.2f}')
