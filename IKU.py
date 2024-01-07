import tkinter as tk

def hitung_indeks_kualitas_udara(jumlah_kendaraan, suhu, durasi_tanpa_hujan):

    # Validasi input
    if jumlah_kendaraan < 0:
        raise ValueError("Jumlah kendaraan harus positif")
    if suhu < 0:
        raise ValueError("Suhu harus positif")
    if durasi_tanpa_hujan < 0:
        raise ValueError("Durasi tanpa hujan harus positif")

    # Faktor kontribusi kendaraan
    faktor_kendaraan = jumlah_kendaraan / 100  

    # Faktor kontribusi suhu
    faktor_suhu = suhu / 30  

    # Faktor kontribusi durasi tanpa hujan
    faktor_tanpa_hujan = min(durasi_tanpa_hujan, 24) / 24  

    # Indeks Kualitas Udara (IKU)
    indeks_kualitas_udara = faktor_kendaraan + faktor_suhu + faktor_tanpa_hujan

    return indeks_kualitas_udara

# Klasifikasi kualitas udara
KUALITAS_UDARA = {
    0: "Baik",
    1: "Sedang",
    2: "Tidak sehat untuk kelompok sensitif",
    3: "Tidak sehat",
    4: "Sangat tidak sehat",
    5: "Berbahaya",
}

# Fungsi untuk menampilkan hasil IKU dan keterangan
def tampilkan_hasil():
    # Ambil nilai dari entry
    jumlah_kendaraan = float(entry_jumlah_kendaraan.get())
    suhu = float(entry_suhu.get())
    durasi_tanpa_hujan = float(entry_durasi_tanpa_hujan.get())

    try:
        # Hitung IKU
        iku = hitung_indeks_kualitas_udara(jumlah_kendaraan, suhu, durasi_tanpa_hujan)

        # Tampilkan hasil IKU
        label_hasil_iku.config(text=f"Indeks Kualitas Udara: {iku:.2f}")

        # Tentukan kategori kualitas udara
        kategori = 0
        if iku > 1:
            kategori = 1
        if iku > 2:
            kategori = 2
        if iku > 3:
            kategori = 3
        if iku > 4:
            kategori = 4
        if iku > 5:
            kategori = 5

        # Tampilkan keterangan kualitas udara
        label_keterangan_iku.config(text=f"Kualitas Udara: {KUALITAS_UDARA[kategori]}")

    except ValueError as e:
        # Tangani kesalahan validasi input
        label_hasil_iku.config(text="Error: " + str(e))
        label_keterangan_iku.config(text="")

# Buat jendela Tkinter
window = tk.Tk()
window.title("Kalkulator Identifikasi Kondisi Udara")
window.configure(bg="#B9F3FC")

# Font dan warna untuk judul
judul_font = ("Helvetica", 16, "bold")
judul_warna = "#333"

# Label untuk judul
label_judul = tk.Label(window, text="Kalkulator IKU", font=judul_font, fg=judul_warna, bg="#AEE2FF")
label_judul.grid(row=0, column=0, columnspan=2, pady=10, sticky="EW")

# Font dan warna untuk label dan entry
label_entry_font = ("Helvetica", 12, "bold")
label_warna = "#333"
entry_warna = "#FEDEFF"

# Label untuk jumlah kendaraan
label_jumlah_kendaraan = tk.Label(window, text="Jumlah kendaraan (per jam):", font=label_entry_font, fg=label_warna, bg="#93C6E7", justify="left")
label_jumlah_kendaraan.grid(row=1, column=0, padx=10, pady=5, sticky="E")

# Entry untuk jumlah kendaraan
entry_jumlah_kendaraan = tk.Entry(window, bg=entry_warna)
entry_jumlah_kendaraan.grid(row=1, column=1, padx=10, pady=5, sticky="W")

# Label untuk suhu
label_suhu = tk.Label(window, text="Suhu (derajat Celcius):", font=label_entry_font, fg=label_warna, bg="#93C6E7", justify="left")
label_suhu.grid(row=2, column=0, padx=10, pady=5, sticky="E")

# Entry untuk suhu
entry_suhu = tk.Entry(window, bg=entry_warna)
entry_suhu.grid(row=2, column=1, padx=10, pady=5, sticky="W")

# Label untuk durasi tanpa hujan
label_durasi_tanpa_hujan = tk.Label(window, text="Durasi tanpa hujan (jam):", font=label_entry_font, fg=label_warna, bg="#93C6E7", justify="left")
label_durasi_tanpa_hujan.grid(row=3, column=0, padx=10, pady=5, sticky="E")

# Entry untuk durasi tanpa hujan
entry_durasi_tanpa_hujan = tk.Entry(window, bg=entry_warna)
entry_durasi_tanpa_hujan.grid(row=3, column=1, padx=10, pady=5, sticky="W")

# Button untuk menghitung IKU
button_hitung = tk.Button(window, text="Hitung", command=tampilkan_hasil, bg="#4CAF50", fg="white", font=label_entry_font)
button_hitung.grid(row=4, column=0, columnspan=2, pady=10)

# Font dan warna untuk hasil IKU
hasil_font = ("Helvetica", 14, "bold")
hasil_warna = "#333"

# Label untuk hasil IKU
label_hasil_iku = tk.Label(window, text="Indeks Kualitas Udara:", font=hasil_font, fg=hasil_warna, bg="#93C6E7", justify="left")
label_hasil_iku.grid(row=5, column=0, columnspan=2, pady=5)

# Font dan warna untuk keterangan IKU
keterangan_font = ("Helvetica", 12)
keterangan_warna = "#555"

# Label untuk keterangan IKU
label_keterangan_iku = tk.Label(window, text="", font=keterangan_font, fg=keterangan_warna, bg="#FEDEFF", justify="left")
label_keterangan_iku.grid(row=6, column=0, columnspan=2, pady=5)

# Jalankan aplikasi
window.mainloop()