class Aritmatika :

  @staticmethod
  def tambah(a, b) :
    return a + b

  @staticmethod
  def kurang(a, b) :
    return a - b
  
  @staticmethod
  def bagi(a, b) :
    return a / b

  @staticmethod
  def bagi_int(a, b) :
    return a // b

  @staticmethod
  def pangkat(a, b) :
    return a ** b

# Langsung call class dan method
print(Aritmatika.tambah(5, 5))

# Bikin objek dulu
objekA = Aritmatika()
print(objekA.pangkat(2, 3))
