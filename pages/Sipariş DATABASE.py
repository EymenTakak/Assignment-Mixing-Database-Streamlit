import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect("odev.db")
c = conn.cursor()
c.execute("SELECT * FROM siparis")
urun = c.fetchall()
urunler = pd.DataFrame(urun)
urunler.columns = ["Sipariş No","Kullanıcı No","Adres ID","Ürünler","Toplam Fiyat","Ödeme Şekli","Teslim Durumu","Tarih"]
st.table(urunler)