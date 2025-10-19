# TUPLE -PAKAI KURUNG

# anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
# print(anggota)


# anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))
# manggil 1 elemen niee
# print(anggota[1])
# print(anggota[-1])

# ('samarinda', 12)
# manggil elemen di gdalam nested tuple
# print(anggota[5][0])



# NYISIPKAN ELEMEN

# studyclub = ("Data Science", "Robotics", "Multimedia", "Network")
# diubah dulu jadi list (biar bisa diubah)
# liststudy=list(studyclub)

# liststudy.insert(2,"Web")
# ubah lagi list jadi tuple (habis disisipkan anunya tadi)
# studyclub=tuple(liststudy)
# print(studyclub)


# UNPACK TUPLE
# kasih variabel
# (PTI, orsikom, basisdata) = tugas
# print(PTI)
# print(orsikom)
# print(basisdata)

# barang = ('triangle','bola', 'meja', 'handphone', 'televisi')
# (segitiga, bulat, *kotak) = barang
# print(segitiga)
# print(bulat)
# print(kotak)



# walaupun tuple statis, tapi dia tetep bisa ngegabung (pake + kaya list tadi)