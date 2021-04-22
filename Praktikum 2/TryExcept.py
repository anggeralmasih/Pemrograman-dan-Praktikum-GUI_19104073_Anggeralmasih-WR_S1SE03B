# Try..except
try :
  a = int(input('Masukkan nilai a: '))
  b = int(input('Masukkan nilai b: '))
  c = a/b
  print(f"{a} / {b} = {c}")

except ZeroDivisionError as e :
  print('Error : Tidak boleh dibagi 0')

# Try..except..finally
f = ''

try : 
  f = open('contoh.txt', 'r')
  lines = f.readlines()
  for line in lines :
    print(line, end = '\n')
  
except IOError as e :
  print('Error : File hilang')

finally : 
  if f :
    f.close()