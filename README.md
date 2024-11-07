# Simulasi Scheduling Algorithm

Proyek ini adalah simulasi dari berbagai proses Scheduling Algorithm menggunakan Python. Simulasi dilakukan untuk menganalisis dan membandingkan kinerja dari lima algoritma penjadwalan berbeda dalam menentukan algoritma yang paling optimal dan yang paling kurang efisien.

## Anggota Kelompok
1. Edrick Saputra Lionard
2. Deny Wahyudi Asaloei
3. Chaiden Richardo Foanto
4. A. Alfian Tenggara Putra

## Daftar Algoritma
Proyek ini mencakup lima algoritma penjadwalan:
1. **First Come First Serve (FCFS)**
2. **Shortest Job First Non-preemptive (SJF-NP)**
3. **Shortest Job First Preemptive (SJF-P)**
4. **Longest Job First Preemptive (LJF-P)**
5. **Round Robin (RR)** dengan quantum time 12

## Kriteria Evaluasi
Algoritma dievaluasi berdasarkan beberapa kriteria:
- **Average Waiting Time (AWT)**: Waktu rata-rata proses menunggu dalam antrian (semakin rendah semakin baik).
- **Average Turnaround Time (ATT)**: Waktu rata-rata yang dibutuhkan untuk menyelesaikan proses (semakin rendah semakin baik).
- **Fairness**: Keadilan dalam pembagian CPU dan menghindari starvation.
- **Response Time**: Waktu yang dibutuhkan untuk mulai merespon proses (semakin cepat semakin baik).

## Hasil Simulasi
Rata-rata hasil simulasi untuk setiap algoritma berdasarkan kriteria di atas adalah sebagai berikut:

| Algoritma | AWT  | ATT  | Fairness | Response Time |
|-----------|------|------|----------|---------------|
| FCFS      | 45.5 | 58.3 | 0.70     | 12.0          |
| SJF-NP    | 32.1 | 42.5 | 0.80     | 10.5          |
| SJF-P     | 30.2 | 40.8 | 0.85     | 9.8           |
| LJF-P     | 53.7 | 65.4 | 0.60     | 15.3          |
| RR        | 40.0 | 50.2 | 0.75     | 13.2          |
| **Rata-Rata** | **40.3** | **51.44** | **0.74** | **12.16**     |

### Kesimpulan
- **Algoritma Terbaik**: SJF Preemptive, karena memberikan waktu tunggu rata-rata (AWT) paling rendah dan optimal untuk data dengan variasi burst time.
- **Algoritma Terburuk**: LJF Preemptive, karena menghasilkan waktu tunggu yang tinggi dan kurang efisien untuk proses-proses pendek.

## File dalam Repository
- `fcfs.py`, `sjf_non_preemptive.py`, `sjf_preemptive.py`, `ljf_preemptive.py`, `round_robin.py`: Script Python untuk setiap algoritma penjadwalan.
- `processes.xlsx`: File Excel yang berisi data proses yang digunakan dalam simulasi.
- `output_fcfs.xlsx`, `output_sjf_non_preemptive.xlsx`, dll.: Hasil output dari setiap algoritma dalam format Excel.
- `Analisa_Scheduling_Algorithm.pdf`: Laporan analisis lengkap yang mencakup hasil simulasi dan perbandingan performa algoritma.

## Cara Menjalankan
1. Pastikan Python dan pustaka yang diperlukan (`pandas`, `openpyxl`, dll.) sudah terinstal.
2. Jalankan setiap file Python untuk menjalankan simulasi per algoritma.
   ```bash
   python fcfs.py
   python sjf_non_preemptive.py
   python sjf_preemptive.py
   python ljf_preemptive.py
   python round_robin.py
   ```
3.Hasil simulasi akan disimpan dalam file Excel sesuai dengan algoritma yang dijalankan.
