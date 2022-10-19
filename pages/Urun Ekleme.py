import random
import streamlit as st
import sqlite3
import random as rn



conn = sqlite3.connect("odev.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS urunler(urunId INTEGER NOT NULL PRIMARY KEY, urunIsmı TEXT, fiyat INTEGER)")
conn.commit()

urun = random.randint(1,300)
urunismi = st.text_input("ürün ismi")
urunfiyat = st.number_input("ürün fiyatı",step=1)

if st.button("Kaydet"):
    c.execute("INSERT INTO urunler VALUES(?,?,?)",(urun,urunismi,urunfiyat))
    conn.commit()

