nama = input("NAMA: ")
nim = input("NIM: ")
hargalaptop = int(input("HARGA LAPTOP: "))

laptopAcer = hargalaptop - (hargalaptop * 0.05)
laptopAsus = hargalaptop - (hargalaptop * 0.07)
laptopLenovo = hargalaptop - (hargalaptop * 0.1)

col1, col2, col3 = 15, 8, 20
total_width = col1 + col2 + col3 + 10  

print("=" * total_width)
print(" " * ((total_width - 30) // 2) + "BIAYA LAPTOP SETELAH DISKON")
print("=" * total_width)
print(f"{nama} dengan NIM {nim} ingin membeli laptop seharga {hargalaptop:}")
print("-" * total_width)


print(f"| {'Merk Laptop':^{col1}} | {'Diskon':^{col2}} | {'Harga Setelah Diskon':^{col3}} |")
print("-" * total_width)


print(f"| {'Laptop Acer':^{col1}} | {'5%':^{col2}} | {laptopAcer:^{col3}.0f} |")
print(f"| {'Laptop Asus':^{col1}} | {'7%':^{col2}} | {laptopAsus:^{col3}.0f} |")
print(f"| {'Laptop Lenovo':^{col1}} | {'10%':^{col2}} | {laptopLenovo:^{col3}.0f} |")

print("-" * total_width)
