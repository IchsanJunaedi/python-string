# Operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_awal = "ican"
nama_tengah = "D"
nama_akhir = "Constantine"

nama_lengkap = nama_awal + " " + nama_tengah + "'" +nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang dari string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. operator untuk string

# mengecek apakah ada komponen char atau string di string
# in dan not in logika operator

d = "d"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))


d = "D"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print(d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-[0:3]:" + nama_lengkap[0:4])
print("index ke-[3:7]:" + nama_lengkap[3:8])
print("index ke-[0,2,4,6,8,10]:" + nama_lengkap[0:10:2])

# item paling kecil
print("paling kecil:" + min(nama_lengkap))
# item paling besar
print("paling besar:" + max(nama_lengkap))

ascii_code = ord("!") # ord untuk mengambil unicode dari one char string
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 126
print("char untuk ASCII 117 adalah " + chr(data))

# 4. operator dalam bentuk method

data = "ican gaming buddy"
jumlah = data.count("a")
print("Jumlah a pada " + data + " = " + str(jumlah))