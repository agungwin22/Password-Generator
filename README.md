Password Generator

Program ini adalah sebuah **Generator Password Acak** yang dibuat dengan Python, memungkinkan pengguna untuk membuat password dengan kombinasi karakter sesuai pilihan mereka.

## Fitur Utama:

1. **Antarmuka Menu Interaktif**:
   - Menampilkan menu pilihan kombinasi karakter (Angka, Huruf, Karakter Khusus)
   - Input panjang password yang diinginkan
   - Pilihan untuk melanjutkan atau menghentikan program

2. **Kombinasi Karakter Fleksibel**:
   - **Angka** (0-9)
   - **Huruf** (huruf besar dan kecil)
   - **Karakter Khusus** (simbol seperti !@#$%^&* dll.)

3. **Fungsi yang Tersedia**:
   - `author()`: Menampilkan informasi pembuat program
   - `showMenu()`: Menampilkan menu pilihan kombinasi password
   - Logika utama untuk mengumpulkan karakter dan menghasilkan password acak

## Cara Menggunakan:

1. Jalankan program dengan perintah:
   ```bash
   python app.py
   ```

2. Masukkan panjang password yang diinginkan

3. Pilih kombinasi karakter dengan memasukkan angka:
   - `1` untuk menambahkan angka
   - `2` untuk menambahkan huruf
   - `3` untuk menambahkan karakter khusus
   - `4` untuk selesai memilih dan melihat hasil

4. Program akan menampilkan password acak berdasarkan pilihan kombinasi

5. Pilih `y` untuk membuat password baru atau `n` untuk keluar

## Catatan Teknis:

- Program membersihkan layar console secara otomatis (kompatibel dengan Windows, dengan alternatif untuk Linux/macOS yang dikomentari)
- Menggunakan modul `random` untuk pengacakan karakter
- Menggunakan modul `string` untuk akses kumpulan karakter standar
- Password dihasilkan dengan memilih karakter acak dari kumpulan karakter yang dipilih pengguna

## Persyaratan:

- Python 3.x
- Sistem operasi Windows (untuk fungsi `cls`), dapat disesuaikan untuk Linux/macOS dengan mengubah `os.system("cls")` menjadi `os.system("clear")`

Program ini berguna untuk membuat password yang kuat dan acak dengan tingkat kustomisasi yang fleksibel sesuai kebutuhan keamanan pengguna.
