
# Laporan Praktikum Minggu [X]
mekanisme system call dan struktur sistem operasi

---

## Identitas
- **Nama**  : Ikhsan Mu'arif 
- **NIM**   : 250202921
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1. Menjelaskan konsep dan fungsi system call dalam sistem operasi.
2. Mengidentifikasi jenis-jenis system call dan fungsinya.
3. Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
4. Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.


---

## Dasar Teori
System call adalah antarmuka antara program aplikasi dan kernel yang memungkinkan aplikasi berinteraksi dengan perangkat keras secara aman melalui layanan OS.

Mahasiswa akan melakukan eksplorasi terhadap:
Jenis-jenis system call yang umum digunakan (file, process, device, communication).
Alur eksekusi system call dari mode user menuju mode kernel.
Cara melihat daftar system call yang aktif di sistem Linux

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

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
![Screenshot hasil](./screenshots/syscall-diagram.png)
![Screenshot hasil](./screenshots/syscall_ls.png)
![Screenshot hasil](./screenshots/dmseg.png)
 

---

## Analisis
- Jelaskan makna hasil percobaan. 
  Menunjukkan interaksi antara user space dan kernel space Menilai efisiensi OS dalam menangani tugas Menganalisis perilaku program
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
  Hasil percobaan menunjukkan bagaimana program berbicara dengan kernel lewat system call.
System call ini adalah bagian penting dari OS karena jadi penghubung antara program dan hardware.
Efisiensi dan kecepatan system call bisa berbeda, tergantung bagaimana arsitektur kernel OS itu dirancang.
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
 System call di Linux umumnya lebih cepat dan efisien dibandingkan Windows.
Hal ini karena Linux menggunakan monolithic kernel yang memungkinkan akses langsung ke layanan kernel tanpa banyak lapisan tambahan.

---
## Analisis 400–500 kata 
 1. Mengapa System Call Penting untuk Keamanan OS dan Bagaimana OS Menjaga Transisi User–Kernel yang Aman

System call adalah penghubung antara aplikasi yang berjalan di mode pengguna (user mode) dengan kernel sistem operasi yang berjalan di mode kernel (kernel mode). System call memungkinkan aplikasi meminta layanan sistem, seperti akses file, komunikasi jaringan, atau manajemen proses, secara terkontrol dan aman.

Pentingnya System Call untuk Keamanan OS

System call sangat penting dalam menjaga keamanan sistem operasi karena mereka menjadi satu-satunya cara bagi program untuk berinteraksi dengan sumber daya hardware dan kernel. Tanpa system call, aplikasi bisa langsung mengakses hardware atau memori kernel, yang akan sangat berbahaya. Dengan adanya system call, kernel dapat melakukan validasi dan kontrol terhadap setiap permintaan.

Misalnya, ketika sebuah aplikasi ingin membuka file, kernel akan mengecek apakah aplikasi tersebut punya izin akses terhadap file tersebut. Jika tidak, kernel akan menolak permintaan tersebut. Hal ini mencegah program jahat mengakses data yang seharusnya dilindungi.

Selain itu, system call juga merupakan titik implementasi berbagai mekanisme keamanan seperti pengaturan hak akses (access control), sandboxing, dan pelacakan aktivitas (audit). Contohnya, sistem keamanan seperti SELinux memanfaatkan kontrol system call untuk membatasi operasi yang bisa dilakukan oleh suatu program.

2. Bagaimana OS Memastikan Transisi User–Kernel Berjalan Aman?

Transisi dari mode pengguna ke mode kernel adalah proses yang sangat sensitif. Jika tidak dijaga dengan baik, bisa terjadi serangan yang memungkinkan program biasa mendapatkan akses kernel yang seharusnya tidak dimiliki.

Untuk itu, OS dan CPU menggunakan beberapa mekanisme keamanan:

Mode Privilege Terpisah
CPU mempunyai dua mode: user mode dan kernel mode. Program hanya bisa masuk ke kernel mode melalui instruksi khusus yang diizinkan, misalnya syscall di Linux. Ini memastikan aplikasi tidak bisa sembarangan menjalankan kode kernel.

Validasi Parameter
Kernel selalu memeriksa setiap data atau pointer yang dikirim aplikasi lewat system call. Ini mencegah program memberikan alamat memori yang salah atau berbahaya.

Isolasi Memori
Teknologi virtual memory dan MMU menjaga agar memori kernel tidak bisa diakses langsung oleh aplikasi biasa. Jadi, aplikasi tidak dapat merusak data kernel atau proses lain.

Pengamanan Jalur Eksekusi
Beberapa OS juga menerapkan teknik seperti Control Flow Integrity (CFI) yang menjaga agar jalur eksekusi kode kernel tidak bisa dibajak oleh program jahat.

3. Contoh System Call yang Sering Digunakan di Linux
read() dan write(): Membaca dan menulis data ke file atau perangkat.
open() dan close(): Membuka dan menutup file.
fork(): Membuat proses baru.

System call sangat krusial dalam arsitektur sistem operasi karena mereka menjamin bahwa setiap akses ke sumber daya yang sensitif harus melalui jalur yang aman dan terkendali. Dengan mekanisme validasi dan isolasi yang ketat, OS memastikan transisi dari user mode ke kernel mode tidak bisa disalahgunakan, sehingga menjaga stabilitas dan keamanan sistem secara keseluruhan.


## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
System call adalah mekanisme utama komunikasi antara program dan kernel, yang memungkinkan program mengakses layanan OS seperti file, memori, dan proses secara aman.

Hasil praktikum menunjukkan bahwa Linux lebih efisien dalam menangani system call dibanding Windows, karena arsitektur kernel Linux yang monolithic meminimalkan overhead.
Alat analisis seperti strace di Linux memudahkan pengamatan langsung terhadap system call, sedangkan di Windows, pemantauan memerlukan tool tambahan dan lebih kompleks.

---

## Quiz
1. Apa fungsi utama system call dalam sistem operasi?
   Fungsi utama system call dalam sistem operasi adalah sebagai jembatan (interface) antara program pengguna (user‑space) dan kernel (kernel‑space), agar program dapat meminta layanan dari sistem operasi secara aman dan terkontrol
2. Sebutkan 4 kategori system call yang umum digunakan.  
   manajemen proses(process control), Manajemen Berkas (File Management), Manajemen Perangkat (Device Management), Manajemen Informasi (Information Maintenance)
3. Mengapa system call tidak bisa dipanggil langsung oleh user program?
   sytem call tidak bisa dipanggil langsung oleh user program karena alasan utama yaitu keamanan, perlindungan sistem, abstraksi dan control, stabilitas sistem

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
 ketika tidak bisa mendownload wsl eror  
- Bagaimana cara Anda mengatasinya?  
 tutorial youtube
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
