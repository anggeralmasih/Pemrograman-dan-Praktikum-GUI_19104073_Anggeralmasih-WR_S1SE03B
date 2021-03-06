from abc import ABCMeta, abstractmethod

# kelas abstract  
class DuaDimensi(metaclass = ABCMeta) :
  @abstractmethod
  def luas(self) :
    pass

# Kelas segiEmpat turunan dari kelas DuaDimensi  
class SegiEmpat(DuaDimensi) :
  def __init__(self, p, l) :
    self.panjang = p
    self.lebar = l

# implementasi metode luas()  
  def luas(self) :
    return self.panjang * self.lebar

# Kelas Segitiga turunan dari kelas DuaDimensi  
class Segitiga(DuaDimensi) :
  def __init__(self, a, t) :
    self.alas = a
    self.tinggi = t

# implementasi metode luas()  
  def luas(self) :
    return (self.alas * self.tinggi) / 2

# Kelas Lingkaran turunan dari kelas DuaDimensi
class Lingkaran(DuaDimensi) :
  def __init__(self, r) :
    self.jari2 = r

# implementasi metode luas()  
  def luas(self) :
    import math
    return math.pi * (self.jari2 ** 2)

segitiga = Segitiga(2, 4)
print(segitiga.luas())
segiEmpat = SegiEmpat(2, 4)
print(segiEmpat.luas())
lingakaran = Lingkaran(10)
print(lingakaran.luas())

