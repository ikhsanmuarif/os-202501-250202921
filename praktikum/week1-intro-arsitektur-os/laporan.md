
# Laporan Praktikum Minggu [X]
Topik: "Arsitektur Sistem Operasi dan Kernel"

---

## Identitas
- **Nama**  : Ikhsan Mu'arif 
- **NIM**   : 250202921  
- **Kelas** : 1IKRB

---

## Tujuan
Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa akan mempelajari arsitektur dasar sistem operasi: bagaimana komponen OS bekerja, serta bagaimana interaksi antara user, aplikasi, kernel, dan hardware terjadi.

Mahasiswa juga diperkenalkan pada:
Perbedaan mode eksekusi kernel mode dan user mode.
Mekanisme system call (panggilan sistem).
Perbandingan model arsitektur OS seperti monolithic kernel, layered approach, dan microkernel.
Eksperimen akan dilakukan menggunakan perintah dasar Linux untuk melihat informasi kernel dan modul aktif.



---

## Langkah Praktikum
1. Setup Environment
Pastikan Linux (Ubuntu/WSL) sudah terinstal.
Pastikan Git sudah dikonfigurasi dengan benar:
git config --global user.name "Nama Anda"
git config --global user.email "email@contoh.com"

2. Diskusi Konsep
Baca materi pengantar tentang komponen OS.
Identifikasi komponen yang ada pada Linux/Windows/Android.

3. Eksperimen Dasar Jalankan perintah berikut di terminal:
uname -a
whoami
lsmod | head
dmesg | head
Catat dan analisis modul kernel yang tampil.

4. Membuat Diagram Arsitektur
Buat diagram hubungan antara User → System Call → Kernel → Hardware.
Gunakan draw.io atau Mermaid.
Simpan hasilnya di:
praktikum/week1-intro-arsitektur-os/screenshots/diagram-os.png

5. Penulisan Laporan
Tuliskan hasil pengamatan, analisis, dan kesimpulan ke dalam laporan.md.
Tambahkan screenshot hasil terminal ke folder screenshots/.
6. Commit & Push
git add .
git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
git push origin main

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./sreenshots/screenshots.terminal%20wsl.png.png)

---

## Analisis
- Jelaskan makna hasil percobaan. 
- makna uname -a
Laporan ini adalah kartu identitas dari Kernel yang sedang berjalan. Angka versi (misalnya, 5.10.0-23) menunjukkan fungsionalitas dan fitur yang tersedia dalam Kernel tersebut (misalnya, driver apa yang didukung, algoritma scheduler mana yang digunakan, dan bug apa yang sudah diperbaiki)..
makna whoami
Laporan ini memberi tahu siapa yang menjalankan perintah, yang secara langsung berkaitan dengan hak akses (privileges) yang dimiliki oleh proses saat ini.
makna lsmod | head
Laporan ini adalah daftar modul kernel (driver dan layanan) yang saat ini dimuat dan aktif dalam memori Kernel. Ini menunjukkan bahwa sistem telah mendeteksi dan mengaktifkan fungsionalitas tertentu (seperti file system vfat atau dukungan virtualisasi kvm).
makna dmesg | head 
Laporan ini adalah log sejarah komunikasi antara perangkat keras dan Kernel sejak sistem dihidupkan (boot). Ini mencatat semua inisialisasi, deteksi perangkat keras (CPU, memori, disk), dan potensi kesalahan driver.

- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
- Secara keseluruhan, laporan dari keempat perintah ini menegaskan tiga poin fundamental:
System Call sebagai Gerbang Eksklusif: Semua informasi yang ditampilkan (identitas, versi, log) bersifat privilege (berhak istimewa). Program ruang pengguna hanya dapat mengaksesnya melalui System Call yang diawasi Kernel. Ini menjamin keamanan dan konsistensi sistem.
Kernel sebagai Manajer Tunggal: Hasil ini mendemonstrasikan fungsi utama Kernel:
Identitas & Keamanan (whoami).
Abstraksi Hardware (uname -a & dmesg).
Manajemen Sumber Daya (I/O, CPU, Memori melalui lsmod dan dmesg).
Arsitektur Monolitik yang Fleksibel: Laporan lsmod mengkonfirmasi bahwa meskipun Linux berakar pada arsitektur monolitik, ia menggunakan modularitas untuk efisiensi dan kemampuan live-patching, membuktikan desain yang menyeimbangkan kinerja dan fleksibilitas.

- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?
- Perbedaan hasil dari perintah yang sama di lingkungan Linux (berbasis UNIX/POSIX) dan Windows terletak pada perbedaan fundamental dalam arsitektur OS, set System Call, dan implementasi Fungsi Kernel yang mendasarinya.
Secara umum, Linux memberikan hasil yang mentah, teknis, dan berfokus pada kernel, sementara Windows (melalui perintah atau alat setara) memberikan hasil yang terstruktur, berfokus pada keamanan domain, dan lebih berorientasi pada pengguna akhir.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
Kernel Adalah Bos Mutlak Sistem.
Semua hasil perintah (versi Kernel dari uname -a, hak akses dari whoami, dan log boot dari dmesg) membuktikan bahwa Kernel adalah inti yang mengontrol segalanya. Aplikasi user harus melalui System Call untuk meminta izin Kernel, seperti meminta ID pengguna atau membaca driver yang sedang aktif.

Linux Cepat Karena Fleksibilitasnya Cerdik.
Arsitektur Linux menggunakan cara kerja Monolitik (semua fungsi inti bersama-sama agar cepat), namun ia pintar karena bisa memuat driver baru secara dinamis (Modul Kernel seperti yang dilihat di lsmod). Ini membuat sistem tetap cepat seperti Monolitik, tapi fleksibel seperti sistem modern, tanpa harus restart setiap saat.


---

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi.
   Manajemen Sumber Daya (Resource Management): OS bertanggung jawab untuk mengelola dan mengalokasikan sumber daya sistem seperti CPU (prosesor), memori, perangkat I/O (input/output), dan penyimpanan. Ini mencakup penjadwalan proses, alokasi memori, dan pengelolaan file agar program dapat berjalan secara efisien dan tidak saling mengganggu.

   Antarmuka Pengguna (User Interface - UI): OS menyediakan cara bagi pengguna untuk berinteraksi dengan komputer. Ada dua jenis utama: Antarmuka Baris Perintah (Command-Line Interface - CLI) dan Antarmuka Grafis (Graphical User Interface - GUI).

   Penyediaan Layanan (Service Provision): OS menyediakan layanan dasar bagi program aplikasi, seperti eksekusi program, operasi I/O, komunikasi antar-proses, dan deteksi/penanganan error.
   
2. Jelaskan perbedaan antara kernel mode dan user mode.

   kernel mode adalah mode super power OS untuk mengendalikan perangkat keras, sedangkan user mode adalah mode sandbox di mana aplikasi berjalan dengan hak terbatas demi keamanan dan stabilitas sistem.

3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.

   contoh os arsitektur monolithic yaitu linux, openBSD, freeBSD, netBSD.
   contoh os microkernel yaitu Mach, QNX, Minix 3.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  bagian paling menantang minggu ini adalah tidak bisa download wsl di laptop.
- Bagaimana cara Anda mengatasinya?  
  tutorial youtube dan meminta teman untuk mengajarkan.
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
