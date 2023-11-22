import streamlit as st
st.title( 'hitung luas persegi panjang')

panjang = st.number_input("masukkan nilai Panjang", 0) 
lebar = st.number_input("masukkan nilai Lebar", 0) 
hitung = st.button ("gitung luas")