#variabel angka untik menampung jumlah anka yang di inputkan berupa array/list angka = []

#variabel bilangan untuk menentukan jumlah bilangan yang diinginkan bilangan = input("Masukkan jumlah bilangan yang diinginkan")

#mengkonversi input bilangan string ke integer karena method input() selalu type data bilangan = int(bilangan)

print("Program mengurutkan data ")

#melalukan perulangan berdasarkan jumlah dari variabel bilangan

for i in range(0,10):
    #menampilakan variabel i , (" "* 3) Artinya menambahkan spasi kali lalu end => yaitu memulai baris baru setelah nilai terahir
    print(i, " " *3, end= '')

    for j in range(1,10):
        #menampilakan variabel i , (" "* 3) Artinya menambahkan spasi kali lalu end => yaitu memulai baris baru setelah nilai terahir
        print(j+i, " " *3, end= '')
    print()
