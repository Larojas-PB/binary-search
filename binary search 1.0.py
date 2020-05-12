print("pisahkan angka dengan koma")
p = input("Masukkan list angka : ")
o = int(input("Masukkan angka yg dicari: "))

def search(p,l,u,o) :

    if l <= u:
        mid = l + (u-l)
        if int(p[mid]) == o:
            return mid
        elif int(p[mid]) > o:
          return search(p, l, mid-1, o)
        else:
          return search(p, mid+1, u, o)
    else:
      return -1
  

p = p.split(',')
hasil = search(p,0, len(p)-1, o)
if hasil != -1:
    print("ditemukan di index ke " + str(hasil))
else :
    print ("tidak ada")                
