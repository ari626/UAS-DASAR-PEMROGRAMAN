import math

nama = input("Masukkan nama : ")
print(f"\nHalo, {nama} 👋")

while True:
    print("\n=== Bangun Datar ===")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")

    pilih = input("Pilih bangun datar (1-4): ")

    if pilih == "1":
        sisi = int(input("Masukkan sisi : "))
        luas = sisi * sisi
        keliling = 4 * sisi
        print("Luas persegi :", luas)
        print("Keliling persegi :", keliling)

    elif pilih == "2":
        panjang = int(input("Masukkan panjang : "))
        lebar = int(input("Masukkan lebar : "))
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)
        print("Luas persegi panjang :", luas)
        print("Keliling persegi panjang :", keliling)

    elif pilih == "3":
        alas = int(input("Masukkan alas : "))
        tinggi = int(input("Masukkan tinggi : "))
        sisi_miring = int(input("Masukkan sisi miring : "))
        luas = 0.5 * alas * tinggi
        keliling = alas + tinggi + sisi_miring
        print("Luas segitiga :", luas)
        print("Keliling segitiga :", keliling)

    elif pilih == "4":
        r = int(input("Masukkan jari-jari : "))
        luas = math.pi * r * r
        keliling = 2 * math.pi * r
        print("Luas lingkaran :", round(luas, 2))
        print("Keliling lingkaran :", round(keliling, 2))

    else:
        print("Pilihan tidak tersedia ❌")

    ulang = input("\nIngin hitung lagi (y/n)? ")
    if ulang.lower() != 'y':
        break

print(f"\nTerima kasih, {nama} 😊")
