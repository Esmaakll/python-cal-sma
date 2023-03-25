import random as r
import time as t

class taskagıtmakas():

    def __init__(self):
        self.secim()

    def secim(self):
        baslik="tas kagıt makas oyunu oynama"
        print("*" * len(baslik),baslik,"*" * len(baslik),sep="\n",end="\n")

        while True:
           tercih = input("oyunun açıklması için 1'e, başlamak için 2'ye basınız...")

           if tercih=="1":
            self.oyunacıklaması()
           elif tercih =="2":
             self.oyunabasla()
             break
           else:
             print("geçersiz bir karakter girildi... işlem iptal edildi ")
             break

    def oyunacıklaması(self):
          
          print("""Oyunun Açıklaması = >
    Klasik taş kağıt makas oyunu. 
    Kullanıcının seçim yaptığı andaki bilgisayarın kullandığıyla kullanıcının seçtiği karşılaştırılıyor. 
    Oyun, kullanıcı seçim ekranında 1 veya TAŞ, 2 VEYA KAĞIT, ya da 3 VEYA MAKAS dışında 
    bir veri girene kadar devam ediyor.
    """)

    def oyunabasla(self): 

        durumlar=["TAŞ","KAĞIT","MAKAS","1","2","3"]  

        while True:
            kullanıcı = input("1){}\n2){}\n3){}\nSeçiniz =>".format(*durumlar)).upper()
            bilgisayar=r.randrange(0,3)
            sayı=-1

            if kullanıcı in durumlar:
               if kullanıcı == "1" or  kullanıcı=="TAŞ":
                 sayı=0
               elif kullanıcı == "2" or kullanıcı=="KAĞIT":
                 sayı=1
               elif kullanıcı == "3" or kullanıcı=="MAKAS":
                 sayı=2
               if sayı == bilgisayar:
                 print("berabere , sen {} yaptın = ben {} yaptım ".format(durumlar[sayı],durumlar[bilgisayar]))
               elif sayı == 0 and bilgisayar == 2:
                 print("sen kazandın , sen {} yaptın = ben {} yaptım ".format(durumlar[sayı],durumlar[bilgisayar]))
               elif sayı == 0 and bilgisayar == 1:
                 print("ben kazandım , sen {} yaptın = ben {} yaptım".format(durumlar[sayı],durumlar[bilgisayar]))
               elif sayı == 1 and bilgisayar == 2:
                 print("ben kazandım , sen {} yaptın = ben {} yaptım".format(durumlar[sayı],durumlar[bilgisayar]))
               elif sayı == 1 and bilgisayar == 2:
                    print("Ben kazandım, sen {} yaptın = ben {} yaptım".format(durumlar[sayı], durumlar[bilgisayar]))

               elif sayı == 1 and bilgisayar == 0:
                    print("Sen kazandın, sen {} yaptın = ben {} yaptım".format(durumlar[sayı],durumlar[bilgisayar]))

               elif sayı == 2 and bilgisayar == 1:
                    print("Sen kazandın, sen {} yaptın = ben {} yaptım".format(durumlar[sayı], durumlar[bilgisayar]))

               elif sayı == 2 and bilgisayar == 0:
                    print("Ben kazandım, sen {} yaptın = ben {} yaptım".format(durumlar[sayı], durumlar[bilgisayar]))
               print()
            else:
             print("Oyun Bitiriliyor :(")
             break       
if __name__ == "__main__":
     taskagıtmakas()
     t.sleep(1)
           