class _laundry():
    def __init__(self, nama_pelanggan, alamat_pelanggan, tujuan_pelanggan,):
        self.nama_pelanggan = nama_pelanggan
        self.alamat_pelanggan = alamat_pelanggan
        self.tujuan_pelanggan = tujuan_pelanggan
        
    def _set (self, nama_pelanggan, alamat_pelanggan, tujuan_pelanggan,):
        self.nama_pelanggan = nama_pelanggan
        self.alamat_pelanggan = alamat_pelanggan
        self.tujuan_pelanggan = tujuan_pelanggan

    def ok (self):
        print('nama pelanggan       :' + self.nama_pelanggan)
        print('alamat pelanggan     :' + self.alamat_pelanggan)
        print('tujuan pelanggan     :' + self.tujuan_pelanggan)

print('=====================================')
print('     PROGRAM JASA LAUNDRY   ')
print('=====================================')

nama_pelanggan      = input('nama_pelanggan        :')
alamat_pelanggan    = input('alamat_pelanggan      :')
tujuan_pelanggan    = input('tujuan_pelanggan       :')


print('======================================')

proses = _laundry(nama_pelanggan, alamat_pelanggan, tujuan_pelanggan)
print (proses.ok())