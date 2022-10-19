import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect("odev.db")
c = conn.cursor()
c.execute("SELECT * FROM urunler")
urun = c.fetchall()
urunler = pd.DataFrame(urun)
urunler.columns = ["Ürün ID","Ürün İsmi","Fiyat"]
st.table(urunler)

if st.button("text"):
    st.text(urun[1][1])