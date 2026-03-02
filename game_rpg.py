from abc import ABC, abstractmethod

# PRAKTIKUM 1 - CLASS DAN OBJECT
print("=== PRAKTIKUM 1 ===")

class HeroP1:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def info(self):
        print(f"Hero: {self.name} | HP: {self.hp} | Power: {self.attack_power}")

hero1 = HeroP1("Layla", 100, 15)
hero2 = HeroP1("Zilong", 120, 20)

hero1.info()
hero2.info()

# PRAKTIKUM 2 - INTERAKSI ANTAR OBJECT
print("\n=== PRAKTIKUM 2 ===")

class HeroP2:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def serang(self, lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(self.attack_power)

    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} HP tersisa {self.hp}")

h1 = HeroP2("Layla", 100, 15)
h2 = HeroP2("Zilong", 120, 20)

h1.serang(h2)
h2.serang(h1)

# PRAKTIKUM 3 - INHERITANCE
print("\n=== PRAKTIKUM 3 ===")

class HeroP3:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def diserang(self, damage):
        self.hp -= damage
        print(f"{self.name} HP {self.hp}")

class MageP3(HeroP3):
    def __init__(self, name, hp, attack_power, mana):
        super().__init__(name, hp, attack_power)
        self.mana = mana

    def skill_fireball(self, lawan):
        if self.mana >= 20:
            self.mana -= 20
            lawan.diserang(self.attack_power * 2)

eudora = MageP3("Eudora", 80, 30, 100)
balmond = HeroP3("Balmond", 200, 10)

eudora.skill_fireball(balmond)

# PRAKTIKUM 4 - ENCAPSULATION
print("\n=== PRAKTIKUM 4 ===")

class HeroP4:
    def __init__(self, nama, hp_awal):
        self.nama = nama
        self.__hp = hp_awal

    def get_hp(self):
        return self.__hp

    def set_hp(self, nilai):
        if nilai < 0:
            self.__hp = 0
        elif nilai > 1000:
            self.__hp = 1000
        else:
            self.__hp = nilai

hero = HeroP4("Layla", 100)

hero.set_hp(-50)
print(hero.get_hp())

print(hero._HeroP4__hp)

# PRAKTIKUM 5 - ABSTRACTION
print("\n=== PRAKTIKUM 5 ===")

class GameUnit(ABC):
    @abstractmethod
    def serang(self, target):
        pass

    @abstractmethod
    def info(self):
        pass

class HeroP5(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}")

    def info(self):
        print(f"Saya Hero {self.nama}")

class MonsterP5(GameUnit):
    def __init__(self, jenis):
        self.jenis = jenis

    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}")

    def info(self):
        print(f"Saya Monster {self.jenis}")

h = HeroP5("Alucard")
m = MonsterP5("Serigala")

h.info()
m.info()

# PRAKTIKUM 6 - POLYMORPHISM
print("\n=== PRAKTIKUM 6 ===")

class HeroP6:
    def __init__(self, nama):
        self.nama = nama

    def serang(self):
        print("Hero menyerang")

class MageP6(HeroP6):
    def serang(self):
        print(f"{self.nama} melempar bola api")

class ArcherP6(HeroP6):
    def serang(self):
        print(f"{self.nama} memanah")

class FighterP6(HeroP6):
    def serang(self):
        print(f"{self.nama} menyerang dengan pedang")

pasukan = [
    MageP6("Eudora"),
    ArcherP6("Miya"),
    FighterP6("Zilong")
]

for p in pasukan:
    p.serang()

# PROYEK - TECHMASTER INVENTORY
print("\n=== PROYEK TECHMASTER ===")

class BarangElektronik(ABC):
    def __init__(self, nama, harga):
        self.nama = nama
        self.__stok = 0
        self.__harga = harga

    def get_stok(self):
        return self.__stok

    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {self.__stok}")

    def get_harga(self):
        return self.__harga

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass

class Laptop(BarangElektronik):
    def __init__(self, nama, harga, processor):
        super().__init__(nama, harga)
        self.processor = processor

    def tampilkan_detail(self):
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")

    def hitung_harga_total(self, jumlah):
        pajak = self.get_harga() * 0.10
        return (self.get_harga() + pajak) * jumlah

class Smartphone(BarangElektronik):
    def __init__(self, nama, harga, kamera):
        super().__init__(nama, harga)
        self.kamera = kamera

    def tampilkan_detail(self):
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")

    def hitung_harga_total(self, jumlah):
        pajak = self.get_harga() * 0.05
        return (self.get_harga() + pajak) * jumlah

def proses_transaksi(daftar):
    total = 0
    for barang, jumlah in daftar:
        barang.tampilkan_detail()
        subtotal = barang.hitung_harga_total(jumlah)
        print(f"Beli {jumlah} unit | Subtotal: {subtotal}")
        total += subtotal
    print("TOTAL TAGIHAN:", total)

laptop = Laptop("ROG Zephyrus", 20000000, "Ryzen 9")
hp = Smartphone("iPhone 13", 15000000, "12MP")

laptop.tambah_stok(10)
hp.tambah_stok(-5)
hp.tambah_stok(20)

keranjang = [
    (laptop, 2),
    (hp, 1)
]

proses_transaksi(keranjang)