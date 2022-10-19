import streamlit as st
import sqlite3
import random as rn


st.subheader("Adres Ekleme Sayfası")


conn = sqlite3.connect("odev.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS adresler(adresN INTEGER NOT NULL PRIMARY KEY,kullaniciN INTEGER, il TEXT, ilce TEXT, adres TEXT)")
conn.commit()


adresNo = rn.randint(999,99999999)
c.execute("SELECT kullaniciN FROM kullanıcılar")
kkk = c.fetchall()
kullaniciNo = st.selectbox("Kullanici No:",(kkk))
nkullanici = str(kullaniciNo).replace("(","").replace(")","").replace(",","")
il = st.text_input("İl")
ilce = st.text_input("İlçe")
adres = st.text_input("Adres")

if st.button("Kaydet"):
    c.execute("INSERT INTO adresler VALUES(?,?,?,?,?)", (adresNo, nkullanici, il, ilce,adres))
    conn.commit()