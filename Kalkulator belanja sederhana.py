# Kalkulator belanja sederhana

nama_barang_input = input('nama barang : ')

harga_satuan_input = input('harga satuan : ')
harga_satuan = float(harga_satuan_input)

jumlah_barang_input = input('jumlah barang : ')
jumlah_barang = int(jumlah_barang_input)

total_harga = harga_satuan * jumlah_barang
print('total_harga :', total_harga)

kurs = 18000
total_harga_usd = total_harga / kurs
print('total harga usd : ', total_harga_usd)

uang_dibayar_input = input('uang di bayar : ')
uang_dibayar = float(uang_dibayar_input)

kembalian = uang_dibayar - total_harga
print('kembalian :', kembalian )

print('nama barang : ', nama_barang_input)
print('harga satuan : ', harga_satuan)
print('jumlah_barang : ', jumlah_barang)
print('total harga : ', total_harga)
print('uang dibayar : ', uang_dibayar)
print('kembalian : ', kembalian)
print('total harga usd : ', total_harga_usd)


