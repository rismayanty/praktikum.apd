# manajemen data member pilates 
print("\n" + "="*60)
print("🎀 SELAMAT DATANG DI STUDIO PILATES SHAIN 🎀".center(60))
print("="*60)

# global
users = {}
pilates_shain = {}
studio_name = "PILATES SHAIN"
maks_percobaan = 3
opsi_paket = ["BASIC", "FOAM", "LEGS", "FULL", "RINGAN"]


def welcome():
    print("\n" + "="*60)
    print(f"🎀 SELAMAT DATANG DI STUDIO {studio_name} 🎀".center(60))
    print("="*60)

def menu_utama():
    print("\n")
    print("╭════•✧ MENU UTAMA STUDIO PILATES SHAIN ✧•════╮".center(60))
    print("\n")
    print("1. REGISTRASI")
    print("2. LOGIN")
    print("3. KELUAR")
    print("\n" + "="*60)
    return input("PILIH MENU: ")

def validasi_id(id_user):
    return len(id_user) == 4 and id_user.isdigit()

def biaya_pilates(paket, durasi):
    list_harga = {"BASIC": 50000, "FOAM": 75000, "LEGS": 60000, "FULL": 100000, "RINGAN": 40000}
    try:
        return list_harga.get(paket.upper(), 0) * int(durasi)
    except ValueError:
        return False

def data_member(member_id):
    if member_id in pilates_shain:
        data = pilates_shain[member_id]
        print(f"ID: {member_id}")
        print(f"NAMA: {data['nama']}")
        print(f"PAKET: {data['paket']}")
        print(f"DURASI: {data['durasi']} bulan")
        biaya = biaya_pilates(data['paket'], data['durasi'])
        print(f"BIAYA: Rp {biaya}")
    else:
        print("DATA TIDAK DITEMUKAN")

def hitung_member(data, index=0, keys=None):
    if keys is None:
        keys = list(data.keys())
    if index == len(keys):
        return 0
    return 1 + hitung_member(data, index + 1, keys)

# menu admin
def menu_admin():
    print("\n" + "="*60)
    print("🎀 MANAJEMEN DATA MEMBER PILATES 🎀".center(60)) 
    print("="*60)
    print("1. TAMBAH DATA")
    print("2. TAMPILKAN DATA")
    print("3. UBAH DATA")
    print("4. HAPUS DATA")
    print("5. LOGOUT")
    print("="*60)

    pilih = input("PILIH MENU: ")

    if pilih == "1":
        id_member = input("ID MEMBER: ")
        if id_member in pilates_shain:
            print("ID MEMBER SUDAH TERDAFTAR!")
        else:
            nama = input("NAMA: ")
            paket = input("PAKET PILATES (BASIC / FOAM / LEGS / FULL / RINGAN): ")
            durasi_input = input("DURASI MEMBERSHIP (bulan): ")
            try:
                durasi = int(durasi_input)
                if paket.upper() in opsi_paket:
                    pilates_shain[id_member] = {
                        "nama": nama,
                        "paket": paket,
                        "durasi": str(durasi)
                    }
                    print("๑ ⋆₊⋆─ʚ DATA BERHASIL DITAMBAHKAN ɞ─⋆₊⋆ ๑") 
                else:
                    print("PAKET TIDAK VALID!")
            except ValueError:
                print("DURASI WAJIB ANGKA YA!")
        return menu_admin()

    elif pilih == "2":
        if len(pilates_shain) == 0:
            print("YAHHH (╥﹏╥)... BELUM ADA MEMBER")
        else:
            print("\n=== DAFTAR MEMBER PILATES ===")
            counter = 1
            for id_member, data in pilates_shain.items():
                print(f"\nMEMBER KE-{counter}")
                data_member(id_member)
                counter += 1

            total_member = hitung_member(pilates_shain)
            print("\n✩ TOTAL SEMUA MEMBER:", total_member)
        return menu_admin()

    elif pilih == "3":
        data_lama = input("MASUKKAN ID MEMBER YANG INGIN DIUBAH: ")
        if data_lama in pilates_shain:
            print("\n=== UBAH DATA ===")
            print(f"data lama⭢ nama: {pilates_shain[data_lama]['nama']}, paket: {pilates_shain[data_lama]['paket']}, durasi: {pilates_shain[data_lama]['durasi']} bulan")

            ubah_id = input("UBAH ID MEMBER? (Y/T): ")
            if ubah_id == 'Y':
                id_baru = input("ID BARU: ")
                if id_baru in pilates_shain and id_baru != data_lama:
                    print("ID BARU SUDAH TERDAFTAR!")
                else:
                    pilates_shain[id_baru] = pilates_shain.pop(data_lama)
                    data_lama = id_baru

            nama_baru = input("NAMA BARU: ")
            paket_baru = input("PAKET BARU: ")
            durasi_baru_input = input("DURASI BARU (bulan): ")
            try:
                durasi_baru = int(durasi_baru_input)
                pilates_shain[data_lama]["nama"] = nama_baru
                pilates_shain[data_lama]["paket"] = paket_baru
                pilates_shain[data_lama]["durasi"] = str(durasi_baru)
                print("ꔫ DATA BERHASIL DIUBAH ꔫ")
            except ValueError:
                print("DURASI WAJIB BERUPA ANGKA!")
        else:
            print("⌗ DATA TIDAK DITEMUKAN")
        return menu_admin()

    elif pilih == "4":
        data_hapus = input("MASUKKAN ID MEMBER YANG INGIN DIHAPUS: ")
        if data_hapus in pilates_shain:
            del pilates_shain[data_hapus]
            print("ꔫ DATA BERHASIL DIHAPUS ꔫ")
        else:
            print("(╥﹏╥) DATA TIDAK DITEMUKAN")
        return menu_admin()

    elif pilih == "5":
        print("LOGOUT BERHASIL⭢ KEMBALI KE MENU UTAMA")
        return
    else:
        print("PILIHAN TIDAK VALID!")
        return menu_admin()

# menu member
def menu_member():
    print("\n")
    print("╭════•✧ MENU MEMBER PILATES SHAIN ✧•════╮".center(60))
    print("\n")
    print("1. LIHAT DATA SAYA")
    print("2. DAFTAR SEBAGAI MEMBER")
    print("3. LOGOUT")
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
            print("\n=== DATA MEMBER ===")
            data_member(current_user_id)
        else:
            print("\nANDA BELUM TERDAFTAR SEBAGAI MEMBER")
        return menu_member()

    elif pilih == "2":
        if current_user_id in pilates_shain:
            print("ANDA SUDAH TERDAFTAR SEBAGAI MEMBER!")
        else:
            print("\n" + "="*40)
            print("=== DAFTAR MEMBER BARU ===".center(40))
            print("="*40)
            paket = input("PAKET PILATES (BASIC / FOAM / LEGS / FULL / RINGAN): ")
            durasi_input = input("DURASI MEMBERSHIP (bulan): ")
            try:
                durasi = int(durasi_input)
                if paket.upper() in opsi_paket:
                    pilates_shain[current_user_id] = {
                        "nama": current_user['nama'],
                        "paket": paket,
                        "durasi": str(durasi)
                    }
                    print("☆ PENDAFTARAN MEMBER BERHASIL! ☆")
                else:
                    print("PAKET TIDAK VALID!")
            except ValueError:
                print("DURASI WAJIB BERUPA ANGKA!")
        return menu_member()

    elif pilih == "3":
        print("LOGOUT BERHASIL, KEMBALI KE MENU UTAMA")
        return
    else:
        print("PILIHAN TIDAK VALID!")
        return menu_member()

# menu utama
program_berjalan = True
while program_berjalan:
    pilih_menu = menu_utama()

    if pilih_menu == "1":
        print("\n=== ✮ REGISTRASI AKUN ✮ ===")
        id_user = input("MASUKKAN ID (4 angka saja): ")
        nama = input("MASUKKAN NAMA: ")
        usia_input = input("MASUKKAN USIA: ")
        role = input("MASUKKAN ROLE (admin/member): ")

        try:
            usia = int(usia_input)
        except ValueError:
            print("USIA WAJIB ANGKA YA!")
            continue

        if role in ["admin", "member"]:
            if validasi_id(id_user):
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
            else:
                print("ID WAJIB 4 ANGKA!")
        else:
            print("ROLE TIDAK VALID! PILIHAN HANYA (admin/member)")

    elif pilih_menu == "2":
        # login moment
        login_gagal = 0
        login_berhasil = False
        global current_user, current_user_id

        while login_gagal < maks_percobaan and not login_berhasil:
            print("\n" + "="*60)
            print("𝜗ৎ LOGIN USER 𝜗ৎ".center(60))
            print("="*60)
            id_in = input("MASUKKAN ID (4 angka saja): ")
            nama_in = input("MASUKKAN NAMA: ")

            if id_in in users:
                user_data = users[id_in]
                if nama_in == user_data["nama"]:
                    login_berhasil = True
                    current_user = user_data
                    current_user_id = id_in
                    print("☆ LOGIN BERHASIL! ☆")
                    break
            if not login_berhasil:
                login_gagal += 1
                print("LOGIN GAGAL! SILAHKAN COBA LAGI")
                print(f"percobaan tersisa: {maks_percobaan - login_gagal}")

        if not login_berhasil:
            print("GAGAL LOGIN 3 KALI, KEMBALI KE MENU UTAMA")
            continue

        if current_user["role"] == "admin":
            menu_admin()
        elif current_user["role"] == "member":
            menu_member()

    elif pilih_menu == "3":
        print("\n𑣲 TERIMA KASIH SUDAH MENGUNJUNGI STUDIO PILATES SHAIN")
        print("SEE YOUUU!!")
        program_berjalan = False

    else:
        print("PILIHAN TIDAK VALID!")