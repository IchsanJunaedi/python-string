#operator dalam bentuk method

## merubah case dari string

# merubah semua ke upper case

salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay = "aKu keCe AbiezXZZZzz"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

# contoh pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() #hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() #hasilnya bool
print(salam + " is lower = " + str(apakah_upper))

# isalpha() <--- untuk mengecek apakah semuanya huruf
# isalnum() <--- huruf dan angka / alpha dan numeric
# isdecimal() <--- angka saja
# isspace() <---- spasi,tab, newline \n
# istitle() <--- semua kata dimulai dengan huruf kapital

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() #hasilnya boolean

print(judul + " is title = " + str(cek_judul))

## ngecek komponen startswith() endswith() <-- keren jika mulai nya dari huruf besar dan di startswithnya huruf kecil maka false
cek_start = "Ichsan Stark".startswith("Ichsan")
print("start = " + str(cek_start))

cek_end = "Ichsan snow" .endswith("snow")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku', 'sayang', 'kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehem '.join(pisah)
print(gabungan)

gabungan = "akuehemsayangehemkamu"
print(gabungan.split('ehem'))

# alokasi karakter rjust(), ljust() center()

kanan = "kanan  ".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,"-")
print("'"+tengah+"'")

# kebalikannya --> strip()
tengah = tengah.strip("-")
print("'"+tengah+"'")
