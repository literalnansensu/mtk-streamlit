import streamlit as st

st.title("🎈 matematika ilmu yg mematikan")

st.header("aplikasi ngecek genap/ganjil")
angka = st.number_input("tulis sebuah angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah bilangan genap")
else:
    st.write(f"{angka} adalah bilangan ganjil")
