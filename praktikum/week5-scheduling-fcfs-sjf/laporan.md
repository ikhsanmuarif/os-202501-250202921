
# Laporan Praktikum Minggu [5]
Topik: Penjadwalan CPU – FCFS dan SJF


---

## Identitas
- **Nama**  : Ikhsan Mu'arif
- **NIM**   : 250202921  
- **Kelas** : 1IKRB

---

## Tujuan
Tujuan utamanya adalah memahami bagaimana sistem operasi menentukan urutan eksekusi proses, serta bagaimana waiting time dan turnaround time memengaruhi performa sistem.
---

## Dasar Teori
1. mempelajari dan memahami konsep proses dan urutan eksekusi proses.
2. menghitung rata-rata waiting time dan turnaround time.
    
---

## Langkah Praktikum
1. Siapkan Data Proses Gunakan tabel proses
2. **Eksperimen 1 – FCFS (First Come First Served)**
   - Urutkan proses berdasarkan *Arrival Time*.  
   - Hitung nilai berikut untuk tiap proses:
     ```
     Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
     Turnaround Time (TAT) = WT + Burst Time
     ```
   - Hitung rata-rata Waiting Time dan Turnaround Time.  
   - Buat Gantt Chart sederhana:  
     ```
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24
     ```

3. **Eksperimen 2 – SJF (Shortest Job First)**
   - Urutkan proses berdasarkan *Burst Time* terpendek (dengan memperhatikan waktu kedatangan).  
   - Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.  
   - Bandingkan hasil FCFS dan SJF pada tabel berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | FCFS | ... | ... | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
     | SJF | ... | ... | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

4. **Eksperimen 3 – Visualisasi Spreadsheet (Opsional)**
   - Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
     - Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
     - Gunakan formula dasar penjumlahan/subtraksi.
   - Screenshot hasil perhitungan dan simpan di:
     ```
     praktikum/week5-scheduling-fcfs-sjf/screenshots/
     ```

5. **Analisis**
   - Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.  
   - Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  
   - Tambahkan kesimpulan singkat di akhir laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
   git push origin main

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
Turnaround Time (TAT) = WT + Burst Time
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/Gantt%20Chart.png)

---

## Analisis
-  **Eksperimen 1 – FCFS (First Come First Served)**
```
  | P1 | P2 | P3 | P4 |
  0    6    14   21   24
```
- **Eksperimen 2 – SJF (Shortest Job First)**
```
  | P1 | P4 | P3 | P2 |
  0    6    9   16   24
```
- **Tabel hasil FCFS dan SJF**
  
| Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
|------------|------------------|----------------------|------------|-------------|
| FCFS | 8,75 | 14,75 | Sederhana dan mudah diterapkan. | Tidak efisien untuk proses panjang. |
| SJF | 6,5 | 12,5 | Optimal untuk job pendek. | Menyebabkan starvation pada job panjang. |

---

## Kesimpulan
- SJF (Shortest Job First) rata-rata waiting time nya  dan juga Waktu Penyelesaiannya (Turnaround Time) rata-rata lebih rendah dibandingkan FCFS (First Come First Served).
- FCFS lebih sederhana tetapi tidak efisien untuk proses dengan burst time panjang. Sedangkan SJF akan mengeksekusi proses-proses kecil terlebih dahulu, sehingga waktu tunggu rata-rata menjadi sangat rendah.
- FCFS cocok digunakan untuk sistem yang tidak memerlukan efisiensi tinggi dan prosesnya sederhana, sedangkan SJF lebih cocok untuk sistem proses dengan burst pendek yang dapat di prediksi.
---

## Quiz
1. Apa perbedaan utama antara FCFS dan SJF?  
   FCFS Proses yang tiba lebih dulu menjadi yang terdepan dalam antrean, sementara proses yang datang setelahnya ditambahkan ke bagian belakang antrean. sedangkan SJF proses dengan waktu burst terpendek diproses terlebih dahulu.
2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?  
   karena SJF  menjalankan proses yang lebih pendek terlebih dahulu
3. Apa kelemahan SJF jika diterapkan pada sistem interaktif?  
   proses yang panjang akan mempunyai waktu tunggu yang lama karena proses yang lebih cepat akan dieksekusi lebih dahulu

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
  Menghitung waiting time dan turnaround time untuk algoritma FCFS dan SJF.
- Bagaimana cara Anda mengatasinya?  
  belajar memahami lewat google

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
