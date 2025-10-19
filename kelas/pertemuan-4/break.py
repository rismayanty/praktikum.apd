angka = [2, 5, 8, 12, 15, 7, 20]
print("Mencari angka pertama yang lebih besar dari 10...")
for n in angka:
# n itu jumlah yg ada di dalam list
    print(f"Sekarang memeriksa angka: {n}")
    if n > 10:
        print(f"Angka {n} lebih besar dari 10, Perulangan berhenti.")
        break 
# break itu perintah biar dia berhenti, kalau udh nemu angka lebih besar dari 10

print("Program selesai.")

