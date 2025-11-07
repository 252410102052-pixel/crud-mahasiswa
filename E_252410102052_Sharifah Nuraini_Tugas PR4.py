import pandas as pd  # mengimpor library pandas

file_name = 'data_mahasiswa.csv'  # variabel untuk file CSV

# membuat data awal jika file belum ada
data_awal = [
    {'NIM': '192410101000', 'Nama': 'Uya Kuya', 'Program Studi': 'Sistem Informasi'},
    {'NIM': '192410102000', 'Nama': 'Puan Maharani', 'Program Studi': 'Teknologi Informasi'},
    {'NIM': '192410103000', 'Nama': 'Joko Widodo', 'Program Studi': 'Informatika'},
    {'NIM': '192410104000', 'Nama': 'Imam Bonjol', 'Program Studi': 'Sistem Informasi'},
    {'NIM': '192410105000', 'Nama': 'Soebandi', 'Program Studi': 'Teknologi Informasi'},
    {'NIM': '192410106000', 'Nama': 'Cut Nyak Dien', 'Program Studi': 'Informatika'},
    {'NIM': '192410107000', 'Nama': 'Fajar Sadboy', 'Program Studi': 'Sistem Informasi'},
    {'NIM': '192410108000', 'Nama': 'King Bowo', 'Program Studi': 'Teknologi Informasi'},
    {'NIM': '192410109000', 'Nama': 'Taehyung', 'Program Studi': 'Informatika'}
]

# menggunakan fungsi util untuk membaca CSV (memastikan NIM tetap string dan tanpa spasi)
def baca_df():
    df = pd.read_csv(file_name, dtype={'NIM': str})  # membaca CSV, sehingga NIM dibaca sebagai string
    df['NIM'] = df['NIM'].astype(str).str.strip()    # menghapus spasi di NIM
    return df

# membuat file CSV awal jika belum ada / salah struktur
try:
    df = baca_df()
    if set(df.columns) != {'NIM', 'Nama', 'Program Studi'}:
        raise ValueError("Struktur kolom tidak sesuai")  # mengecek kolom
except (FileNotFoundError, ValueError, pd.errors.EmptyDataError):
    df = pd.DataFrame(data_awal)        # membuat DataFrame baru dari data_awal
    df['NIM'] = df['NIM'].astype(str)   # memastikan NIM string
    df.to_csv(file_name, index=False)   # menyimpan ke CSV
    print("File data_mahasiswa.csv dibuat ulang dengan data awal.\n")

# menampilkan seluruh data mahasiswa
def tampilkan_data():
    df = baca_df()
    print("\n=== Data Mahasiswa ===")
    print(df.to_string(index=False))  # tampilkan tabel tanpa index

# menambah data mahasiswa baru
def tambah_data():
    df = baca_df()
    nim = input("Masukkan NIM: ").strip()
    nama = input("Masukkan Nama: ").strip()
    prodi = input("Masukkan Program Studi: ").strip()

    if nim in df['NIM'].astype(str).values:  # cek NIM duplikat
        print("NIM sudah ada, tidak ditambahkan.")
        return

    new_data = pd.DataFrame({'NIM': [nim], 'Nama': [nama], 'Program Studi': [prodi]})
    df = pd.concat([df, new_data], ignore_index=True)  # gabungkan data baru
    df.to_csv(file_name, index=False)
    print("Data berhasil ditambahkan!")

# mengubah data mahasiswa berdasarkan NIM
def ubah_data():
    df = baca_df()
    nim = input("Masukkan NIM mahasiswa yang ingin diubah: ").strip()

    if nim in df['NIM'].astype(str).values:  # cek apakah NIM ada
        nama_baru = input("Masukkan nama baru: ").strip()
        prodi_baru = input("Masukkan program studi baru: ").strip()
        df.loc[df['NIM'] == nim, ['Nama', 'Program Studi']] = [nama_baru, prodi_baru]
        df.to_csv(file_name, index=False)
        print("Data berhasil diubah!")
    else:
        print("NIM tidak ditemukan!")

# menghapus data mahasiswa
def hapus_data():
    df = baca_df()
    nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ").strip()

    if nim in df['NIM'].astype(str).values:  # cek apakah NIM ada
        df = df[df['NIM'] != nim]            # hapus baris sesuai NIM
        df.to_csv(file_name, index=False)
        print("Data berhasil dihapus!")
    else:
        print("NIM tidak ditemukan!")

# menu utama
while True:
    print("\n=== MENU DATA MAHASISWA ===")
    print("1. Tampilkan seluruh data mahasiswa")
    print("2. Tambah data mahasiswa")
    print("3. Ubah data mahasiswa")
    print("4. Hapus data mahasiswa")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ").strip()

    if pilihan == '1':
        tampilkan_data()
    elif pilihan == '2':
        tambah_data()
    elif pilihan == '3':
        ubah_data()
    elif pilihan == '4':
        hapus_data()
    elif pilihan == '5':
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
