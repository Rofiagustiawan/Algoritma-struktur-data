print("=== PROGRAM PERBEDAAN LIST DAN TUPLE (DATA MAHASISWA) ===")

# LIST 

print("\n--- LIST DATA MAHASISWA ---")
list_mahasiswa = []

jumlah = int(input("Berapa banyak mahasiswa yang ingin dimasukkan ke list? "))
for i in range(jumlah):
    nama = input(f"Masukkan nama mahasiswa ke-{i+1}: ")
    list_mahasiswa.append(nama)

print("\nList mahasiswa saat ini:", list_mahasiswa)

# Mengubah list
ubah_index = int(input("Pilih index mahasiswa yang ingin diubah (contoh: 0): "))
nama_baru = input("Masukkan nama mahasiswa baru: ")
list_mahasiswa[ubah_index] = nama_baru

print("List mahasiswa setelah diubah:", list_mahasiswa)


# TUPLE 

print("\n--- TUPLE DATA MAHASISWA ---")
jumlah_tuple = int(input("Berapa banyak mahasiswa yang ingin dimasukkan ke tuple? "))

temp_mhs = []
for i in range(jumlah_tuple):
    nama = input(f"Masukkan nama mahasiswa ke-{i+1}: ")
    temp_mhs.append(nama)

tuple_mahasiswa = tuple(temp_mhs)
print("\nTuple mahasiswa:", tuple_mahasiswa)

print("\nMencoba mengubah tuple... (TIDAK BISA)")
try:
    index = int(input("Pilih index mahasiswa yang ingin diubah pada tuple (contoh: 0): "))
    nama_baru = input("Masukkan nama baru: ")
    tuple_mahasiswa[index] = nama_baru
except TypeError as e:
    print("Error:", e)

print("\nKesimpulan:")
print("List bisa diubah (mutable). Tuples tidak bisa diubah (immutable).")
