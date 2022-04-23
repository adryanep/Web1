class PersegiPanjang():
    panjang = 0
    lebar = 0
    luas = 0
    keliling = 0
    def __init__(self, panjang,lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        self.luas = self.panjang * self.lebar
    
    def hitung_keliling(self):
        self.keliling = 2 * (self.panjang + self.lebar)
    
    def cetak(self):
        print("luas :", self.luas)
        print("keliling :", self.keliling)
        print("panjang :", self.panjang)
        print("lebar :", self.lebar)