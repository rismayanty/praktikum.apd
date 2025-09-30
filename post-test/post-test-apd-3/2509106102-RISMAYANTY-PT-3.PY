print ("MASUKKAN NAMA DAN NIM SESUAI DENGAN DATA DIRI ANDA")
print ("MASUKKAN NAMA ANDA (WAJIB CAPSLOCK)")

UKT = 6000000
NAMA = input()
if NAMA == "RISMAYANTY":
    print ("MASUKKAN NIM ANDA")
    NIM = input()
    if NIM == "2509106102":
        print ("BERIKUT OPSI PEMBAYARAN UKT ANDA")
        print ("1. LUNAS (Sekali Bayar): BADMINISTRASI (1%)")
        print ("2. CICILAN 2x per Semester: ADMINISTRASI (5%)")
        print ("3. CICILAN 4x per Semester: ADMINISTRASI (8%)")
        print ("4. CICILAN 6x per Semester: ADMINISTRASI (12%)")


        OPSI = int(input())
        if OPSI == 1:
            ADMIN = 0.01
            TOTAL = UKT + UKT*ADMIN
            print (f"TOTAL:{TOTAL:.0f}")

        elif OPSI == 2:
            ADMIN = 0.05
            TOTAL = UKT + UKT*ADMIN
            CICILAN = TOTAL /2
            print (f"CICILAN:{CICILAN:.0f}")

        elif OPSI == 3:
            ADMIN = 0.08
            TOTAL = UKT + UKT*ADMIN
            CICILAN = TOTAL /4
            print (f"CICILAN:{CICILAN:.0f}")

        elif OPSI == 4:
             ADMIN = 0.12
             TOTAL = UKT + UKT*ADMIN
             CICILAN = TOTAL /6
             print (f"CICILAN:{CICILAN:.0f}")
             print ("SILAHKAN MEMBAYAR UKT ANDA, TERIMA KASIH...")

        else:
          print ("GAGAL LOGIN")

else:
    print ("GAGAL LOGIN")

