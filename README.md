# time-server-thread
## Tugas 2 Pemrograman Jaringan Kelas C

Untuk menjalankan program bisa dilakukan melalui lokal ataupun menggunakan docker yang tersedia di repository <a href="https://github.com/rm77/progjar">ini</a>

Untuk pengetesan yang saya lakukan, saya menggunakan docker yang ada di repositori di atas lalu menjalankan 2 mesin virtual (mesin1 dan mesin2), kemudian mengcapture nya menggunakan interface eth1 wireshark virtual yang tersedia.

###  Cara pengetesan
1. Buka wireshark di salah satu mesin dengan mengakses `localhost:[port]`, contoh wireshark dari mesin1:
```
localhost:50001
```
2. Start capture dari interface eth1
3. Jalankan program `tugas2-server.py` di mesin1
```
python3 tugas2-server.py
```
4. Jalankan program `tugas2-client.py` di mesin2 atau mesin3
```
python3 tugas2-client.py
```