class persegiPanjang :
  # Variable biasa
  counter = 0

  # Constructor
  def __init__(self, p, l) :
    self.panjang = p
    self.lebar = l
  
# Encapsulation
  # Setter
  def ubahPanjang (self, p) :
    self.panjang = p

  def ubahLebar (self, l) :
    self.lebar = l
#-- End Encapsulation

  def hitungLuas (self) :
    return self.panjang * self.lebar

  def hitungKeliling (self) :
    return 2 * (self.panjang + self.lebar) 
  
  def cetakLuas(self) :
    print(f'Luas Persegi Panjang\t:  {self.hitungLuas()}')

  def cetakKeliling(self) :
    print(f'Keliling Persegi Panjang\t: {self.hitungKeliling()}')

#import persegiPanjang;
objekPP1 = persegiPanjang(10, 8)

objekPP2 = persegiPanjang(9, 8)

objekPP3 = persegiPanjang(8, 8)

objekPP1.cetakLuas()

objekPP1.cetakKeliling()

objekPP1.counter = 10

#objekPP = persegiPanjang(10, 8)

#objekPP.cetakLuas()

#objekPP.cetakKeliling
     