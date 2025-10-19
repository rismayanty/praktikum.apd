# kunci/key yang kiri, value/nilai yang kanan
# item itu gabungan key dan value
# Daftar_buku = { 
#     "Buku1" : "Bumi Manusia", 
#     "Buku2" : "Laut Bercerita",
#     "Buku3" : "Anak Semua Bangsa" 
# }

# ini ngeprint langsung sekali, tapi sederet
# print(Daftar_buku["Buku2"])
# print(Daftar_buku)


# karena "value" itu cuman variabel, mau diganti apapun bakal tetap key yang tampil
# sifat dari perulangan, makanya yang nampil cuman key
# for values in Daftar_buku:
#     print(values)

# for duar in Daftar_buku.keys():
#     print(duar)



# ini buat nampilin values
# for duar in Daftar_buku.values():
#     print(duar)


# kalau mau manggil dua duanya, pake item
# nah ini nampilin satu satu, per baris

# for duar in Daftar_buku.items():
#     print(duar)








# Biodata = { 
# "Nama" : "Ananda Daffa Harahap", 
# "NIM" : 2409106050, 
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data",
#         "Jaringan Komputer", "Sistem Operasi"], 
# "Mahasiswa_Aktif" : True, 
# "Social Media" : {"Instagram" : "daffahrhap" 
#     }
# }

# print(Biodata["Nama"])
# print(Biodata["KRS"][1])
# print(Biodata["KRS"])
# print(Biodata["Social Media"]["Instagram"])

# print dari belakang
# print(Biodata["KRS"][-1])

# print(Biodata["KRS"][1:4:2])
# print(Biodata["KRS"][1:5])


# list_nama= dict(mahasiswa1 = "Dapupu", mahasiswa2 = "Bambang",
#                 mahasiswa3 = "")



# print(f"nama saya adalah {Biodata["Nama"]}") 
# print(f"Instagram : {Biodata['Social Media']['Instagram']}") 
 
# print(f"nama saya adalah {Biodata.get("Nama")}") 


# nambahin item
# Film = { 
# "Avenger Endgame" : "Action", 
# "Sherlock Holmes" : "Mystery", 
# "The Conjuring" : "Horror" 
# }

# Sebelum Ditambah 
#  print(Film) 
 
# Film["Zombieland"] = "Comedy" 
# Film.update({"Hours" : "Thriller"}) 
# Setelah Ditambah 
# print(Film) 
 
# Sebelum Ditambah 
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery', 
# 'The Conjuring': 'Horror'} 
 
# Setelah Ditambah 
# {'Avenger Endgame': 'Action', 'Sherlock Holmes': 'Mystery', 
# 'The Conjuring': 'Horror', 'Zombieland': 'Comedy', 'Hours': 
# 'Thriller'}


# pakai del
# data = { 
# "Nama" : "Daffa", 
# "Umur" : 19, 
# "Jurusan" : "Informatika" 
# } 
# Sebelum Dihapus 
# print(data) 
 
# del data["Nama"] 
 
# Setelah diubah 
# print(data) 
 
# memanggil data yang telah dihapus 
# print(data.get("Nama")) 
 
# {'Nama': 'Daffa', 'Umur': 19, 'Jurusan': 'Informatika'} 
 
# {'Umur': 19, 'Jurusan': 'Informatika'}



# clear
# data = { 
# "Nama" : "Daffa", 
# "Umur" : 19, 
# "Jurusan" : "Informatika" 
# } 
 
# #Sebelum Dihapus 
# print(data) 
 
# data.clear() 
 
#Setelah dihapus 
# print(data) 
 

# data = { 
# "Nama" : "Daffa", 
# "Umur" : 19, 
# "Jurusan" : "Informatika" 
# }
# print("Jumlah Data = ", len(data)) 


# copy
# buku = { 
#  "Buku1" : "Bumi Manusia", 
#  "Buku2" : "Laut Bercerita" 
# } 
 
# pinjam = buku.copy() 
# pinjam = buku.copy() 
# print("Dictionary yang telah disalin : ", pinjam)

# key = "apel", "jeruk", "mangga", "pisang"
 
# value = "Buah Favorite"
 
# buah = dict.fromkeys(key, value) 
 
# print(buah) 








# nested dictionary
Musik = { 
"The Chainsmoker" : ["All we Know", "The Paris"], 
"Alan Walker" : ["Alone", "Lily"], 
"Neffex" : ["Best of Me", "Memories"] 
} 
 
for penyanyi, album in Musik.items(): 
 print(f"Musik milik {penyanyi} adalah : ") 
 for song in album: 
  print(song) 
 print("")