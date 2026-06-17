
#Memasukkan nama

nama = input("Masukkan Nama Pendek Anda: ")
if nama == "habib":
    print("SELAMAT DATANG HABIB")
    print("BAIK HATI DAN TIDAK SOMBONG")
else:
    print("Program Selesai")

#Memasukkan umur

umur = int(input("Masukkan Umur Anda: "))
if  umur <= 0:
    print("anda belum lahir")
elif umur > 60:
    print("banyakin ibadah, bentar lagi ketemu yang maha kuasa")
elif umur >= 18:
    print("anda sudah cukup umur")
elif umur < 18:
    print("anda belum cukup umur")