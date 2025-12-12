# 3
class ElektroAvto(Avtomobil):
    def __init__(self, brend, model, yil, batareya):
        super().__init__(brend, model, yil)
        self.batareya = batareya

    def zaryad(self):
        return f"{self.brend} {self.model} zaryad qilinmoqda..."

elektro1 = ElektroAvto("Tesla", "Model S", 2022, 75)
print(elektro1.holat())

print(elektro1.zaryad())



# 4
class Hayvon:
    def ovoz(self):
        pass

class Kuchuk(Hayvon):
    def ovoz(self):
        return "Vov-vov"

class Mushuk(Hayvon):
    def ovoz(self):
        return "Miyov"

hayvonlar = [Kuchuk(), Mushuk()]
for hayvon in hayvonlar:
    print(hayvon.ovoz())
