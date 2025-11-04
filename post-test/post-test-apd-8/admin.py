from prettytable import PrettyTable
from operasi import data_member, hitung_member, opsi_paket

def menu_admin(pilates_shain):
    print("\n🎀 MANAJEMEN DATA MEMBER PILATES 🎀".center(60))
    print("="*60)
    print("1. TAMBAH DATA\n2. TAMPILKAN DATA\n3. UBAH DATA\n4. HAPUS DATA\n5. LOGOUT")
    print("="*60)

    pilih = input("PILIH MENU: ")

    if pilih == "1":
        id_member = input("ID MEMBER: ")
        if id_member in pilates_shain:
            print("ID MEMBER SUDAH TERDAFTAR!")
        else:
            nama = input("NAMA: ")
            paket = input("PAKET PILATES (BASIC/FOAM/LEGS/FULL/RINGAN): ")
            durasi = input("DURASI MEMBERSHIP (bulan): ")
            if paket.upper() in opsi_paket and durasi.isdigit():
                pilates_shain[id_member] = {"nama": nama, "paket": paket, "durasi": durasi}
                print("๑ ⋆₊⋆─ʚ DATA BERHASIL DITAMBAHKAN ɞ─⋆₊⋆ ๑")
            else:
                print("DATA TIDAK VALID!")

    elif pilih == "2":
        if not pilates_shain:
            print("YAHHH (╥﹏╥)... BELUM ADA MEMBER")
        else:
            table = PrettyTable()
            table.field_names = ["ID", "Nama", "Paket", "Durasi", "Biaya (Rp)"]
            table.align = "l"
            table.hrules = True
            table.vrules = True
            
            from operasi import biaya_pilates
            for id_m, data in pilates_shain.items():
                biaya = biaya_pilates(data["paket"], data["durasi"])
                table.add_row([id_m, data["nama"], data["paket"], data["durasi"], biaya])
            
            print("\n" + "═" * 80)
            print("📊 DATA MEMBER PILATES".center(80))
            print("═" * 80)
            print(table)
            print("═" * 80)
            
            total_table = PrettyTable()
            total_table.field_names = ["TOTAL MEMBER"]
            total_table.add_row([hitung_member(pilates_shain)])
            total_table.align = "c"
            total_table.hrules = True
            total_table.vrules = True
            
            print("\n")
            print(total_table)
            print("\n")

    elif pilih == "3":
        data_lama = input("MASUKKAN ID MEMBER YANG INGIN DIUBAH: ")
        if data_lama in pilates_shain:
            nama_baru = input("NAMA BARU: ")
            paket_baru = input("PAKET BARU: ")
            durasi_baru = input("DURASI BARU (bulan): ")
            if durasi_baru.isdigit():
                pilates_shain[data_lama] = {"nama": nama_baru, "paket": paket_baru, "durasi": durasi_baru}
                print("ꔫ DATA BERHASIL DIUBAH ꔫ")
            else:
                print("DURASI WAJIB ANGKA!")
        else:
            print("⌗ DATA TIDAK DITEMUKAN")

    elif pilih == "4":
        data_hapus = input("MASUKKAN ID MEMBER YANG INGIN DIHAPUS: ")
        if data_hapus in pilates_shain:
            del pilates_shain[data_hapus]
            print("ꔫ DATA BERHASIL DIHAPUS ꔫ")
        else:
            print("(╥﹏╥) DATA TIDAK DITEMUKAN")

    elif pilih == "5":
        print("LOGOUT BERHASIL⭢ KEMBALI KE MENU UTAMA")
        return
    else:
        print("PILIHAN TIDAK VALID!")

    return menu_admin(pilates_shain)