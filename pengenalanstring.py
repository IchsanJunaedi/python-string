data = "ini adalah data"
print(data)
print(type(data))

# 1. cara membuat string

'''
        1. menggunakan tanda petik satu '...'
        2. menggunakan tanda petik dua "..."
'''
data = 'menggunukan tanda petik satu'
print(data)

data = "menggunukan tanda petik dua"
print(data)

print('"Halo, Apa kabar?"')
print("'Halo, Apa kabar?'")
print("ini adalah hari jum'at")

# menggunakan tanda \

# membuat tanda ' menjadi string
print('ini adalah hari jum\'at')
print('g\'day, isn\'t it?')

# backslash
print("C:\\user\\ican")

# tab
print("ican\tmenjauh, tolongin did")

# newline
print("baris pertama. \nbaris kedua.") #LF > Line feed biasa dipakai linux,macos
print("baris pertama, \rbaris kedua") #CR > Carriage Return > biasa dipakai computer jadul
print("baris pertama, \r\nbaris kedua") #CRLF > Carriage return line feed > biasa dipakai Windows

#3. string literal atau raw

# hati-hati
print('C:\new folder') #akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multineline literal string
print("""
Nama : ican
Kelas : TK A
""")

# multineline literal string dan RAW
print(r"""
nama : ican
ttl : New Orleans, 15 october 2006
website : www.ican.com\newID #harusnya kan \n tu kebaca command Line feed ya, karena memakai r diawal maka \n itu tidak ada outputnya
""")

