import streamlit as st
from sheets_service import read_records

# Fungsi halaman login
def login_page():
    st.title("🔗 Login User")
    user_map_df = read_records("user_map")

    with st.form("login_form"):
        username = st.text_input("Kode User")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

    if submitted:
        if username == "" or password == "":
            st.warning("Mohon isi Kode User dan Password")
        else:
            user_row = user_map_df[
                (user_map_df['Kode User'] == username) & 
                (user_map_df['Password'] == password)
            ]

            if not user_row.empty:
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.session_state['fullname'] = user_row.iloc[0]['Nama Lengkap']
                st.experimental_rerun()
                return  # Hindari error dengan return setelah rerun
            else:
                st.error("Kode User atau Password salah.")

# Fungsi halaman utama setelah login
def main_page():
    st.title(f"Welcome, {st.session_state['fullname']}")

    page = st.sidebar.selectbox("Pilih halaman:", ["Form", "Dashboard"])

    if page == "Form":
        st.header("Form Page")
        # Tambahkan form input disini
        st.write("Ini adalah halaman Form.")
    elif page == "Dashboard":
        st.header("Dashboard Page")
        # Tambahkan tampilan dashboard disini
        # Contoh: baca data sesuai username
        try:
            data = read_records(st.session_state['username'])
            st.dataframe(data)
        except Exception as e:
            st.error("Gagal membaca data sheet sesuai username:")
            st.exception(e)

    if st.sidebar.button("Logout"):
        st.session_state.clear()
        st.experimental_rerun()

# Inisialisasi session_state
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if st.session_state['logged_in']:
    main_page()
else:
    login_page()