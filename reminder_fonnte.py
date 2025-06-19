
import requests
import pandas as pd
from datetime import datetime

# === KONFIGURASI ===
FONNTE_TOKEN = "ISI_TOKEN_LO_DI_SINI"  # Ganti dengan token dari fonnte.com
EXCEL_FILE = "data_pengiriman.xlsx"

# === FUNGSI KIRIM PESAN ===
def kirim_whatsapp(nomor, pesan):
    url = "https://api.fonnte.com/send"
    payload = {
        "target": nomor,
        "message": pesan,
        "countryCode": "62"
    }
    headers = {
        "Authorization": FONNTE_TOKEN
    }
    response = requests.post(url, data=payload, headers=headers)
    print(f"{nomor} -> Status: {response.status_code}")

# === LOGIKA UTAMA ===
df = pd.read_excel(EXCEL_FILE)
hari_ini = datetime.now().date()

for index, row in df.iterrows():
    tanggal_kirim = row["Tanggal Kirim"].date()
    if tanggal_kirim == hari_ini:
        pesan = f"Halo {row['Nama']}, barang kamu akan dikirim hari ini. Terima kasih 🙏"
        kirim_whatsapp(str(row['Nomor WA']), pesan)
