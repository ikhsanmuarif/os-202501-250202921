
# Laporan Praktikum Minggu [11]
Topik: Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Ikhsan Mu'arif  
- **NIM**   : 250202921  
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program sederhana untuk mendeteksi deadlock.  
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.  
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.  
4. Memberikan interpretasi hasil uji secara logis dan sistematis.  
5. Menyusun laporan praktikum sesuai format yang ditentukan.
---

## Dasar Teori
Deadlock adalah kondisi ketika dua atau lebih proses saling menunggu sumber daya yang sedang digunakan oleh proses lain sehingga tidak ada proses yang dapat melanjutkan eksekusi.

---

## Langkah Praktikum  
1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

   Contoh tabel:

   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

4. **Analisis Hasil**

   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```python
import csv

def read_dataset(filename):
    processes = []
    allocation = {}
    request = {}

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            p = row['Process']
            processes.append(p)
            allocation[p] = row['Allocation']
            request[p] = row['Request']

    return processes, allocation, request


def detect_deadlock(processes, allocation, request):
    graph = {}

    for p in processes:
        graph[p] = request[p]

    deadlock_processes = []

    for p in processes:
        visited = set()
        current = p

        while current not in visited:
            visited.add(current)
            next_resource = graph[current]

            found = False
            for q in processes:
                if allocation[q] == next_resource:
                    current = q
                    found = True
                    break

            if not found:
                break
        else:
            deadlock_processes.extend(list(visited))

    return set(deadlock_processes)


if __name__ == "__main__":
    processes, allocation, request = read_dataset("dataset_deadlock.csv")
    deadlock = detect_deadlock(processes, allocation, request)

    print("=== HASIL DETEKSI DEADLOCK ===")
    if deadlock:
        print("Deadlock terdeteksi pada proses:")
        for p in deadlock:
            print("-", p)
    else:
        print("Tidak terjadi deadlock")

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/Screenshot%202025-12-26%20192858.png)

---

## Analisis
### 1. Tabel hasil deteksi deadlock  
| Proses |  Status Deadlock  |
| :----: | :---------------: |
|   P2   | Deadlock |
|   P3   | Deadlock |
|   P1   | Deadlock |
---
Deadlock terjadi karena adanya circular wait, di mana P1 menunggu resource R2 yang dipegang P2, P2 menunggu R3 yang dipegang P3, dan P3 menunggu R1 yang dipegang P1. Kondisi ini menyebabkan tidak ada satu pun proses yang dapat melanjutkan eksekusi. Hasil ini sesuai dengan teori deadlock karena keempat kondisi deadlock terpenuhi, yaitu mutual exclusion, hold and wait, no preemption, dan circular wait jadi sistem dinyatakan deadlock.
## Kesimpulan
Deadlock terjadi akibat circular wait antar proses yang saling menunggu resource. Simulasi ini membuktikan deteksi deadlock penting dalam sistem operasi untuk menjaga stabilitas dan ketersediaan resource.

---

## Quiz
1. Apa perbedaan antara *deadlock prevention*, *avoidance*, dan *detection*?  
- deadlock prevetion yaiut mencegah kemungkinan deadlock tejadi dari awal dengan memastikan salahsatu dari empat kondisi yang menyebabkan deadlock tidak pernah terjadi.  
- Deadlock avoidance adalah pendekatan yang mencegah sistem masuk ke unsafe state, yaitu kondisi yang bisa menyebabkan deadlock. Strategi ini memerlukan informasi tentang permintaan sumber daya di masa depan.  
- Deadlock detection adalah pendekatan yang membiarkan deadlock terjadi, kemudian sistem memeriksa secara periodik apakah deadlock terjadi dan mengambil tindakan (mis. membatalkan proses) untuk recover/recover dari deadlock.
2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?  
karena dalam sistem operasi terjadi kondisi ketika sejumlah proses saling menunggu sumber daya yang sedang digunakan proses lain, sehingga eksekusi tidak dapat berlanjut. Tanpa mekanisme pendeteksian akan membuat sistem tidak responsif. sistem operasi perlu mengenali situasi tersebut dan melakukan tindakan pemulihan agar kinerja tetap berjalan normal.
3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?  
kelebihan: sistem tidak perlu membatasi penggunaan resource secara ketat, sehingga tingkat pemanfaatan resource menjadi lebih efisien dan fleksibel.  
kekurangan: deadlock dibiarkan terjadi terlebih dahulu sebelum terdeteksi, yang dapat menyebabkan penurunan kinerja sistem. Selain itu, sistem memerlukan mekanisme tambahan untuk mendeteksi dan memulihkan deadlock, sehingga menimbulkan overhead komputasi.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
 semuanya menantang
- Bagaimana cara Anda mengatasinya?  
 solat lima waktu

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
