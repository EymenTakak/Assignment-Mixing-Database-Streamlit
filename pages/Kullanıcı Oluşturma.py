import random

import streamlit as st
import sqlite3
import random as rn

st.subheader("Kullanıcı Oluşturma Sayfası")


conn = sqlite3.connect("odev.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS kullanıcılar(kullaniciN INTEGER NOT NULL PRIMARY KEY, isim TEXT, soyisim TEXT, telefon INTEGER NOT NULL UNIQUE)")
conn.commit()

ad = st.text_input("Ad")
soyad = st.text_input("Soyad")
telno = st.number_input("Telefon Numarası",step=1)
x = random.randint(999,99999999)

if st.button("Oluştur"):
    c.execute("INSERT INTO kullanıcılar VALUES(?,?,?,?)",(x,ad,soyad,telno))
    conn.commit()
