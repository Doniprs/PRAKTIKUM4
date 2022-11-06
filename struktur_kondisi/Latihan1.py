# menerima input yang diketik dan menyimpan didalam variabel
bilanganSatu = input("Masukkan bilangan Pertama : ")
bilanganKedua = input("Masukkan bilangan Kedua : ")

# mengkonversibinput string ke integer karena method input () selalu mengembalikan type data str
bilanganSatu = int(bilanganSatu)
bilanganKedua = int(bilanganKedua)

#Mengecek untuk menentukan bilangan terbesar dari kedua bilangan
if bilanganSatu > bilanganKedua:
    print("Bilangan ", bilanganSatu,"lebih besar dari bilangan", bilanganKedua)
else: print("Bilangan", bilanganKedua,"lebih besar dari bilangan",bilanganSatu)

