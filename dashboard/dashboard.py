import streamlit as st
import analysis

def main():
    st.sidebar.image("https://thumbs.dreamstime.com/b/bike-rental-logo-design-minimalist-style-three-bicycle-row-creative-emblem-mountain-store-161043342.jpg")
    st.sidebar.header('Pilih Dasbor')
    analysis_choice = st.sidebar.selectbox(
        'Hasil Analisis yang Tersedia:', 
                                           ['Pola Rental Berdasarkan Musim', 
                                            'Distribusi Rental Hari Libur vs Hari Kerja', 
                                            'Hubungan antara Kondisi Cuaca dan Jumlah Rental'
                                            ]
                                            )

    analysis.display_analysis(analysis_choice)

if __name__ == '__main__':
    main()