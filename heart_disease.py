import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('model.sav','rb'))

def main():
    st.title('Cek Kemungkinan Kamu Terjangkit Penyakit Jantung')

    age = st.text_input('Umur')
    sex = st.text_input('Jenis Kelamin (0=Perempuan 1=Laki-Laki)')
    cp = st.text_input('Tipe Nyeri Data (Dari 0 sampai 3)')
    trestbps = st.text_input('Tekanan Darah Saat Istirahat')
    chol = st.text_input('Kolesterol mg/d;')
    fbs = st.text_input('Gula Darah > 120 (0=Salah 1=Benar)')
    restecg = st.text_input('Rekam Jantung (0,1,2)')
    thalach = st.text_input('Detak Jantung Tertinggi')
    exang = st.text_input('Nyeri Dada Saat Latihan (0=Tidak 1=Ya)')
    oldpeak = st.text_input('ST Depressi')
    slope = st.text_input('Puncak Latihan ST Segment')
    ca = st.text_input('Jumlah Pembulud Darah Utama')
    thal = st.text_input('Thal (0=Normal 1=Cacat Non Permanen 2=Cacat Permanen)')

    diagnose = ''

    if st.button('Heart Disease Result'):
        diagnose = heart_predict([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
    
    st.success(diagnose)

def heart_predict(input_data):
    input_array = np.asarray(input_data)
    re=input_array.reshape(1,-1)
    prediction=loaded_model.predict(re)
    print(prediction)
    
    if prediction[0] == 1:
        return 'Terindikasi Penyakit Jantung'
    else:
        return 'Tidak Ada Indikasi Penyakit Jantung'

if __name__ == '__main__':
    main()