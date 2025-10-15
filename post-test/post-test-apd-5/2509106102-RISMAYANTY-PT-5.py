# manajemen data member pilates

print("\n" + "="*60)
print("🎀 SELAMAT DATANG DI STUDIO PILATES SHAIN 🎀".center(60))
print("="*60)

# registration moment
users = []         
pilates_shain = [] 

registrasi_selesai = False
while not registrasi_selesai:
    print("\n=== ✮ REGISTRASI AKUN ✮ ===")
    id_user = input("MASUKKAN ID (4 angka saja): ")
    nama = input("MASUKKAN NAMA: ")
    usia = input("MASUKKAN USIA: ")
    role = input("MASUKKAN ROLE (admin/member): ")
    paket = input("PAKET PILATES (BASIC / FOAM / LEGS / FULL / RINGAN): ")
    durasi = input("DURASI MEMBERSHIP (bulan): ")

    if role == "admin" or role == "member":
        # cek ID udah terdaftar atau belum
        id_sama = False
        i = 0
        while i < len(users):
            if users[i][0] == id_user:
                print("ID SUDAH TERDAFTAR, GUNAKAN ID LAIN.")
                id_sama = True
                break
            i += 1

        if not id_sama:
            users.append([id_user, nama, usia, role])
            print("☆ REGISTRASI BERHASIL! ☆")
            registrasi_selesai = True
    else:
        print("ROLE TIDAK VALID! PILIH HANYA (admin/member)")

# login
login_gagal = 0
login_berhasil = False
role_user = ""

while login_gagal < 3 and not login_berhasil:
    print("\n" + "="*60)
    print("𝜗ৎ LOGIN USER 𝜗ৎ".center(60))
    print("="*60)

    id_in = input("MASUKKAN ID (4 angka saja): ")
    nama_in = input("MASUKKAN NAMA: ")
    usia_in = input("MASUKKAN USIA: ")
    role_in = input("MASUKKAN ROLE (admin/member): ")
    paket = input("PAKET PILATES (BASIC / FOAM / LEGS / FULL / RINGAN): ")
    durasi = input("DURASI MEMBERSHIP (bulan): ")

    i = 0
    while i < len(users):
        if (id_in == users[i][0] and nama_in == users[i][1] and 
            usia_in == users[i][2] and role_in == users[i][3]):
            login_berhasil = True
            role_user = users[i][3]
            break
        i += 1

    if login_berhasil:
        print("☆ LOGIN BERHASIL SEBAGAI", role_in)
    else:
        login_gagal += 1
        print("LOGIN GAGAL! SILAHKAN COBA LAGI.")
        print(f"Percobaan tersisa: {3 - login_gagal}")

if not login_berhasil:
    print("ANDA GAGAL LOGIN 3 KALI, PROGRAM BERHENTI")
    exit()

# menu admin
if login_berhasil and role_user == "admin":
    admin_berjalan = True
    while admin_berjalan:
        print("\n" + "="*60)
        print("🎀 MANAJEMEN DATA MEMBER PILATES 🎀".center(60))
        print("="*60)
        print("1. TAMBAH DATA")
        print("2. TAMPILKAN DATA")
        print("3. UBAH DATA")
        print("4. HAPUS DATA")
        print("5. KELUAR")
        print("="*60)

        pilih = input("PILIH MENU: ")

        if pilih == "1":
            id = input("ID MEMBER: ")
            paket = input("PAKET PILATES (BASIC / FOAM / LEGS / FULL / RINGAN): ")
            durasi = input("DURASI MEMBERSHIP (bulan): ")
            pilates_shain.append([id, paket, durasi])
            print("DATA BERHASIL DITAMBAHKAN")

        elif pilih == "2":
            if len(pilates_shain) == 0:
                print("YAHHH (╥﹏╥)... BELUM ADA MEMBER")
            else:
                print("\n=== DAFTAR MEMBER PILATES ===")
                i = 0
                while i < len(pilates_shain):
                    print(f"\nMember ke-{i+1}")
                    print(f"ID: {pilates_shain[i][0]}")
                    print(f"PAKET: {pilates_shain[i][1]}")
                    print(f"DURASI: {pilates_shain[i][2]} bulan")
                    i += 1

        elif pilih == "3":
            data_lama = input("MASUKKAN ID MEMBER YANG INGIN DIUBAH: ")
            ditemukan = False
            i = 0
            while i < len(pilates_shain):
                if data_lama == pilates_shain[i][0]:
                    print("\n=== UBAH DATA ===")
                    pilates_shain[i][0] = input("ID BARU: ")
                    pilates_shain[i][1] = input("PAKET BARU: ")
                    pilates_shain[i][2] = input("DURASI BARU (bulan): ")
                    print("DATA BERHASIL DIUBAH")
                    ditemukan = True
                    break
                i += 1
            if not ditemukan:
                print("DATA TIDAK DITEMUKAN")

        elif pilih == "4":
            data_hapus = input("MASUKKAN ID MEMBER YANG INGIN DIHAPUS: ")
            ditemukan = False
            i = 0
            while i < len(pilates_shain):
                if data_hapus == pilates_shain[i][0]:
                    del pilates_shain[i]
                    print("DATA BERHASIL DIHAPUS")
                    ditemukan = True
                    break
                i += 1
            if not ditemukan:
                print("(╥﹏╥) DATA TIDAK DITEMUKAN")

        elif pilih == "5":
            print("𑣲 TERIMA KASIH TELAH MENGUNJUNGI MANAJEMEN DATA MEMBER PILATES")
            admin_berjalan = False

        else:
            print("PILIHAN TIDAK VALID")

# menu member
elif login_berhasil and role_user == "member":
    print("\n" + "="*60)
    print("🎀 SELAMAT DATANG MEMBER PILATES SHAIN 🎀".center(60))
    print("="*60)
    print("𑣲 TERIMA KASIH SUDAH MENJADI BAGIAN DARI PILATES SHAIN")
    print("FYI -> HANYA ADMIN YANG DAPAT MELIHAT DATA")