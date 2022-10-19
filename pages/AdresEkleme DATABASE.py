import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect("odev.db")
c = conn.cursor()

c.execute("SELECT * FROM adresler")
adres = c.fetchall()
adresler = pd.DataFrame(adres)
adresler.columns = ["Adres No","Müşteri No","il","ilçe","Adres"]
st.table(adresler)