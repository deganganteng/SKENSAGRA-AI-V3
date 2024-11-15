import streamlit as st
from AIComponents.Crew import *
from dotenv import load_dotenv

class OptionPage:
    def __init__(self,question : str, info : str, Context, lang, crew_method):
        self.crew_method = crew_method
        self.question = question
        self.Context = Context
        self.info = info
        self.lang = lang

    def BaseIO(self) :
        st.markdown(self.info)
        UserQueries = st.text_input(self.question)
        Konteks = self.Context
        language = self.lang
        submit = st.button("Tanyakan !")
        if  submit and UserQueries != "":
            st.write('**Your Query:**')
            st.write(f"> {UserQueries}")
            with st.spinner("AI sedang memproses Pertanyaan!") : 
                skensagra_instance = SkensagraCrew(UserQueries, Konteks, language)
                results = self.crew_method(skensagra_instance)

            st.success("Here are the results:")
            st.markdown(results)

        elif submit and UserQueries == "":
            st.warning("Please enter a query to get started.")
    
    def DiseaseDetect(self) :
        st.markdown(self.info)
        UserQueries = st.text_input(self.question)
        Konteks = self.Context
        language = self.lang
        submit = st.button("Tanyakan !")
        if  submit and UserQueries != "":
            st.write('**Your Query:**')
            st.write(f"> {UserQueries}")
            with st.spinner("AI sedang memproses Pertanyaan!") : 
                gema_instance = SkensagraCrew(UserQueries, Konteks, language)
                results = self.crew_method(gema_instance)

            st.success("Here are the results:")
            st.markdown(results)

        elif submit and UserQueries == "":
            st.warning("Please enter a query to get started.")
    def StartPage(self) : 
        st.info("Silahkan memilih menu diatas untuk memulai berikut penjelasan setiap menu yang tersedia!")
        st.markdown("""##### SMKN 1 GRATI 
menyediakan Informasi umum mengenai berbagai hal tentang SMKN 1 GRATI       
##### Informasi Umum SMKN 1 GRATI
Memberikan informasi terkait:

- Profil SMKN 1 GRATI
- Sejarah dan prestasi sekolah
- Fasilitas yang tersedia di SMKN 1 GRATI
- Program unggulan yang ditawarkan

##### Informasi Kejuruhan SMKN 1 GRATI
Memberikan informasi terkait:

- Program studi kejuruan yang ada di SMKN 1 GRATI
- Kompetensi dan kurikulum masing-masing jurusan
- Fasilitas laboratorium dan praktek
- Keunggulan setiap jurusan dalam mencetak lulusan yang siap kerja

##### Informasi Golden Ticket PENS
Memberikan informasi terkait:

- Gambaran umum tentang program Golden Ticket
- Cara mendaftar dan manfaat partisipasi
- Kriteria kelayakan untuk program Golden Ticket
                    
##### Informasi Produk SMKN 1 GRATI
Memberikan informasi terkait:

- Produk-produk hasil karya siswa SMKN 1 GRATI
- Cara pembelian dan pemesanan produk
- Showcase produk pada pameran dan acara khusus
- Produk unggulan yang telah mendapatkan sertifikasi

##### Informasi Kerja Sama Industri SMKN 1 GRATI
Memberikan informasi terkait:

- Kerja sama industri yang telah dijalin oleh SMKN 1 GRATI
- Manfaat kerja sama bagi siswa dan pihak industri
- Program magang dan kunjungan industri
- Peluang kerja bagi lulusan melalui kemitraan industri
                    
##### Informasi Layanan Siswa
Memberikan informasi terkait:

- Layanan akademik dan administrasi untuk siswa
- Bimbingan karier dan konseling siswa
- Program ekstrakurikuler dan pengembangan minat bakat
- Bantuan dan dukungan untuk kesejahteraan siswa di sekolah
""")