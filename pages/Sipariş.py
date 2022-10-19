import random
import streamlit as st
import sqlite3
import random as rn
import main as mn
import main2 as mnd
import datetime

conn = sqlite3.connect("odev.db")
c = conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS siparis(siparisNo INTEGER NOT NULL PRIMARY KEY,kullaniciN INTEGER, adresN INTEGER, urunler TEXT, toplam INTEGER, odeme TEXT,teslim INTEGER, sipTarih TEXT)")
conn.commit()


c.execute("SELECT * FROM urunler")
urun = c.fetchall()


def toplama():
    zz = 0
    z = 0
    for a in range(len(mn.fiyat_toplam)):
        tp = mn.fiyat_toplam[z]
        tp+=zz
        z+=1
    return zz


col1, col2 = st.columns(2)


with col1:
    sxx = 0
    zxx = "Sepete Ekle "
    urunler = []
    conn.commit()
    for x in range(len(urun)):
        st.markdown(f"Ürün: {urun[sxx][1]}")
        st.text(f"Fiyat: {urun[sxx][2]}")
        if st.button(zxx):
            mn.fiyat_toplam.append(urun[sxx][2])
            mnd.idler.append(urun[sxx][0])
        sxx+=1
        zxx+=" "

with col2:
    if st.button("Sepeti Temizle"):
        mn.fiyat_toplam=[]
        mnd.idler=[]

    st.header(f"Toplam Fiyat: {sum(mn.fiyat_toplam)}")
    st.header(mnd.idler)
    siparisn = rn.randint(11111,99999999)
    c.execute("SELECT kullaniciN FROM kullanıcılar")
    kkk = c.fetchall()
    kullaniciNo = st.selectbox("Kullanici No:", (kkk))
    nkullanici = int(str(kullaniciNo).replace("(", "").replace(")", "").replace(",", ""))
    toplama()
    c.execute(f"SELECT adres FROM adresler WHERE kullaniciN=={nkullanici}")
    adres = c.fetchall()
    adres2 = st.selectbox("Adres Seçiniz",(adres))
    adres3 = str(adres2).replace("(","").replace(")","").replace(",","")
    ödeme_turu = st.selectbox("Ödeme Şekli",("Nakit","Kredi Kartı","Online Ödeme"))
    teslim = 0
    st.text(datetime.datetime.now())
    if st.button("Sipariş Ver"):
        c.execute(f"SELECT adresN FROM adresler WHERE adres=={adres3}")
        adresid = c.fetchone()
        adresid = str(adresid).replace("(","").replace(")","").replace(",","")
        gun = datetime.datetime.now()
        st.text(f"{siparisn, nkullanici, adresid, str(mnd.idler), sum(mn.fiyat_toplam), ödeme_turu, teslim}")
        c.execute("INSERT INTO siparis VALUES(?,?,?,?,?,?,?,?)",(siparisn,int(nkullanici),int(adresid),str(mnd.idler),sum(mn.fiyat_toplam),ödeme_turu,teslim,gun))
        conn.commit()

