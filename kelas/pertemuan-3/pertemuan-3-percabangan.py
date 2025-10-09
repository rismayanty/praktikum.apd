pemakaianlistrik = int (input("masukkan:" ))

if pemakasianlistrik == 100:
    tarif = pemakaianlistrik * 1200
elif pemakaianlistrik >= 101 and pemakaianlistrik <= 300:
    tarif = pemakaianlistrik *1500
else:
    tarif = pemakaianlistrik * 2000

print("total gtarif listrik yang harus dibayar: Rp", tarif)



# ternary operator

# nilai = 70
# if nilai = 60:
# status = "Lulus"
# else:
# status = "Tidak Lulus"
# print(status)


# Menggunakan Ternary Operator

# nilai = 70
# status = "Lulus" if nilai = 60 else "Tidak Lulus"
# print(status)



# pertemuan3

# nilai = int (input("masukkan nilai:"))
# if nilai >=80:
#     print ("Nilai A")
# elif nilai >=70:
#     print ("Nilai B")  
# elif nilai >=60:
#     print ("Nilai C")
# else:
#     print ("tidak lulus")

