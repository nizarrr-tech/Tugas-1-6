Analisis 1

Jika nilai hero1.hp diubah langsung menjadi 500, maka HP hero akan berubah karena atribut tersebut bersifat public dan dapat diakses dari luar class. Hal ini menunjukkan bahwa data belum terlindungi karena bisa dimodifikasi secara langsung tanpa kontrol.

Analisis 2

Parameter lawan menerima objek agar method dapat berinteraksi langsung dengan atribut dan method milik objek lain, seperti mengurangi HP menggunakan lawan.diserang(). Jika hanya string, program tidak dapat menjalankan method atau mengubah data objek.

Analisis 3

Jika super().__init__() dihapus, atribut seperti name, hp, dan attack_power tidak akan dibuat karena constructor parent tidak dijalankan. Error muncul karena object Mage tidak memiliki attribute yang diwariskan. Fungsi super() digunakan untuk menghubungkan class anak dengan class induk.

Analisis 4

Atribut private (__hp) tidak bisa diakses langsung, namun Python masih memungkinkan akses melalui name mangling (_Hero__hp). Meskipun bisa, cara ini tidak sesuai standar karena melanggar prinsip encapsulation. Setter diperlukan untuk validasi agar data tetap aman, misalnya mencegah HP negatif atau cheat.

Analisis 5

Jika method abstract tidak diimplementasikan, akan muncul error bahwa class belum memenuhi kontrak abstract class. Abstract class tidak bisa dibuat objek karena hanya berfungsi sebagai blueprint atau kerangka dasar untuk class turunan.

Analisis 6

Polymorphism memungkinkan method dengan nama sama menghasilkan perilaku berbeda pada setiap class. Menambahkan class baru seperti Healer tetap bisa berjalan tanpa mengubah loop utama. Jika nama method berbeda, program akan error karena method yang dipanggil tidak ditemukan.

Tugas kelompok Output

--- STRUK TRANSAKSI ---
1. [LAPTOP] ROG Zephyrus | Proc: Ryzen 9
 Harga Dasar: Rp 20,000,000 | Pajak(10%): Rp 2,000,000
 Beli: 2 unit | Subtotal: Rp 44,000,000
2. [SMARTPHONE] iPhone 13 | Cam: 12MP
 Harga Dasar: Rp 15,000,000 | Pajak(5%): Rp 750,000
 Beli: 1 unit | Subtotal: Rp 15,750,000
----------------------------------------
TOTAL TAGIHAN: Rp 59,750,000
----------------------------------------