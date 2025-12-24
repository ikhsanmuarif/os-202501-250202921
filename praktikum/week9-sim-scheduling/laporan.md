
# Laporan Praktikum Minggu 9
Topik: Simulasi Algoritma Penjadwalan CPU  

---

## Identitas
- **Nama**  : ikhsan mu'arif  
- **NIM**   : 250202921  
- **Kelas** : 1IKRB  

---

## Tujuan
Setelah menyelesaikan praktikum ini, mahasiswa mampu:
1. Membuat program simulasi algoritma penjadwalan CPU FCFS dan SJF.
2. Menjalankan program menggunakan dataset uji.
3. Menyajikan hasil simulasi dalam bentuk tabel.
4. Menjelaskan hasil simulasi secara tertulis.
5. Mengunggah kode dan laporan ke repository Git.

---

## Dasar Teori
1. CPU Scheduling adalah mekanisme sistem operasi untuk menentukan proses mana yang dieksekusi oleh CPU.
2. FCFS (First Come First Served) mengeksekusi proses berdasarkan urutan kedatangan.
3. SJF (Shortest Job First) mengeksekusi proses dengan burst time terpendek terlebih dahulu.
4. Waiting Time adalah waktu proses menunggu sebelum dieksekusi.
5. Turnaround Time adalah total waktu dari proses datang hingga selesai dieksekusi.

---

## Langkah Praktikum

### 1. Menyiapkan Dataset
Dataset proses yang digunakan:

| Proses | Arrival Time | Burst Time |
|-------|--------------|------------|
| P1    | 0            | 6          |
| P2    | 1            | 8          |
| P3    | 2            | 7          |
| P4    | 3            | 3          |

### 2. Implementasi Algoritma
Program dibuat menggunakan bahasa Python untuk mensimulasikan algoritma FCFS dan SJF non-preemptive serta menghitung waiting time dan turnaround time.

### 3. Eksekusi & Validasi
Program dijalankan menggunakan dataset uji dan hasilnya dibandingkan dengan perhitungan manual.

### 4. Analisis
Hasil simulasi dianalisis untuk melihat perbedaan performa antara FCFS dan SJF.

---

## Kode Program
```python
processes = [
    ("P1", 0, 6),
    ("P2", 1, 8),
    ("P3", 2, 7),
    ("P4", 3, 3),
]

def fcfs(processes):
    time = 0
    result = []

    for p in processes:
        pid, arrival, burst = p
        if time < arrival:
            time = arrival
        waiting = time - arrival
        turnaround = waiting + burst
        time += burst
        result.append((pid, waiting, turnaround))

    return result


print("=== FCFS ===")
for p in fcfs(processes):
    print(p)
```

---


## Hasil Eksekusi
![Screenshot hasil](./screenshots/Screenshot%202025-12-25%20013852.png)

---

## Analisis
### 1. Alur Program
Program simulasi penjadwalan CPU menggunakan algoritma First Come First Served (FCFS). Dataset proses disimpan dalam bentuk list tuple yang berisi ID proses, waktu kedatangan (arrival time), dan waktu eksekusi (burst time).

setiap proses akan menghitung Waiting Time yaitu selisih antara waktu CPU saat proses mulai dieksekusi dengan waktu kedatangan. Turnaround Time yaitu total waktu proses berada di sistem (waiting time + burst time). Hasil perhitungan disimpan dan ditampilkan dalam bentuk tabel sederhana di terminal.

### 2. Perbandingan Hasil Simulasi dengan Perhitungan Manual  

Hasil dari simulasi menunjukkan bahwa nilai waktu tunggu dan waktu putar sama persis dengan hasil perhitungan manual yang telah dilakukan pada praktikum sebelumnya. Ini membuktikan bahwa algoritma FCFS telah diimplementasikan dengan akurat. Simulasi ini membantu untuk memverifikasi perhitungan manual dan mengurangi kemungkinan terjadi kesalahan hitung, terutama ketika jumlah proses semakin banyak.

### 3. kelebihan dan Keterbatasan Simulasi

Kelebihan: Mempercepat proses perhitungan dibandingkan metode manual, Mengurangi kesalahan dalam perhitungan, Membantu memahami alur kerja algoritma scheduling secara praktis.

Keterbatasan: Simulasi bersifat sederhana Tidak mempertimbangkan faktor seperti context switching dan prioritas proses.

---

## Kesimpulan
- Simulasi algoritma penjadwalan CPU menggunakan FCFS berhasil dilakukan dan menghasilkan nilai waiting time serta turnaround time yang sesuai dengan perhitungan manual.
- Penggunaan simulasi berbasis program sangat membantu dalam memahami konsep penjadwalan CPU serta meningkatkan efisiensi dan akurasi perhitungan.

---

## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?  
   Simulasi memungkinkan pengujian algoritma secara otomatis dan akurat tanpa perhitungan manual.

2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?  
   Simulasi lebih cepat, konsisten, dan minim kesalahan dibandingkan manual.

3. Algoritma mana yang lebih mudah diimplementasikan?  
   FCFS lebih mudah karena hanya berdasarkan urutan kedatangan.

---

## Refleksi Diri
Bagian paling menantang adalah memahami alur scheduling SJF. Hal ini diatasi dengan mencoba simulasi manual sebelum mengimplementasikan kode.

---

**Credit:**  
Template laporan praktikum Sistem Operasi – Universitas Putra Bangsa
