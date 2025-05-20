# Width and Multiline

# Data

data_nama = "Ican Stark"
data_umur = 17
data_tinggi = 165.1
data_nomor_Sepatu = 44

# string
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, nomor sepatu = {data_nomor_Sepatu} "
print(5*"="+"Data String"+5*"=")
print(data_string)

# String multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nnomor sepatu {data_nomor_Sepatu} "
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# String multiline (kutip triplets)
data_string = f""" 
nama    = {data_nama}
umur    = {data_umur}
tinggi  = {data_tinggi}
 sepatu = {data_nomor_Sepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# mengatur lebar
data_string = f""" 
nama   = {data_nama:>5}
umur   = {data_umur:>5}
tinggi = {data_tinggi:>5}
sepatu = {data_nomor_Sepatu:>5}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)
