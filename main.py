def hisoblagich(a, b , c):
    if a > b > c :
        print(a)
    elif a < b > c:
        print(b)
    else:
        print(c)
hisoblagich(3,2,1)

def hisoblagich(a, b , c):
           if c > a > b:
              print(c)
           elif c < a > b:
              print(a)
           elif c < b > a:
              print(b)
hisoblagich(int(input("Birinchi raqamni kiriting: ")),int(input("Ikkinchi raqamni kiriting: ")),int(input("Uchinchi raqamni kiriting: ")))
