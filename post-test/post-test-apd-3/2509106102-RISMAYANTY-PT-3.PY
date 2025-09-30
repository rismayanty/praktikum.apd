print ("MASUKKAN NAMA DAN NIM SESUAI DENGAN DATA DIRI ANDA")
print ("MASUKKAN NAMA ANDA (WAJIB CAPSLOCK)")

NAMA = input()
if NAMA == "RISMAYANTY":
    print ("MASUKKAN NIM ANDA")
    NIM = input()
    if NIM == "2509106102":
        print ("MASUKKAN JUMLAH UKT ANDA TERLEBIH DAHULU")
        UKT = int(input())
        print ("BERIKUT OPSI PEMBAYARAN UKT ANDA")
        print("1. LUNAS (1%)\n2. CICILAN 2x (5%)\n3. CICILAN 4x (8%)\n4. CICILAN 6x (12%)")

        

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

