#küçük harfteki kelimeyi büyük harfe çevirir
import author
author
kharf ="qazwsxedcrfvtgbyhnujmıköolçpşğiü"
bharf = "QAZWSXEDCRFVTGBYHNUJMIKÖOLÇPŞĞİÜ"
secim = input("'ENTER' tuşuna basınız:")
while True:
        if secim == "":
                cevir = str.maketrans(kharf,bharf)
        veri = input("Kelimeyi giriniz:")
        v_uz=len(veri)
        if veri == "":
            break
        else:
            print("metin çevrildi","Metniniz:","","'",veri.translate(cevir),"'","","Metin uzunluğu:","",v_uz)
