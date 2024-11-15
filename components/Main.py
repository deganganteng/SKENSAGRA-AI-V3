from components.subcomponents.Options.OptionPage import *
from components.subcomponents.Options.OptionHandler import *

def Main():
    option = st.selectbox(
        " Apa yang bisa kami bantu ? ",
        (
            "Informasi Umum SMKN 1 GRATI",
            "Informasi Kejuruhan SMKN 1 GRATI",
            "Informasi Golden Ticket PENS",
            "Informasi Produk SMKN 1 GRATI",
            "Informasi Kerja Sama INDUSTRI",
            "informasi Layanan Siswa",
        ),index=None,
        placeholder="Pilih Menu"
    )
    bahasa = st.selectbox(
        "Bahasa",
        (
            "Bahasa Indonesia",
            "Bahasa Inggris",
            "Bahasa Jepang",
            "Bahasa Jerman",
            "Bahasa Mandarin",
        ),index=None
    )
    Option(option,bahasa)
