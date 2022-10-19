import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect("odev.db")
c = conn.cursor()

c.execute("SELECT * FROM kullanıcılar")
kullanici = c.fetchall()
kullanicilar = pd.DataFrame(kullanici)
kullanicilar.columns = ["Müşteri No","İsim","Soyisim","Telefon Numarası"]
st.table(kullanicilar)

