
# Laporan Praktikum Minggu [14]
Topik: Penyusunan Laporan Praktikum Format IMRAD
---

## Identitas
- **Nama**  : Ikhsan Mu'arif
- **NIM**   : 250202921  
- **Kelas** : 1IKRB

---

## Topik: Simulasi dan Mendeteksi Deadlock Dalam Siste Operasi 
---

## Pendahuluan (Introduction)
## A. Latar Belakang  
 Deadlock merupakan salah satu permasalahan dalamsistem operasi modern yang menyebabkan sistem berhenti merespons dan menurunkan kinerja secara signifikan. Deadlock terjadi ketika dua atau lebih proses saling menunggu sumber daya(resource) yang sedang digunakan oleh proses lain, sehingga tidak ada satupun proses yang dapat melanjutkan eksekusinya.
 
 deadlock dapat terjadi jika empat kondisi berikut terpenuhi secara bersamaan: mutual exclusion (hanya satu proses yang dapat menggunakan resource pada suatu waktu), hold and wait (proses memegang resource sambil menunggu resource lain), no preemption (resource tidak dapat diambil paksa dari proses), dan circular wait (terdapat rantai siklik dari proses yang saling menunggu resource). praktikum ini bertujuan mensimulasikan dan mendeteksi deadlock.
 ## B. Rumusan Masalah
 1. Bagaimana mengimplementasikan algoritma deteksi deadlock untuk mengidentifikasi proses-proses yang terlibat dalam kondisi deadlock?
2. Bagaimana karakteristik circular wait yang menyebabkan terjadinya deadlock dalam sistem dengan multiple processes dan resources?
## C. Tujuan  
1. Mengimplementasikan program deteksi deadlock berbasis graph untuk menganalisis resource allocation dan request
2. Menjalankan simulasi deteksi deadlock menggunakan dataset uji yang telah ditentukan
3. Mengidentifikasi proses-proses yang terlibat dalam kondisi deadlock
4. Menganalisis hubungan antara circular wait dengan terjadinya deadlock dalam sistem operasi
---
## Metode (Metods)
## A. Lingkungan Uji
Praktikum ini berupa simulasi yang dijalankan dengan sistem operasi windows menggunakan bahasa pemograman python.
## B. Prosedur Eksperimen
1. Menyiapkan dataset uji
2. Menjalankan program dan mencatat output hasil deteksi
3. Memvalidasi hasil dengan analisis manual terhadap dataset
4. Mendokumentasikan hasil dalam bentuk tabel dan screenshot
---
## Hasil (Results)
1. Dataset uji
    | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

    Keterangan:
- Process: Identifier proses (P1, P2, P3)
- Allocation: Resource yang sedang dipegang oleh proses
- Request: Resource yang diminta/dibutuhkan oleh proses
2. Hasik eksekusi program
Program berhasil dijalankan dan menghasilkan output deteksi deadlock. Berikut adalah screenshot hasil eksekusi:
![hasil eksekusi](./screenshots/Screenshot%202025-12-26%20192858.png)
3. Tabel Hasil Deteksi  
Berdasarkan eksekusi program terhadap dataset uji, diperoleh hasil sebagai berikut:


| Proses | Allocation | Request | Status   | Keterangan                         |
|-------:|-----------:|--------:|----------|------------------------------------|
| P1     | R1         | R2      | Deadlock | Terlibat dalam circular wait       |
| P2     | R2         | R3      | Deadlock | Terlibat dalam circular wait       |
| P3     | R3         | R1      | Deadlock | Terlibat dalam circular wait       |

---
## Pembahasan (Discussion)

## A. Interpretasi Hasil
Hasil eksperimen menunjukkan bahwa ketiga proses (P1, P2, P3) terdeteksi berada dalam kondisi deadlock. Hal ini disebabkan oleh adanya circular wait yang terbentuk dalam sistem, di mana:
1. Proses P1 memegang resource R1 tetapi meminta R2 yang sedang dipegang oleh P2
2. Proses P2 memegang resource R2 tetapi meminta R3 yang sedang dipegang oleh P3
3. Proses P3 memegang resource R3 tetapi meminta R1 yang sedang dipegang oleh P1

## B. Analisis Kondisi Deadlock
Berdasarkan hasil uji kondisi deadlock terpenuhi dalam eksperimen ini:
1. Mutual Exclusion: Setiap resource (R1, R2, R3) hanya dapat digunakan oleh satu proses pada satu waktu. Resource tidak dapat di-share.
2. Hold and Wait: Setiap proses memegang minimal satu resource (Allocation) sambil menunggu resource lain (Request). Misalnya, P1 memegang R1 sambil menunggu R2.
3. No Preemption: Resource yang sudah dialokasikan tidak dapat diambil paksa.
4. Circular Wait: Terdapat rantai siklik dari proses P1, P2, P3 di mana setiap proses menunggu resource yang dipegang oleh proses berikutnya dalam rantai.

Karena keempat kondisi ini terpenuhi maka sistem dipastikan berada dalam kondisi deadlock.

---
## Kesimpulan
Berdasarkan hasil percobaan dan analisis yang telah dilakukan, dapat disimpulkan bahwa penerapan algoritma deteksi deadlock dengan dasar alokasi sumber daya dapat mengenali situasi deadlock dengan tepat pada kumpulan data yang diuji. Dari hasil pengujian, tampak bahwa ketiga proses, yaitu P1, P2, dan P3, terdeteksi dalam situasi deadlock.

Penyebab utama terjadinya deadlock dalam percobaan ini adalah adanya pembentukan lingkaran tunggu, di mana proses-proses saling menunggu dalam permintaan sumber daya. Contohnya, P1 menunggu sumber daya yang dipegang oleh P2, P2 menunggu sumber daya yang dimiliki oleh P3, dan P3 menunggu sumber daya yang dipegang oleh P1. Situasi ini membuat sistem tidak bisa melanjutkan proses tanpa campur tangan dari luar.

## Daftar Pustaka
Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). Operating System Concepts (10th ed.). Wiley.
Tanenbaum, A. S., & Bos, H. (2015). Modern Operating Systems (4th ed.). Pearson.
