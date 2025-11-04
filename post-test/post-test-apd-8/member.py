from operasi import data_member, opsi_paket
import os

def menu_member(pilates_shain, current_user, current_user_id):
    print("\n╭════•✧ MENU MEMBER ✧•════╮")
    print("1. LIHAT DATA SAYA")
    print("2. DAFTAR SEBAGAI MEMBER")
    print("3. LOGOUT")
    print("="*60)

    pilih = input("PILIH MENU: ")

    if pilih == "1":
        print(f"\nID USER: {current_user_id}")
        print(f"NAMA: {current_user['nama']}")
        print(f"USIA: {current_user['usia']}")
        if current_user_id in pilates_shain:
            data_member(pilates_shain, current_user_id)
        else:
            print("ANDA BELUM TERDAFTAR SEBAGAI MEMBER.")
    elif pilih == "2":
        if current_user_id in pilates_shain:
            print("ANDA SUDAH TERDAFTAR!")
            input("tekan ENTER untuk next...")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            paket = input("PAKET PILATES (BASIC/FOAM/LEGS/FULL/RINGAN): ")
            durasi = input("DURASI MEMBERSHIP (bulan): ")
            if paket.upper() in opsi_paket and durasi.isdigit():
                pilates_shain[current_user_id] = {
                    "nama": current_user["nama"],
                    "paket": paket,
                    "durasi": durasi
                }
                print("☆ PENDAFTARAN MEMBER BERHASIL! ☆")
            else:
                print("DATA TIDAK VALID!")
    elif pilih == "3":
        print("☆ LOGOUT BERHASIL! ☆")
        return
    else:
        print("PILIHAN TIDAK VALID!")

    return menu_member(pilates_shain, current_user, current_user_id)