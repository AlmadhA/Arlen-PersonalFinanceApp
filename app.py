import streamlit as st
from sheets_service import read_records

st.title("🔗 Login User")

# Ambil data user_map
user_map_df = read_records("user_map")

with st.form("login_form"):
    username = st.text_input("Kode User")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

if submitted:
    if username == "" or password == "":
        st.warning("Mohon isi Kode User dan Password")
    else:
        # Cari user yang cocok
        user_row = user_map_df[
            (user_map_df['Kode User'] == username) & 
            (user_map_df['Password'] == password)
        ]

        if not user_row.empty:
            st.success(f"Login berhasil! Selamat datang {user_row.iloc[0]['Nama Lengkap']}")
            # Baca sheet sesuai username (Kode User)
            try:
                data = read_records(username)
                st.dataframe(data)
            except Exception as e:
                st.error("Gagal membaca data sheet sesuai username:")
                st.exception(e)
        else:
            st.error("Kode User atau Password salah.")