import pickle
import numpy as np
import streamlit as st

#load save model 
model = pickle.load (open('Penyakit_jantung.sav','rb'))

#judul web
st.title('Prediksi Penyakit jantung')

col1, col2, col3, =st.columns(3)

with col1:
    age= st.number_input ('Umur')
with col2:
    anaemia = st.number_input ('Anemia')
with col3:
    creatinine_phosphokinase = st.number_input ('creatinine_phosphokinase')
with col1:
    diabetes = st.number_input ('diabetes')
with col2:
    ejection_fraction = st.number_input ('ejection_fraction')
with col3:
    high_blood_pressure = st.number_input ('tekanan_darah tinggi')
with col1:
    platelets = st.number_input ('trombosit')
with col2:
    serum_creatinine = st.number_input ('serum_kreatinin')
with col3:
   serum_sodium = st.number_input ('serum_sodium')
with col1:
    sex = st.number_input ('Kelamin')
with col2:
   smoking = st.number_input ('Meroko')
with col3:
   time = st.number_input ('waktu')

#code for prediction
Penyakitjantung_diagnosis =''

#membuat tombol prediction
if st.button('Prediksi Penyakit jantung'):
    Penyakitjantung_prediction = model.predict([[age,anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,serum_sodium,sex,smoking,time]])

    if (Penyakitjantung_prediction [0]==0):
        Penyakitjantung_diagnosis = 'Pasien Terkena Penyakit Jantung'
    else : 
        penyakitjantung_diagnosis = 'Pasien Tidak Terkena Penyakit jantung'

st.success (Penyakitjantung_diagnosis)

st.write ('Ahmad fudoli zaenun nazhirin ~ 191351108')

