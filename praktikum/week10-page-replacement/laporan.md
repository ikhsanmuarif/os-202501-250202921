
# Laporan Praktikum Minggu 10  
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas
- **Nama**  : Ikhsan Mu'arif 
- **NIM**   : 250202921  
- **KELAS** : 1IKRB

---

## Tujuan
Tujuan dari praktikum ini adalah untuk memahami konsep manajemen memori virtual pada sistem operasi, khususnya mekanisme page replacement, serta membandingkan performa algoritma FIFO (First-In First-Out) dan LRU (Least Recently Used) berdasarkan jumlah page fault yang dihasilkan.

---

## Dasar Teori
1. Manajemen Memori Virtual memungkinkan sistem operasi menjalankan program yang ukuran memorinya melebihi kapasitas memori utama.
2. Page Fault terjadi ketika halaman yang dibutuhkan proses tidak berada di memori utama.
3. Page Replacement Algorithm digunakan untuk menentukan halaman mana yang akan diganti saat memori penuh.
4. FIFO (First-In First-Out) mengganti halaman yang pertama kali masuk ke memori tanpa mempertimbangkan frekuensi penggunaannya.
5. LRU (Least Recently Used) mengganti halaman yang paling lama tidak digunakan berdasarkan riwayat akses.

---

## Langkah Praktikum
1. Menentukan reference string sebagai data uji.
2. Menentukan jumlah frame memori.
3. Mengimplementasikan algoritma FIFO.
4. Mengimplementasikan algoritma LRU.
5. Menjalankan simulasi page replacement.
6. Mencatat jumlah page fault dari masing-masing algoritma.
7. Menganalisis dan membandingkan hasil simulasi.
8. Melakukan commit dan push ke repository GitHub.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```python
# Simulasi Page Replacement FIFO dan LRU
# Praktikum Sistem Operasi - Bab 10

def fifo(reference, frames):
    memory = []
    page_fault = 0
    pointer = 0

    print("=== FIFO ===")
    for page in reference:
        if page not in memory:
            page_fault += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory[pointer] = page
                pointer = (pointer + 1) % frames
            status = "Page Fault"
        else:
            status = "Page Hit"

        print(f"Page {page} -> {memory} ({status})")

    return page_fault


def lru(reference, frames):
    memory = []
    page_fault = 0
    last_used = {}

    print("\n=== LRU ===")
    for i, page in enumerate(reference):
        if page not in memory:
            page_fault += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = min(last_used, key=last_used.get)
                memory[memory.index(lru_page)] = page
                del last_used[lru_page]
            status = "Page Fault"
        else:
            status = "Page Hit"

        last_used[page] = i
        print(f"Page {page} -> {memory} ({status})")

    return page_fault


if __name__ == "__main__":
    reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frames = 3

    print("Reference String:", reference_string)
    print("Jumlah Frame:", frames)

    fifo_fault = fifo(reference_string, frames)
    lru_fault = lru(reference_string, frames)

    print("\n=== Perbandingan Akhir ===")
    print("FIFO Page Fault:", fifo_fault)
    print("LRU Page Fault :", lru_fault)

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/Screenshot%202025-12-25%20125318.png)

---

## Analisis
### 1. Tabel Perbandingan Algoritma  

| Algoritma | Jumlah Page Fault | Keterangan                              |
| --------- | ----------------- | --------------------------------------- |
| FIFO      | 10                | Menutup halaman berdasarkan waktu masuk tanpa mempertimbangkan pola akses       |
| LRU       | 9                 | Mengganti halaman yang jarang digunakan |


### 2. Analisis Perbedaan Page Fault  
Jumlah page fault yang dihasilkan oleh algoritma FIFO dan LRU dapat berbeda karena strategi penggantian halaman yang digunakan oleh masing-masing algoritma tidak sama.  
### 3. Analisis algoritma mana yang lebih efisien  
Algoritma LRU menghasilkan lebih sedikit kesalahan halaman jika dibandingkan dengan FIFO, sehingga dapat disimpulkan bahwa LRU memiliki efisiensi yang lebih baik. Tingkat efisiensi LRU diperoleh dari kemampuannya dalam menyesuaikan penggantian halaman berdasarkan pola akses proses, meskipun cara kerjanya lebih rumit dibandingkan FIFO.

---

## Kesimpulan
Algoritma Page Replecement menentukan halaman mana yang harus dihapus saat terjadinya page fault dan ketika memori utama telah terisi penuh.

Hasil dari simulasi menunjukkan bahwa algoritma FIFO mempunyai implementasi yang sederhana, tetapi kurang efisien karena tidak memperhatikan pola penggunaan halaman dan dapat mengalami Anomali Belady. Di sisi lain, algoritma LRU dapat menghasilkan lebih sedikit page fault karena mempertimbangkan riwayat penggunaan halaman, sehingga lebih sesuai dengan cara program mengakses data.

Oleh karena itu, algoritma LRU lebih efisien dibandingkan dengan FIFO dalam pengelolaan memori, meskipun tingkat kompleksitas dalam penerapannya lebih tinggi.

---

## Quiz
1. Apa Perbedaan utama FIFO dan LRU?   
   **Jawaban:**  Perbedaan utama antara FIFO dan LRU terletak pada cara mengganti data. FIFO mengganti data yang masuk lebih dulu, sedangkan LRU mengganti data yang paling lama tidak digunakan.
2. Mengapa FIFO dapat menyebabkan Belady’s Anomaly?  
**Jawaban:** Karena penambahan jumlah frame tidak selalu menurunkan jumlah page fault pada FIFO.
3. Mengapa LRU lebih efisien dibanding FIFO?  
   **Jawaban:** karena LRU mengganti halaman yang paling jarang digunakan, bukan yang paling lama masuk, sehingga mengurangi page fault (kesalahan halaman) dengan lebih baik karena cenderung mempertahankan halaman yang sering diakses ulang 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
 memahami konsep mwkanisme Page Replacement FIFO dan LRU.
- Bagaimana cara Anda mengatasinya?  
 Mengerjakan tugas sambil memahami lewat google.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
