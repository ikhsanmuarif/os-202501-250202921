
# Laporan Praktikum Minggu 6
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling

---

## Identitas
- **Nama**  : Ikhsan Mu'arif
- **NIM**   : 250202921
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menghitung *waiting time* dan *turnaround time* pada algoritma RR dan Priority.  
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.  
3. Membandingkan performa algoritma RR dan Priority.  
4. Menjelaskan pengaruh *time quantum* dan prioritas terhadap keadilan eksekusi proses.  
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.  
   
---

## Dasar Teori
1. **Round Robin (RR):**  
   Algoritma ini menggunakan time quantum untuk membagi waktu CPU secara bergiliran ke setiap proses, cocok untuk sistem time-sharing.

2. **Priority Scheduling:**  
   Proses dijalankan berdasarkan tingkat prioritas. Proses dengan prioritas lebih tinggi mendapat akses CPU lebih dulu.

3. **Time Quantum:**  
   Ukuran time quantum memengaruhi efisiensi dan responsivitas sistem. Terlalu kecil → overhead tinggi; terlalu besar → proses pendek tertunda.

4. **Starvation:**  
   Pada Priority Scheduling, proses prioritas rendah bisa tidak pernah dijalankan jika selalu ada proses prioritas tinggi.

5. **Pemilihan Algoritma:**  
   Harus disesuaikan dengan kebutuhan sistem, apakah lebih mementingkan keadilan, efisiensi, atau penanganan proses penting.

---

## Langkah Praktikum
1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  
   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | ...
     0    3    6    9   12   15   18  ...
     ```
   - Catat sisa *burst time* tiap putaran.

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | ... | ... | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | ... | ... | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
 *time quantum (q)* = 3.  
 WT[i] = waktu mulai eksekusi - Arrival[i]
 TAT[i] = WT[i] + Burst[i]  

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/tabel.png)
- Gant Chart FCFS
```bash
| P1 | P2 | P3 | P4 | P1 | P3 | P4 | P4 |
0    3    6   9   12   15    18   21  24  
```
- Gant Chart FCFS
```bash
| P1 | P2 | P4 | P3 |
0    5    8   14   22
```
---
## tabel perbandingan
   | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
   |------------|------------------|----------------------|------------|-------------|
   | RR | 11,75 | 12,5 | Setiap proses mendapat giliran eksekusi | Tidak efisien jika quantum tidak tepat |
   | Priority | 5,25 | 10,75 | Cocok untuk sistem yang butuh respons cepat terhadap proses tertentu | Proses yang datang lebih dulu bisa dikalahkan oleh proses baru yang punya prioritas lebih tinggi |
## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?
2. Apa pengaruh besar/kecilnya time quantum terhadap performa sistem?
3. Mengapa algoritma Priority dapat menyebabkan starvation?
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
