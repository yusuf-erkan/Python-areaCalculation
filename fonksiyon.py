def dortgen_alan_hesapla_v1(a,b):
    print("-"*20)
    c=int(a)*int(b)
    print("Dikdörtgenin alanı: ",c)
    print("-"*20)

a=input("dikdörtgenin ilk kenarını girin: ")
b=input("dikdörtgenin ikinci kenarını girin: ")
dortgen_alan_hesapla_v1(a,b)


def daire_alan_hesapla_v1(r):
    print("-"*20)
    c=3.14*int(r)*int(r)
    print("Dairenin Alanı: ",c)
    print("-"*20)

r=input("Dairenin yarıçapını girin: ")
daire_alan_hesapla_v1(r)


def dortgen_alanı_hesapla_v2(a):
    print("-"*20)
    c=int(a)**2
    print("Dörtgenin alanı: ",c)
    print("-"*20)

d=input("Dörtgenin kenarını girin: ")
dortgen_alanı_hesapla_v2(d)

def daire_alanı_hesapla_v2(r):
    print("-"*20)
    c=3.14*(int(r)**2)
    print("Dairenin Alanı: ",c)
    print("-"*20)

R=input("Dairenin yarıçapını girin: ")
daire_alanı_hesapla_v2(R)
