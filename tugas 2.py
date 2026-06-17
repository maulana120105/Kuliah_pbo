# Nama yang benar (ganti sesuai nama pendek kamu)
nama_benar = "habib"

# Input nama
nama = input("Masukan nama anda: ")

# Validasi nama
if nama.lower() == nama_benar:
    print("Nama benar, lanjut ke program...\n")
    
    # Input angka
    angka = int(input("Masukkan angka (1-10): "))
    
    # Validasi angka
    if 1 <= angka <= 10:
        print(f"\nTabel perkalian {angka}:")
        for i in range(1, 11):
            print(f"{angka} x {i} = {angka * i}")
    else:
        print("Angka harus antara 1 sampai 10")
else:
    print("Silahkan coba lagi")
