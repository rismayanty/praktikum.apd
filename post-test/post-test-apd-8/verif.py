import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def validasi_id(id_user):
    return len(id_user) == 4 and id_user.isdigit()

def registrasi(users):
    clear()
    print("\n=== ✮ REGISTRASI AKUN ✮ ===")
    id_user = input("MASUKKAN ID (4 angka): ")
    nama = input("MASUKKAN NAMA: ")
    usia = input("MASUKKAN USIA: ")
    role = input("MASUKKAN ROLE (admin/member): ")

    if not usia.isdigit():
        print("USIA HARUS ANGKA.")
        input("tekan ENTER untuk next...")
        clear()
        return

    if role not in ["admin", "member"]:
        print("ROLE TIDAK VALID.")
        input("tekan ENTER untuk next...")
        clear()
        return

    if not validasi_id(id_user):
        print("ID WAJIB 4 ANGKA.")
        input("tekan ENTER untuk next...")
        clear()
        return

    if id_user in users:
        print("ID SUDAH TERDAFTAR.")
        input("tekan ENTER untuk next...")
        clear()
        return

    users[id_user] = {
        "nama": nama,
        "usia": int(usia),
        "role": role
    }
    print("☆ REGISTRASI BERHASIL! ☆")

def login(users, maks_percobaan):
    clear()
    for i in range(maks_percobaan):
        print("\n𝜗ৎ LOGIN USER 𝜗ৎ")
        id_in = input("MASUKKAN ID: ")
        nama_in = input("MASUKKAN NAMA: ")
        if id_in in users and nama_in == users[id_in]["nama"]:
            print("☆ LOGIN BERHASIL! ☆")
            input("tekan ENTER untuk next...")
            clear()
            return id_in, users[id_in]
        else:
            print(f"LOGIN GAGAL ({i+1}/{maks_percobaan})")
            if i < maks_percobaan - 1:
                input("tekan ENTER untuk next...")
                clear()
    input("tekan ENTER untuk next...")
    clear()
    return None