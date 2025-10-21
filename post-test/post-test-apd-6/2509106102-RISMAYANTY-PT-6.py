# manajemen data member pilates 
print("\n" + "="*60)
print("🎀 SELAMAT DATANG DI STUDIO PILATES SHAIN 🎀".center(60))
print("="*60)

# registration moment
users = {}
pilates_shain = {}
registrasi_selesai = False

while not registrasi_selesai:
    print("\n=== ✮ REGISTRASI AKUN ✮ ===")
    id_user = input("MASUKKAN ID (4 angka saja): ")
    nama = input("MASUKKAN NAMA: ")
    usia = input("MASUKKAN USIA: ")
    role = input("MASUKKAN ROLE (admin/member): ")
    
    if role == "admin" or role == "member":
        # cek ID udah terdaftar atau belum
        if id_user in users:
            print("ID SUDAH TERDAFTAR, GUNAKAN ID LAIN.")
        else:
            users[id_user] = {
                "nama": nama,
                "usia": usia,
                "role": role,
                "paket": "",
                "durasi": ""
            }
            print("☆ REGISTRASI BERHASIL! ☆")
            registrasi_selesai = True
    else:
        print("ROLE TIDAK VALID! PILIH HANYA (admin/member)")

# login moment
login_gagal = 0
login_berhasil = False
current_user = None
current_user_id = ""

while login_gagal < 3 and not login_berhasil:
    print("\n" + "="*60)
    print("𝜗ৎ LOGIN USER 𝜗ৎ".center(60))
    print("="*60)
    id_in = input("MASUKKAN ID (4 angka saja): ")
    nama_in = input("MASUKKAN NAMA: ")
    
    if id_in in users:
        user_data = users[id_in]
        if (nama_in == user_data["nama"]):
            login_berhasil = True
            current_user = user_data
            current_user_id = id_in
            break
    
    if not login_berhasil:
        login_gagal += 1
        print("LOGIN GAGAL! SILAHKAN COBA LAGI.")
        print(f"Percobaan tersisa: {3 - login_gagal}")

if not login_berhasil:
    print("ANDA GAGAL LOGIN 3 KALI, PROGRAM BERHENTI")
    exit()

# menu admin 
if login_berhasil and current_user["role"] == "admin":
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
            id_member = input("ID MEMBER: ")
            if id_member in pilates_shain:
                print("ID MEMBER SUDAH TERDAFTAR!")
            else:
                nama = input("NAMA: ")
                paket = input("PAKET PILATES (BASIC / FOAM / LEGS / FULL / RINGAN): ")
                durasi = input("DURASI MEMBERSHIP (bulan): ")
                pilates_shain[id_member] = {
                    "nama": nama,
                    "paket": paket,
                    "durasi": durasi
                }
                print("DATA BERHASIL DITAMBAHKAN")
                
        elif pilih == "2":
            if len(pilates_shain) == 0:
                print("YAHHH (╥﹏╥)... BELUM ADA MEMBER")
            else:
                print("\n=== DAFTAR MEMBER PILATES ===")
                counter = 1
                for id_member, data in pilates_shain.items():
                    print(f"\nMEMBER KE-{counter}")
                    print(f"ID: {id_member}")
                    print(f"NAMA: {data['nama']}")
                    print(f"PAKET: {data['paket']}")
                    print(f"DURASI: {data['durasi']} bulan")
                    counter += 1
                    
        elif pilih == "3":
            data_lama = input("MASUKKAN ID MEMBER YANG INGIN DIUBAH: ")
            if data_lama in pilates_shain:
                print("\n=== UBAH DATA ===")
                print(f"Data lama: Nama {pilates_shain[data_lama]['nama']}, Paket {pilates_shain[data_lama]['paket']}, Durasi {pilates_shain[data_lama]['durasi']} bulan")
                
                ubah_id = input("UBAH ID MEMBER? (y/t): ")
                if ubah_id == 'y':
                    id_baru = input("ID BARU: ")
                    if id_baru in pilates_shain and id_baru != data_lama:
                        print("ID BARU SUDAH TERDAFTAR!")
                    else:
                        data_sementara = pilates_shain[data_lama]
                        del pilates_shain[data_lama]
                        pilates_shain[id_baru] = data_sementara
                        data_lama = id_baru
                
                pilates_shain[data_lama]["nama"] = input("NAMA BARU: ")
                pilates_shain[data_lama]["paket"] = input("PAKET BARU: ")
                pilates_shain[data_lama]["durasi"] = input("DURASI BARU (bulan): ")
                print("DATA BERHASIL DIUBAH")
            else:
                print("DATA TIDAK DITEMUKAN")
                
        elif pilih == "4":
            data_hapus = input("MASUKKAN ID MEMBER YANG INGIN DIHAPUS: ")
            if data_hapus in pilates_shain:
                del pilates_shain[data_hapus]
                print("DATA BERHASIL DIHAPUS")
            else:
                print("(╥﹏╥) DATA TIDAK DITEMUKAN")
                
        elif pilih == "5":
            print("𑣲 TERIMA KASIH SUDAH MENJADI BAGIAN DARI PILATES SHAIN")
            admin_berjalan = False
        else:
            print("PILIHAN TIDAK VALID")

# menu member (CREATE AND READ)
elif login_berhasil and current_user["role"] == "member":
    member_berjalan = True
    while member_berjalan:
        print("\n" + "="*60)
        print("🎀 MENU MEMBER PILATES SHAIN 🎀".center(60))
        print("="*60)
        print("1. LIHAT DATA SAYA")
        print("2. DAFTAR SEBAGAI MEMBER")
        print("3. KELUAR")
        print("="*60)
        pilih = input("PILIH MENU: ")
        
        if pilih == "1":
            print("\n" + "="*40)
            print("📋 DATA ANDA".center(40))
            print("="*40)
            print(f"ID USER: {current_user_id}")
            print(f"NAMA: {current_user['nama']}")
            print(f"USIA: {current_user['usia']}")
            print(f"ROLE: {current_user['role']}")
            
            if current_user_id in pilates_shain:
                print("\n--- DATA MEMBER ---")
                print(f"PAKET MEMBER: {pilates_shain[current_user_id]['paket']}")
                print(f"DURASI MEMBER: {pilates_shain[current_user_id]['durasi']} bulan")
            else:
                print("\nANDA BELUM TERDAFTAR SEBAGAI MEMBER")
                
        elif pilih == "2": 
            if current_user_id in pilates_shain:
                print("ANDA SUDAH TERDAFTAR SEBAGAI MEMBER!")
            else:
                print("\n" + "="*40)
                print("DAFTAR MEMBER BARU".center(40))
                print("="*40)
                paket = input("PAKET PILATES (BASIC / FOAM / LEGS / FULL / RINGAN): ")
                durasi = input("DURASI MEMBERSHIP (bulan): ")
                
                pilates_shain[current_user_id] = {
                    "nama": current_user['nama'],
                    "paket": paket,
                    "durasi": durasi
                }
                print("☆ PENDAFTARAN MEMBER BERHASIL! ☆")
                
        elif pilih == "3":
            print("\n𑣲 TERIMA KASIH TELAH MENGUNJUNGI MANAJEMEN DATA MEMBER PILATES")
            print("SEE YOUUU! ")
            member_berjalan = False
        else:
            print("PILIHAN TIDAK VALID")