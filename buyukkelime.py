#büyük harfteki kelimeyi küçük harfe çevirir
import os
os.system("clear")
import author
author
print("")
kharf = ("qazwsxedcrfvtgbyhnujmıköolçpşğiü")
bharf = ("QAZWSXEDCRFVTGBYHNUJMIKÖOLÇPŞĞİÜ")
secim = input("'|ENTER|' tuşuna basınız:")
while True:
    if secim == "":
        cevir=str.maketrans(bharf,kharf)
        veri=input("Kelimeyi giriniz:")
        v_uz=len(veri)
    if veri == "":
        break
    else:
        print("metin çevrildi","Metniniz:","","'",veri.translate(cevir),"'","","Metin uzunluğu:","",v_uz)
    print("")
