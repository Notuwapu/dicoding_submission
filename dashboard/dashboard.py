import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
hour_df = pd.read_csv("../data/hour.csv")
day_df = pd.read_csv("../data/day.csv")

# Judul dashboard
st.title("Dashboard Analisis Peminjaman Sepeda")

# Sidebar untuk navigasi
menu = st.sidebar.selectbox("Pilih Visualisasi", [
    "Statistik Data", "Rata-rata Peminjaman Sepeda per Jam", "Distribusi Peminjaman Berdasarkan Cuaca"])

if menu == "Statistik Data":
    st.header("Informasi Dataset")
    st.write("### Informasi Dataset hour_df")
    st.write(hour_df.describe())
    st.write("### Informasi Dataset day_df")
    st.write(day_df.describe())
    
elif menu == "Rata-rata Peminjaman Sepeda per Jam":
    st.header("Rata-rata Jumlah Peminjaman Sepeda per Jam")
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.lineplot(data=hour_df, x='hr', y='cnt', estimator='mean', errorbar=None)
    ax.set_title("Rata-rata Jumlah Peminjaman Sepeda per Jam")
    ax.set_xlabel("Jam")
    ax.set_ylabel("Jumlah Peminjaman")
    ax.set_xticks(range(0, 24))
    st.pyplot(fig)
    
elif menu == "Distribusi Peminjaman Berdasarkan Cuaca":
    st.header("Distribusi Peminjaman Sepeda Berdasarkan Kondisi Cuaca")
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.boxplot(data=day_df, x='weathersit', y='cnt')
    ax.set_title("Distribusi Peminjaman Sepeda Berdasarkan Kondisi Cuaca")
    ax.set_xlabel("Kondisi Cuaca (1=Baik, 2=Normal, 3=Buruk, 4=Sangat Buruk)")
    ax.set_ylabel("Jumlah Peminjaman")
    st.pyplot(fig)
    

