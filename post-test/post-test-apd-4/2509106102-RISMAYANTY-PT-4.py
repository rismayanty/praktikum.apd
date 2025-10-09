NAMA_LENGKAP = "RISMAYANTY"
NIM = "2509106102"

LIMIT_PERCOBAAN = 3
PERCOBAAN = 0

print("=== VALIDASI LOGIN ===")

while PERCOBAAN < LIMIT_PERCOBAAN:

    USERNAME = input("USERNAME: ")
    PASSWORD = input("PASSWORD: ")
    
    if USERNAME == NAMA_LENGKAP and PASSWORD == NIM:
        print("LOGIN BERHASIL! ✩ SELAMAT BERBELANJA ୨୧")
        
        # menu furniture
        print("\n" + "="*50)
        print("🎀 MENU FURNITUR 🎀".center(50))
        print("="*50)
        print("1. SOFA -> Rp500.000 /unit".center(50))
        print("2. MEJA BELAJAR -> Rp250.000 /unit".center(50))
        print("3. RAK LEMARI -> Rp150.000 /unit".center(50))
        print("4. KELUAR DARI PROGRAM ෆ‿︵".center(50))
        print("="*50)
        
        while True:
            OPSI = input("\nPILIH OPSI (1-4): ")
            
            if OPSI == "1":
                print("\nANDA MEMILIH: SOFA")
                print("HARGA: Rp500.000 /unit")
                
                JUMLAH = input("MASUKKAN JUMLAH UNIT: ")
                
                input_isinya_angka_semua = True
                if JUMLAH == "": 
                    input_isinya_angka_semua = False
                else:
                    for setiap_karakter in JUMLAH:
                        if setiap_karakter not in "0123456789":
                            input_isinya_angka_semua = False
                            break
                
                if input_isinya_angka_semua:
                    JUMLAH = int(JUMLAH)
                    TOTAL = 500000 * JUMLAH
                    print(f"TOTAL HARGA: Rp{TOTAL:.0f}")

                    # ini tampilan diskon
                    if TOTAL >= 700000:
                        DISKON = TOTAL * 0.20
                        TOTAL_AKHIR = TOTAL - DISKON
                        print(f"TOTAL AKHIR: Rp{TOTAL_AKHIR:.0f}")
                        print("YEAYY DAPET DISKON 20% !!")
                        
                    elif TOTAL >= 500000 and TOTAL < 700000:
                        DISKON = TOTAL * 0.08
                        TOTAL_AKHIR = TOTAL - DISKON
                        print(f"TOTAL AKHIR: Rp{TOTAL_AKHIR:.0f}")
                        print("YEAYY DAPET DISKON 8% !!")
                        
                    elif TOTAL >= 150000 and TOTAL < 500000:
                        TOTAL_AKHIR = TOTAL
                        print(f"TOTAL AKHIR: Rp{TOTAL_AKHIR:.0f}")
                        print("YEAYY DAPET KITCHEN SET !")
                        
                    else:
                        TOTAL_AKHIR = TOTAL
                        print(f"SUBTOTAL: Rp{TOTAL:.0f}")
                        print(f"TOTAL AKHIR: Rp{TOTAL_AKHIR:.0f}")
                        print("TERIMA KASIH UDAH BELANJA !!")
                    
                    
                else:
                    print("JUMLAH WAJIB PAKAI ANGKA YEAH !")

            elif OPSI == "2":
                print("\nANDA MEMILIH: MEJA BELAJAR")
                print("HARGA: Rp250.000 /unit")
                
                JUMLAH = input("MASUKKAN JUMLAH UNIT: ")
                
                # ngecek input, buat mastiin "angka semua atau ada huruf"
                input_isinya_angka_semua = True
                if JUMLAH == "":
                    input_isinya_angka_semua = False
                else:
                    for setiap_karakter in JUMLAH:
                        if setiap_karakter not in "0123456789":
                            input_isinya_angka_semua = False
                            break
                
                if input_isinya_angka_semua:
                    JUMLAH = int(JUMLAH)
                    TOTAL = 250000 * JUMLAH
                    print(f"TOTAL HARGA: Rp{TOTAL:.0f}")

                    # ini tampilan diskon
                    if TOTAL >= 700000:
                        DISKON = TOTAL * 0.20
                        TOTAL_AKHIR = TOTAL - DISKON
                        print(f"TOTAL AKHIR: Rp{TOTAL_AKHIR:.0f}")
                        print("YEAYY DAPET DISKON 20% !!")
                        
                    elif TOTAL >= 500000 and TOTAL < 700000:
                        DISKON = TOTAL * 0.08
                        TOTAL_AKHIR = TOTAL - DISKON
                        print(f"TOTAL AKHIR: Rp{TOTAL_AKHIR:.0f}")
                        print("YEAYY DAPET DISKON 8% !!")
                        
                    elif TOTAL >= 150000 and TOTAL < 500000:
                        TOTAL_AKHIR = TOTAL
                        print(f"TOTAL AKHIR: Rp{TOTAL_AKHIR:.0f}")
                        print("YEAYY DAPET KITCHEN SET !")
                        
                    else:
                        TOTAL_AKHIR = TOTAL
                        print(f"SUBTOTAL: Rp{TOTAL:.0f}")
                        print(f"TOTAL AKHIR: Rp{TOTAL_AKHIR:.0f}")
                        print("TERIMA KASIH UDAH BELANJA !")
                else:
                    print("JUMLAH WAJIB PAKAI ANGKA YEAH !")
                    
            elif OPSI == "3":
                print("\nANDA MEMILIH: RAK LEMARI")
                print("HARGA: Rp150.000 /unit")
                
                # ini tampilan diskon
                JUMLAH = input("MASUKKAN JUMLAH UNIT YANG DIINGINKAN: ")
                input_isinya_angka_semua = True
                if JUMLAH == "": 
                    input_isinya_angka_semua = False
                else:
                    for setiap_karakter in JUMLAH:44
                        if setiap_karakter not in "0123456789":
                            input_isinya_angka_semua = False
                            break
                
                if input_isinya_angka_semua:
                    JUMLAH = int(JUMLAH)
                    TOTAL = 150000 * JUMLAH
                    print(f"TOTAL HARGA: Rp{TOTAL:.0f}")
                    if TOTAL >= 700000:
                        DISKON = TOTAL * 0.20
                        TOTAL_AKHIR = TOTAL - DISKON
                        print(f"TOTAL AKHIR: Rp{TOTAL_AKHIR:.0f}")
                        print("YEAYY DAPET DISKON 20% !!")
                        
                    elif TOTAL >= 500000 and TOTAL < 700000:
                        DISKON = TOTAL * 0.08
                        TOTAL_AKHIR = TOTAL - DISKON
                        print(f"TOTAL AKHIR: Rp{TOTAL_AKHIR:.0f}")
                        print("YEAYY DAPET DISKON 8% !!")
                        
                    elif TOTAL >= 150000 and TOTAL < 500000:
                        TOTAL_AKHIR = TOTAL
                        print(f"TOTAL AKHIR: Rp{TOTAL_AKHIR:.0f}")
                        print("YEAYY DAPET KITCHEN SET !")
                        
                    else:
                        TOTAL_AKHIR = TOTAL
                        print(f"SUBTOTAL: Rp{TOTAL:.0f}")
                        print(f"TOTAL AKHIR: Rp{TOTAL_AKHIR:.0f}")
                        print("TERIMA KASIH UDAH BELANJA !")
                else:
                    print("JUMLAH WAJIB PAKAI ANGKA YEAH !")

            elif OPSI == "4":
                print("\nTERIMA KASIH SUDAH BERKUNJUNG  DI TOKO FURNITUR INFORDEH! SAMPAI JUMPA ୨୧")
                break
                
            else:
                print("GA VALID HUHU, PAKE ANGKA YA! YUK PILIH ULANG (1-4)")
            
            # ini buat opsi keluar
            LANJUT = input("\nMASIH MAU BELANJA? (YA/TIDAK): ")
            if LANJUT == "TIDAK":   
                print("\nTERIMA KASIH SUDAH BERBELANJA DI TOKO FURNITUR INFORDEH !! SAMPAI JUMPA ୨୧")
                break 

        # bakal stop, karena user udah selesai belanja
        break
        
    else:
        PERCOBAAN += 1
        SISA_PERCOBAAN = LIMIT_PERCOBAAN - PERCOBAAN
        print("YAHH ૮◞ ﻌ ◟ა LOGIN GAGAL! USERNAME ATAU PASSWORD SALAH")
        print("SISA PERCOBAAN:", SISA_PERCOBAAN)
        
        # ini kesempatan, kalau emang belum nyampe limit user masih bisa login
        if PERCOBAAN < LIMIT_PERCOBAAN:
            print("COBA LAGI YEAHH ʕ•ᴥ•ʔ\n")

# ini kalau emang udah nyampe limit, dia bakal ngasih tau kalau user udah gabisa login
if PERCOBAAN == LIMIT_PERCOBAAN:
    print("UDAH KENA LIMIT NIEHH, MAAF AKSES DITOLAK !")