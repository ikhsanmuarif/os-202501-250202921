# Perbedaan monolithic kernel, microkernel, dan layered architecture.

Kernel adalah inti dari sebuah sistem operasi yang menghubungkan perangkat keras (hardware) dan perangkat lunak (software). Kernel bertugas untuk mengatur berbagai sumber daya dalam komputer, seperti CPU, memori, dan perangkat input/output. Dalam istilah sederhana, kernel bertindak sebagai pengatur lalu lintas data antara aplikasi yang kamu gunakan dan perangkat keras yang mendasari sistem operasimu. Fungsi utama dari Kernel Sistem Operasi adalah untuk memastikan bahwa setiap proses dalam sistem berjalan dengan efisien dan tidak saling mengganggu satu sama lain. Kernel bekerja di tingkat rendah, artinya ia beroperasi langsung dengan perangkat keras, tetapi memberikan layanan yang diperlukan oleh aplikasi dan program yang berjalan di atasnya. Tanpa kernel, perangkat lunak tidak dapat berinteraksi dengan perangkat keras secara efektif.

## Monolitic kernel
 merupakan suatu arsitektur kernel yang melengkapi keseluruhan sistem operasi supaya berjalan pada ruang kernel dalam modus supervisor. Berbeda dengan arsitektur kernel lainnya, monolitic kernel memberikan layananan virtual perangkat keras secara penuh pada level tingkat tinggi dan dengan layanan pada level tingkat bawah yang bersifat primitif sebagai layanan basis sistem operasi seperti manajemen proses, konkurensi, dan manajemen ingatan dalam satu atau beberapa modul.

## Microkernel
merupakan perangkat lunak dalam jumlah minimum dan meyediakan beragam mekanisme dasar yang dibutuhkan untuk bekerja sebagai sebuah sistem operasi. mikrokernel merupakan satu-satunya perangkat lunak yang berjalan dengan tingkat tertinggi (umumnya disebut sebagai modus supervisor atau modus kernel). Layanan yang disediakan oleh sebuah sistem operasi beberapa diantaranya adalah device driver, protokol jaringan, sistem berkas, dan kode antarmuka pengguna yang berada dalam ruang pengguna.

## Layered architecture
membagi aplikasi menjadi lapisan-lapisan yang memiliki fungsi spesifik. Biasanya terdiri dari lapisan presentasi, logika bisnis, dan data. Ibarat gedung bertingkat di mana setiap lantai punya fungsi khusus.

## Contoh sistem operasi

monolitic kernel : semua komponen utama OS (driver, sistem file, manajemen memori, dll) contoh: Linux(ubuntu, debian, fedora, ,android), BSD(OpenBSD, FreeBSD, NetBSD)
microkernel : Hanya fungsi dasar OS yang dijalankan di mode kernel. contoh: QNX, Minix, GNU hurd.
Layered/Hybrid: Gabungan konsep monolithic dan microkernel contoh : Windows NT dan macOS (XNU kernel) yang menggabungkan konsep microkernel dengan BSD

## Analisis model kernel paling relevan untuk sistem modern:

Model yang paling relevan untuk sistem operasi modern adalah Hybrid Kernel, dengan konsep Monolithic Kernel dan Microkernel yang di gabungkan. Kedua model ini mengombinasikan kinerja tinggi dari kernel monolitik dengan keamanan dan modularitas dari microkernel.
Dalam sistem modern seperti Windows NT, macOS (XNU), dan Android (Linux kernel yang dimodifikasi), pendekatan hybrid digunakan agar sistem tetap cepat namun juga lebih stabil dan aman. Komponen penting seperti manajemen memori dan proses tetap berada di ruang kernel untuk efisiensi, sementara layanan non-esensial seperti device driver tertentu, file system tambahan, atau layanan jaringan berjalan di user space agar lebih mudah diperbarui dan tidak merusak sistem inti bila terjadi kegagalan.
Selain itu, arsitektur hybrid lebih mudah dikembangkan untuk teknologi baru seperti virtualisasi, cloud computing, dan containerization (Docker, Kubernetes) karena struktur modularnya mendukung isolasi proses dan efisiensi sumber daya.