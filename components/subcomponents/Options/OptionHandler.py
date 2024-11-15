from components.subcomponents.Options.OptionPage import *
from components.subcomponents import urlbase
import streamlit as st


def Option(option, lang):
    if option == None:
        OptionPage("","","","","").StartPage()
    elif option == "Informasi Umum SMKN 1 GRATI":
        OptionPage("Masukkan Pertanyaan disini!",
                   """##### Informasi umum SMKN 1 GRATI 
menyediakan Informasi umum mengenai berbagai hal tentang SMKN 1 GRATI    

##### Informasi Umum SMKN 1 GRATI
Memberikan informasi terkait:
- Profil SMKN 1 GRATI
- Sejarah dan prestasi sekolah
- Fasilitas yang tersedia di SMKN 1 GRATI
- Program unggulan yang ditawarkan""",
                    "Pusat Informasi Umum SMKN 1 GRATI dengan website resmi {urlbase.url_umum} ",
                    lang,
                    SkensagraCrew.GeneralCrew).BaseIO()
    elif option == "Informasi Kejuruhan SMKN 1 GRATI":
        OptionPage("Cari Informasi Seputar Kejuruhan SMKN 1 GRATI disini!",
                   """##### Informasi Kejuruhan SMKN 1 GRATI
Memberikan informasi terkait:
- Program studi kejuruan yang ada di SMKN 1 GRATI
- Kompetensi dan kurikulum masing-masing jurusan
- Fasilitas laboratorium dan praktek
- Keunggulan setiap jurusan dalam mencetak lulusan yang siap kerja""",
                    "Pusat Informasi Kejuruhan SMKN 1 GRATI dengan website resmi {urlbase.url_kejuruhan}",
                    lang,
                    SkensagraCrew.BaseCrew).BaseIO()
    elif option == "Informasi Golden Ticket PENS":
        OptionPage("Cari Informasi Seputar Golden Ticket PENS disini!",
                   """##### Informasi Golden Ticket PENS
Memberikan informasi terkait:
- Gambaran umum tentang program Golden Ticket
- Cara mendaftar dan manfaat partisipasi
- Kriteria kelayakan untuk program Golden Ticket""",
                    "Pusat Informasi Golden Ticket PENS dengan website resmi {urlbase.url_goldenticket}",
                    lang,
                    SkensagraCrew.BaseCrew).BaseIO()
    elif option == "Informasi Produk SMKN 1 GRATI":
        OptionPage("Cari Informasi Seputar Produk SMKN 1 GRATI disini!",
                   """##### Informasi Riset GEMA
Memberikan informasi terkait:
- Produk-produk hasil karya siswa SMKN 1 GRATI
- Cara pembelian dan pemesanan produk
- Showcase produk pada pameran dan acara khusus
- Produk unggulan yang telah mendapatkan sertifikasi""",
                    "Pusat Informasi Produk SMKN 1 GRATI dengan website resmi SMKN 1 GRATI : {urlbase.url_produk}",
                    lang,
                    SkensagraCrew.BaseCrew).BaseIO()
    elif option == "Informasi Kerja Sama Industri SMKN 1 GRATI":
        OptionPage("Cari Informasi Seputar Kerja Sama Industri SMKN 1 GRATI disini!",
                   """##### Informasi Kerja Sama Industri SMKN 1 GRATI
Memberikan informasi terkait:
- Kerja sama industri yang telah dijalin oleh SMKN 1 GRATI
- Manfaat kerja sama bagi siswa dan pihak industri
- Program magang dan kunjungan industri
- Peluang kerja bagi lulusan melalui kemitraan industri""",
                    "Pusat Informasi Kerja Sama Industri SMKN 1 GRATI dengan website resmi SMKN 1 GRATI {urlbase.url_kerjasama}",
                    lang,
                    SkensagraCrew.BaseCrew).BaseIO()
    elif option == "Informasi Layanan Siswa":
        OptionPage("Cari Informasi Seputar Informasi Layanan Siswa disini!",
                   """##### Informasi Layanan Siswa
Memberikan informasi terkait:
- Layanan akademik dan administrasi untuk siswa
- Bimbingan karier dan konseling siswa
- Program ekstrakurikuler dan pengembangan minat bakat
- Bantuan dan dukungan untuk kesejahteraan siswa di sekolah""",
                    "Pusat Informasi Layanan Siswa dengan website resmi : {urlbase.url_layanansiswa}",
                    lang,
                    SkensagraCrew.Basecrew).BaseIO()
    else:
        st.write("Masih dalam pengembangan")
