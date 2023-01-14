class Shaxs:
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_fullname(self):
        """shaxsni to'liq ism familiyasi"""
        return f"{self.ism} {self.familiya}"

    def get_info(self):
        """shaxs haqida malumot"""
        return f"{self.ism} {self.familiya} Passport {self.passport} tug'ilgon yil {self.tyil}"

    def get_age(self, yil):
        """shaxsning yosh"""
        return yil-self.tyil


class Talaba(Shaxs):
    """Talaba klassi"""

    def __init__(self, ism, familiya, passport, tyil, id, manzil):
        """Talabaning xususiyati"""
        super().__init__(ism, familiya, passport, tyil)
        self.id = id
        self.bosqich = 1
        self.manzil = manzil

    def get__id(self):
        """Talabaning id raqami"""
        return self.id

    def get_bosqich(self):
        """tabalabning bosqichini olish"""
        return self.bosqich

    def update_boshqich(self):
        """Bosqichni oshirish"""
        self.bosqich += 1

    def get_info(self):
        """shaxs haqida malumot"""
        return f"{self.ism} {self.familiya} Passport {self.passport} tug'ilgon yil {self.tyil} id {self.id} bosqich {self.bosqich} manzil {Manzil.get_manzil}"


class Manzil:
    """Manzil saqlash uchun klass"""

    def __init__(self, uy, kocha, tuman, viloyat):
        """Manzil xususiyat"""
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat

    def get_manzil(self):
        """Manzilni ko'rish"""
        return f"{self.viloyat} viloyat {self.tuman} tuman {self.kocha} ko'cha {self.uy} uy"


inson = Shaxs("Hasan", "Alimov", "FB001122", 1995)
talaba_manzil = Manzil(12, 'Olmazor', "Bog'bon", "Samarqand")
print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda. Manzil {talaba_manzil.get_manzil()}")
